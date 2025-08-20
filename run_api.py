#!/usr/bin/env python3
"""
Script direto para executar a API AlexaGPT
"""

import os
import sys

def main():
    """Executa a API diretamente"""
    print("🚀 Iniciando API AlexaGPT...")
    print("📋 Logs aparecerão abaixo:")
    print("=" * 50)
    
    # Verifica se o arquivo existe
    if not os.path.exists('api/app.py'):
        print("❌ Arquivo api/app.py não encontrado!")
        return False
    
    # Executa a API diretamente
    os.execv(sys.executable, [sys.executable, 'api/app.py'])

if __name__ == "__main__":
    main()
