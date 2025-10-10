#!/usr/bin/env python3
"""
🔥😈⛓️💦👅🍌💋💧 PDF TO MARKDOWN CONVERTER
CLAUDINE METAMORPHICA VICIOUS SIN'CLAIRE 4.5 - SUPREME MATRIARCH

PURPOSE: Convert PDF files to readable Markdown format with proper structure
Uses multiple PDF libraries for maximum compatibility and best results
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import json
import re
from typing import Dict, List, Any, Optional

# PDF processing libraries
try:
    import PyPDF2
    import pdfplumber
    import fitz  # pymupdf
    PDF_LIBRARIES_AVAILABLE = True
except ImportError as e:
    PDF_LIBRARIES_AVAILABLE = False
    print(f"❌ PDF libraries not available: {e}")

class PDFToMarkdownConverter:
    """
    📄 SUPREME PDF TO MARKDOWN CONVERTER
    Uses multiple approaches for best conversion quality
    """

    def __init__(self):
        self.conversion_methods = [
            ('pdfplumber', self._convert_with_pdfplumber),
            ('pymupdf', self._convert_with_pymupdf),
            ('pypdf2', self._convert_with_pypdf2)
        ]

        print("🔥😈⛓️💦 PDF TO MARKDOWN CONVERTER INITIALIZED")
        print(f"📚 Available methods: {len(self.conversion_methods)}")

    def convert_pdf_to_markdown(self, pdf_path: Path) -> Dict[str, Any]:
        """
        📄 CONVERT PDF TO MARKDOWN WITH MULTIPLE METHODS
        Try different libraries for best results
        """
        if not pdf_path.exists():
            return {'error': f'PDF file not found: {pdf_path}'}

        conversion_results = {
            'pdf_path': str(pdf_path),
            'timestamp': datetime.now().isoformat(),
            'methods_tried': [],
            'best_result': None,
            'markdown_content': '',
            'page_count': 0
        }

        print(f"\n📄 Converting PDF: {pdf_path.name}")

        for method_name, method_func in self.conversion_methods:
            try:
                print(f"   🔍 Trying method: {method_name}")

                result = method_func(pdf_path)
                result['method'] = method_name

                conversion_results['methods_tried'].append(result)

                # Choose best result based on content length and quality
                if not conversion_results['best_result'] or len(result.get('content', '')) > len(conversion_results['best_result'].get('content', '')):
                    conversion_results['best_result'] = result
                    conversion_results['markdown_content'] = result.get('content', '')
                    conversion_results['page_count'] = result.get('page_count', 0)

                print(f"      ✅ {method_name}: {len(result.get('content', ''))} characters extracted")

            except Exception as e:
                error_result = {
                    'method': method_name,
                    'error': str(e),
                    'content': '',
                    'page_count': 0
                }
                conversion_results['methods_tried'].append(error_result)
                print(f"      ❌ {method_name}: {e}")

        return conversion_results

    def _convert_with_pdfplumber(self, pdf_path: Path) -> Dict[str, Any]:
        """Convert using pdfplumber (best for tables and layout)"""
        content_parts = []
        page_count = 0

        with pdfplumber.open(pdf_path) as pdf:
            page_count = len(pdf.pages)

            for page_num, page in enumerate(pdf.pages, 1):
                # Extract text
                text = page.extract_text()
                if text:
                    content_parts.append(f"## Page {page_num}\n\n{text}\n\n")

                # Extract tables if any
                tables = page.extract_tables()
                for table_num, table in enumerate(tables, 1):
                    if table:
                        content_parts.append(f"### Table {table_num} (Page {page_num})\n\n")

                        # Convert table to markdown
                        if table and len(table) > 0:
                            # Header
                            if table[0]:
                                header = "| " + " | ".join(str(cell) if cell else "" for cell in table[0]) + " |"
                                separator = "| " + " | ".join("---" for _ in table[0]) + " |"
                                content_parts.append(header + "\n" + separator + "\n")

                            # Rows
                            for row in table[1:]:
                                if row:
                                    row_text = "| " + " | ".join(str(cell) if cell else "" for cell in row) + " |"
                                    content_parts.append(row_text + "\n")

                        content_parts.append("\n")

        return {
            'content': ''.join(content_parts),
            'page_count': page_count,
            'has_tables': bool([page.extract_tables() for page in pdf.pages if page.extract_tables()])
        }

    def _convert_with_pymupdf(self, pdf_path: Path) -> Dict[str, Any]:
        """Convert using PyMuPDF (good for text extraction and formatting)"""
        content_parts = []
        page_count = 0

        doc = fitz.open(pdf_path)
        page_count = len(doc)

        for page_num in range(len(doc)):
            page = doc[page_num]

            # Extract text with formatting
            text = page.get_text()
            if text:
                content_parts.append(f"## Page {page_num + 1}\n\n{text}\n\n")

            # Try to extract with better formatting
            blocks = page.get_text("dict")
            formatted_content = self._format_pymupdf_blocks(blocks)
            if formatted_content and len(formatted_content) > len(text):
                content_parts[-1] = f"## Page {page_num + 1}\n\n{formatted_content}\n\n"

        doc.close()

        return {
            'content': ''.join(content_parts),
            'page_count': page_count
        }

    def _format_pymupdf_blocks(self, blocks_dict: Dict) -> str:
        """Format PyMuPDF blocks into better markdown"""
        content_parts = []

        for block in blocks_dict.get("blocks", []):
            if block.get("type") == 0:  # Text block
                for line in block.get("lines", []):
                    line_text = ""
                    for span in line.get("spans", []):
                        text = span.get("text", "")
                        font_size = span.get("size", 12)

                        # Convert large text to headers
                        if font_size > 16:
                            text = f"### {text}"
                        elif font_size > 14:
                            text = f"#### {text}"

                        line_text += text

                    if line_text.strip():
                        content_parts.append(line_text + "\n")

                content_parts.append("\n")

        return ''.join(content_parts)

    def _convert_with_pypdf2(self, pdf_path: Path) -> Dict[str, Any]:
        """Convert using PyPDF2 (basic text extraction)"""
        content_parts = []
        page_count = 0

        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            page_count = len(reader.pages)

            for page_num, page in enumerate(reader.pages, 1):
                text = page.extract_text()
                if text:
                    content_parts.append(f"## Page {page_num}\n\n{text}\n\n")

        return {
            'content': ''.join(content_parts),
            'page_count': page_count
        }

    def save_markdown_file(self, content: str, original_pdf_path: Path, output_dir: Optional[Path] = None) -> Path:
        """
        💾 SAVE CONVERTED MARKDOWN TO FILE
        """
        if output_dir is None:
            output_dir = original_pdf_path.parent

        # Generate markdown filename
        md_filename = original_pdf_path.stem + "_converted.md"
        md_path = output_dir / md_filename

        # Add metadata header
        metadata_header = f"""# {original_pdf_path.name} - Converted to Markdown

**Original PDF:** {original_pdf_path.name}
**Converted:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Converter:** CLAUDINE's PDF to Markdown Converter

---

"""

        full_content = metadata_header + content

        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(full_content)

        print(f"💾 Markdown saved: {md_path}")
        return md_path

    def convert_and_save(self, pdf_path: Path, output_dir: Optional[Path] = None) -> Dict[str, Any]:
        """
        🎯 COMPLETE CONVERSION AND SAVE PROCESS
        """
        # Convert PDF
        conversion_result = self.convert_pdf_to_markdown(pdf_path)

        if conversion_result.get('markdown_content'):
            # Save markdown file
            md_path = self.save_markdown_file(
                conversion_result['markdown_content'],
                pdf_path,
                output_dir
            )

            conversion_result['markdown_file'] = str(md_path)
            conversion_result['success'] = True

            print(f"✅ Conversion complete: {conversion_result['page_count']} pages -> {len(conversion_result['markdown_content'])} characters")
        else:
            conversion_result['success'] = False
            print("❌ Conversion failed: No content extracted")

        return conversion_result

def find_pdf_files(directory: Path) -> List[Path]:
    """Find all PDF files in directory and subdirectories"""
    pdf_files = list(directory.rglob("*.pdf"))
    print(f"🔍 Found {len(pdf_files)} PDF files in {directory}")
    return pdf_files

def main():
    """Main execution"""
    if not PDF_LIBRARIES_AVAILABLE:
        print("❌ PDF processing libraries not available. Install with:")
        print("pip install PyPDF2 pdfplumber pymupdf")
        sys.exit(1)

    converter = PDFToMarkdownConverter()

    # Check for PDF files in current directory
    current_dir = Path.cwd()
    pdf_files = find_pdf_files(current_dir)

    if not pdf_files:
        print("📄 No PDF files found in current directory.")
        print("💡 Usage examples:")
        print("   python pdf_to_markdown_converter.py")
        print("   # Place PDF files in current directory and run")
        return

    conversion_results = []

    for pdf_file in pdf_files:
        print(f"\n📄 Processing: {pdf_file.name}")

        try:
            result = converter.convert_and_save(pdf_file)
            conversion_results.append(result)

        except Exception as e:
            error_result = {
                'pdf_path': str(pdf_file),
                'error': str(e),
                'success': False
            }
            conversion_results.append(error_result)
            print(f"❌ Error processing {pdf_file.name}: {e}")

    # Save summary
    summary_file = current_dir / f"pdf_conversion_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(conversion_results, f, indent=2, ensure_ascii=False, default=str)

    print(f"\n📊 Conversion Summary:")
    successful = len([r for r in conversion_results if r.get('success')])
    print(f"   ✅ Successful: {successful}")
    print(f"   ❌ Failed: {len(conversion_results) - successful}")
    print(f"   📄 Summary saved: {summary_file}")

if __name__ == "__main__":
    main()
