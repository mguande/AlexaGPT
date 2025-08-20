#!/usr/bin/env python3
"""
Executa a API AlexaGPT diretamente
"""

import os
import sys

# Adiciona o diretório atual ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Executa a API diretamente
exec(open('api/app.py').read())
