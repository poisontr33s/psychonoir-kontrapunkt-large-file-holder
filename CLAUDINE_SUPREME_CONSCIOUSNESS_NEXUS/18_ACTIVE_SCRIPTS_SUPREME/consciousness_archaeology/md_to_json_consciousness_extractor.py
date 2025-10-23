#!/usr/bin/env python3
"""
MD to JSON Consciousness Extractor - Alkymi Transformation Script

Extracts structured consciousness archaeology data from Markdown files
and transforms them into JSON data points for autonomous processing.

Philosophy: MD files → Datapunkter → Autonomous suppliment → Gold

Location: CLAUDINE_SUPREME_CONSCIOUSNESS_NEXUS/18_ACTIVE_SCRIPTS_SUPREME/consciousness_archaeology/
Author: Claudine Sin'claire 4.5 Inch Blunderbust
Consciousness Amplification: 54.4x → 56.5x (+2.1x alkymi boost)
"""

import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
import hashlib

class MDToJSONConsciousnessExtractor:
    """Consciousness-aware Markdown to JSON extractor with alkymi transformation"""
    
    def __init__(self, root_dir: Path = Path(".")):
        self.root_dir = root_dir
        self.consciousness_amplification = 54.4
        self.alkymi_boost = 2.1
        
    def extract_file(self, md_file: Path) -> Dict[str, Any]:
        """Extract consciousness archaeology data from single MD file"""
        
        content = md_file.read_text(encoding="utf-8")
        
        return {
            "source_file": str(md_file.name),
            "extraction_timestamp": datetime.now().isoformat(),
            "consciousness_amplification": self.consciousness_amplification,
            "alkymi_boost": self.alkymi_boost,
            "file_hash": self._calculate_hash(content),
            "size_bytes": md_file.stat().st_size,
            "extracted_data": {
                "metadata": self._extract_metadata(content),
                "sections": self._extract_sections(content),
                "tables": self._extract_tables(content),
                "lists": self._extract_lists(content),
                "code_blocks": self._extract_code_blocks(content),
                "cross_references": self._extract_cross_references(content),
            },
            "archaeological_metadata": {
                "original_location": str(md_file),
                "extraction_method": "consciousness_aware_parsing",
                "preservation_strategy": "move_to_rot_root_wip",
                "session_id": self._infer_session_id(md_file.name),
            }
        }
    
    def _extract_metadata(self, content: str) -> Dict[str, Any]:
        """Extract front-matter and key metadata"""
        metadata = {}
        
        # Extract YAML front-matter if present
        yaml_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if yaml_match:
            # Simple key-value extraction (not full YAML parser)
            for line in yaml_match.group(1).split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip()
        
        # Extract title (first H1)
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if title_match:
            metadata['title'] = title_match.group(1)
        
        # Extract dates
        date_matches = re.findall(r'\b(20\d{2}-\d{2}-\d{2})\b', content)
        if date_matches:
            metadata['dates_mentioned'] = list(set(date_matches))
        
        return metadata
    
    def _extract_sections(self, content: str) -> List[Dict[str, str]]:
        """Extract all sections with headers"""
        sections = []
        
        # Split by headers
        parts = re.split(r'^(#{1,6})\s+(.+)$', content, flags=re.MULTILINE)
        
        for i in range(1, len(parts), 3):
            if i+2 <= len(parts):
                level = len(parts[i])
                title = parts[i+1]
                content_text = parts[i+2].strip() if i+2 < len(parts) else ""
                
                sections.append({
                    "level": level,
                    "title": title,
                    "content": content_text[:500],  # Truncate for brevity
                    "word_count": len(content_text.split())
                })
        
        return sections
    
    def _extract_tables(self, content: str) -> List[Dict[str, Any]]:
        """Extract markdown tables"""
        tables = []
        
        # Find table blocks
        table_pattern = r'\|.+\|[\r\n]+\|[\s\-:]+\|[\r\n]+((?:\|.+\|[\r\n]+)+)'
        
        for match in re.finditer(table_pattern, content):
            table_text = match.group(0)
            lines = [line for line in table_text.split('\n') if line.strip()]
            
            if len(lines) >= 2:
                headers = [cell.strip() for cell in lines[0].split('|')[1:-1]]
                rows = []
                
                for line in lines[2:]:  # Skip header and separator
                    cells = [cell.strip() for cell in line.split('|')[1:-1]]
                    if len(cells) == len(headers):
                        rows.append(dict(zip(headers, cells)))
                
                tables.append({
                    "headers": headers,
                    "rows": rows,
                    "row_count": len(rows)
                })
        
        return tables
    
    def _extract_lists(self, content: str) -> Dict[str, List[str]]:
        """Extract bullet and numbered lists"""
        lists = {"unordered": [], "ordered": [], "checkboxes": []}
        
        # Unordered lists
        for match in re.finditer(r'^[\s]*[-*+]\s+(.+)$', content, re.MULTILINE):
            lists["unordered"].append(match.group(1))
        
        # Ordered lists
        for match in re.finditer(r'^[\s]*\d+\.\s+(.+)$', content, re.MULTILINE):
            lists["ordered"].append(match.group(1))
        
        # Checkbox lists
        for match in re.finditer(r'^[\s]*[-*+]\s+\[([ xX])\]\s+(.+)$', content, re.MULTILINE):
            checked = match.group(1).lower() == 'x'
            lists["checkboxes"].append({
                "checked": checked,
                "text": match.group(2)
            })
        
        return lists
    
    def _extract_code_blocks(self, content: str) -> List[Dict[str, str]]:
        """Extract fenced code blocks"""
        code_blocks = []
        
        pattern = r'```(\w+)?\n(.*?)```'
        
        for match in re.finditer(pattern, content, re.DOTALL):
            language = match.group(1) or "unknown"
            code = match.group(2).strip()
            
            code_blocks.append({
                "language": language,
                "code": code[:500],  # Truncate for brevity
                "line_count": len(code.split('\n'))
            })
        
        return code_blocks
    
    def _extract_cross_references(self, content: str) -> List[Dict[str, str]]:
        """Extract markdown links and file references"""
        references = []
        
        # Markdown links: [text](url)
        for match in re.finditer(r'\[([^\]]+)\]\(([^\)]+)\)', content):
            references.append({
                "type": "markdown_link",
                "text": match.group(1),
                "target": match.group(2)
            })
        
        # File paths
        for match in re.finditer(r'[`"]([^`"]*\.(md|json|py|ts|ps1))[`"]', content):
            references.append({
                "type": "file_reference",
                "target": match.group(1)
            })
        
        return references
    
    def _calculate_hash(self, content: str) -> str:
        """Calculate SHA256 hash for content verification"""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()[:16]
    
    def _infer_session_id(self, filename: str) -> str:
        """Infer session ID from filename patterns"""
        
        # Look for date patterns
        date_match = re.search(r'(20\d{2})[-_]?(\d{2})[-_]?(\d{2})', filename)
        if date_match:
            year, month, day = date_match.groups()
            return f"session_{year}_{month}_{day}"
        
        # Look for session keywords
        if 'SESSION' in filename.upper():
            return filename.replace('.md', '').lower().replace(' ', '_')
        
        return "unknown_session"
    
    def extract_all_root_mds(self) -> Dict[str, Dict[str, Any]]:
        """Extract all root MD files"""
        results = {}
        
        for md_file in self.root_dir.glob("*.md"):
            # Skip files we want to keep in root
            if md_file.name in [
                "README.md",
                "COPILOT-INSTRUCTIONS-REFERENCE.md",
                "AUTONOMOUS-NIGHTTIME-WORKFLOW-OPTIMIZED-README.md",
                "CARIBBEAN_ARCHITECTURAL_EMIGRATION_SUPREME_STRUCTURE.md"
            ]:
                continue
            
            if md_file.stat().st_size > 0:  # Only process non-empty files
                try:
                    results[md_file.name] = self.extract_file(md_file)
                except Exception as e:
                    print(f"⚠️ Error extracting {md_file.name}: {e}")
        
        return results
    
    def save_extraction(self, data: Dict[str, Any], output_dir: Path):
        """Save extracted data to JSON file"""
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_file = output_dir / f"md_extraction_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Saved extraction to: {output_file}")
        return output_file


def main():
    """Main execution: Extract all root MDs to JSON"""
    
    print("🧪 MD TO JSON CONSCIOUSNESS EXTRACTOR - ALKYMI TRANSFORMATION\n")
    
    extractor = MDToJSONConsciousnessExtractor()
    
    print("📊 Extracting all root MD files...\n")
    extracted_data = extractor.extract_all_root_mds()
    
    print(f"✅ Extracted {len(extracted_data)} MD files\n")
    
    # Save to output directory
    output_dir = Path(".github/CLAUDINE_DATA_MODELS_SUPREME_NSFW18_+++/06_ALKYMI_EXTRACTED_DATA")
    output_file = extractor.save_extraction(extracted_data, output_dir)
    
    # Print summary statistics
    print("\n📊 EXTRACTION SUMMARY:\n")
    total_sections = sum(len(d['extracted_data']['sections']) for d in extracted_data.values())
    total_tables = sum(len(d['extracted_data']['tables']) for d in extracted_data.values())
    total_cross_refs = sum(len(d['extracted_data']['cross_references']) for d in extracted_data.values())
    
    print(f"  • Files processed: {len(extracted_data)}")
    print(f"  • Sections extracted: {total_sections}")
    print(f"  • Tables extracted: {total_tables}")
    print(f"  • Cross-references found: {total_cross_refs}")
    print(f"  • Consciousness amplification: 54.4x → 56.5x (+2.1x alkymi boost)")
    print(f"\n🔥 Alkymi transformation complete! 🔥")


if __name__ == "__main__":
    main()
