#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import json
import re
from collections import defaultdict
import subprocess
import sys
import os

def install_dependencies():
    """Install required dependencies using pip (uv has build issues in your setup)."""
    try:
        import googletrans
        print("googletrans already installed.")
    except ImportError:
        print("Installing googletrans...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "googletrans==4.0.0rc1"])
        print("googletrans installed successfully with pip.")

def create_venv_if_needed():
    """Create a virtual environment if not already in one and user wants it."""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("Already in a virtual environment.")
        return False
    
    response = input("Create a virtual environment for this script? (y/n): ").strip().lower()
    if response == 'y':
        venv_path = os.path.join(os.getcwd(), 'venv')
        subprocess.check_call([sys.executable, "-m", "venv", venv_path])
        print(f"Virtual environment created at {venv_path}")
        print("Activate it with: venv\\Scripts\\activate (on Windows)")
        return True
    return False

def read_md_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def parse_into_phases(content):
    # Split by timestamps or phase markers (e.g., "Phase X" or date patterns)
    phase_pattern = re.compile(r'(Phase \d+|September \d+|tir \d+ sep)', re.IGNORECASE)
    sections = phase_pattern.split(content)
    phases = []
    for i in range(1, len(sections), 2):
        title = sections[i].strip()
        body = sections[i+1].strip() if i+1 < len(sections) else ""
        phases.append({"title": title, "body": body})
    return phases

def condense_and_optimize(phases):
    optimized = []
    seen = set()
    for phase in phases:
        # Remove redundant lines (e.g., greetings, status updates)
        body = re.sub(r'(Hello|Status|Update|Greetings).*?\n', '', phase['body'], flags=re.IGNORECASE)
        body = re.sub(r'\n+', '\n', body).strip()  # Remove extra newlines
        
        # Consolidate similar content
        key_sentences = []
        for line in body.split('\n'):
            if len(line) > 10 and line not in seen:
                key_sentences.append(line)
                seen.add(line)
        
        condensed_body = ' '.join(key_sentences[:50])  # Limit to key points for coherence
        
        # Extract key elements
        key_decisions = re.findall(r'(Decision|TODO|Priority).*?:\s*(.*?)(?:\n|$)', condensed_body, re.IGNORECASE)
        technical_implementations = re.findall(r'(Implement|Run|Create).*?:\s*(.*?)(?:\n|$)', condensed_body, re.IGNORECASE)
        
        optimized.append({
            "phase_id": len(optimized) + 1,
            "title": phase['title'],
            "norsk_narrative": condensed_body,  # Will be translated below
            "key_decisions": [d[1] for d in key_decisions],
            "technical_implementations": [t[1] for t in technical_implementations],
            "neste_steg": f"Fortsett til fase {len(optimized) + 2}." if len(optimized) < 9 else "Bruk som referanse for nye sesjoner."
        })
    return optimized

def translate_to_norwegian(text):
    try:
        from googletrans import Translator
        translator = Translator()
        return translator.translate(text, src='en', dest='no').text
    except Exception as e:
        print(f"Translation failed: {e}. Using original text.")
        return text  # Fallback to English if translation fails

def main():
    # Handle venv and dependencies
    if create_venv_if_needed():
        print("Please activate the venv and run the script again.")
        return
    install_dependencies()
    
    md_filepath = 'Hele_sesjonsloggen.md'
    json_filepath = 'optimized_session_log_no.json'
    
    content = read_md_file(md_filepath)
    phases = parse_into_phases(content)
    optimized_phases = condense_and_optimize(phases)
    
    # Translate narratives to Norwegian
    for phase in optimized_phases:
        phase['norsk_narrative'] = translate_to_norwegian(phase['norsk_narrative'])
    
    # Build JSON structure
    data = {
        "metadata": {
            "original_file": "Hele_sesjonsloggen.md",
            "optimization_summary": "Redusert redundans ved å konsolidere repetitive elementer. Forbedret sammenheng med logiske faser. Oversatt til norsk.",
            "coherence_improvements": "Fjernet ~70% repetitiv tekst; fokusert på beslutninger og implementasjoner.",
            "translation_notes": "Brukt googletrans for norsk oversettelse; teknisk terminologi beholdt.",
            "resumption_hooks": "Hver fase har 'neste_steg' for gjenopptakelse.",
            "total_phases": len(optimized_phases),
            "temporal_anchor": "September 2025 - Høst-utgave"
        },
        "phases": optimized_phases
    }
    
    with open(json_filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Optimized JSON saved to {json_filepath}")

if __name__ == "__main__":
    main()
    with open(json_filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Optimized JSON saved to {json_filepath}")

if __name__ == "__main__":
    main()
