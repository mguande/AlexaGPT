#!/usr/bin/env python3
"""
Script para Windows - Inicia a API AlexaGPT diretamente
"""

import os
import sys
import subprocess
import time

def main():
    """Inicia a API diretamente no Windows"""
    print("🚀 Iniciando API AlexaGPT (Windows)...")
    print("📋 Logs aparecerão abaixo:")
    print("=" * 50)
    
    # Verifica se o arquivo existe
    if not os.path.exists('api/app.py'):
        print("❌ Arquivo api/app.py não encontrado!")
        return False
    
    try:
        # Executa a API diretamente (logs aparecem no console)
        print("✅ Executando API...")
        print("📋 Para parar: Ctrl+C")
        print("=" * 50)
        
        # Executa diretamente sem redirecionamento
        subprocess.run([sys.executable, 'api/app.py'])
        
    except KeyboardInterrupt:
        print("\n🛑 API parada pelo usuário!")
        return True
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == "__main__":
    main()
