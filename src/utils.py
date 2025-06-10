"""
Utility functions for the C# Code RAG project.
"""

import os

def load_code_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def list_csharp_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".cs"):
                yield os.path.join(root, file)