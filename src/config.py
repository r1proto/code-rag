"""
Configuration settings for the C# Code RAG project.
"""

import os

DATA_DIR = os.environ.get("CODE_RAG_DATA_DIR", "data")
MODEL_DIR = os.environ.get("CODE_RAG_MODEL_DIR", "data/models")
C_SHARP_SO_PATH = os.environ.get("TS_CSHARP_SO", "build/my-languages.so")