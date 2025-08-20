#!/usr/bin/env python3
"""
Script para parar todos os serviços AlexaGPT
"""

import subprocess
import time

def stop_all_services():
    """Para todos os serviços"""
    print("🛑 Parando todos os serviços AlexaGPT...")
    print("=" * 50)
    
    # Para processos Python (API)
    try:
        subprocess.run(['taskkill', '/f', '/im', 'python.exe'], capture_output=True)
        print("✅ Processos Python finalizados")
    except Exception as e:
        print(f"⚠️  Erro ao finalizar Python: {e}")
    
    # Para processos ngrok
    try:
        subprocess.run(['taskkill', '/f', '/im', 'ngrok.exe'], capture_output=True)
        print("✅ Processos ngrok finalizados")
    except Exception as e:
        print(f"⚠️  Erro ao finalizar ngrok: {e}")
    
    # Aguarda um pouco
    time.sleep(2)
    
    print("✅ Todos os serviços parados!")
    print("=" * 50)

if __name__ == "__main__":
    stop_all_services()
