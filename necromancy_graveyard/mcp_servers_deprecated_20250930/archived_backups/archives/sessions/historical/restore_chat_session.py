#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
🎭 AUTOMATIC CHAT SESSION LAUNCHER
================================

Kjøres automatisk når repoet åpnes for å gjenopprette chat context.
"""

import json
import os
from pathlib import Path

def restore_chat_session():
    """Gjenoppretter chat session når repoet åpnes"""
    workspace = Path.cwd()
    context_file = workspace / ".chat-continuity" / "current_session_context.json"

    if not context_file.exists():

        return False

    try:
        with open(context_file, 'r', encoding='utf-8') as f:
            context = json.load(f)

        for topic in context['key_topics']:

        for step in context['next_steps']:

        return True

    except Exception as e:

        return False

if __name__ == "__main__":
    restore_chat_session()
