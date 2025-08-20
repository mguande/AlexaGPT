#!/usr/bin/env python3
"""
Script para monitorar logs da API em tempo real
"""

import subprocess
import sys
import time
import requests

def check_api_running():
    """Verifica se a API está rodando"""
    try:
        response = requests.get('http://localhost:5000/health', timeout=2)
        return response.status_code == 200
    except:
        return False

def monitor_api_logs():
    """Monitora logs da API em tempo real"""
    print("📊 Monitor de Logs da API AlexaGPT")
    print("=" * 50)
    
    if not check_api_running():
        print("❌ API não está rodando!")
        print("💡 Execute primeiro: python start_api.py")
        return False
    
    print("✅ API está rodando. Monitorando logs...")
    print("📋 Para parar o monitor: Ctrl+C")
    print("=" * 50)
    
    try:
        # Monitora logs usando tail (se disponível) ou lê arquivo de log
        while True:
            # Verifica se a API ainda está rodando
            if not check_api_running():
                print("❌ API parou de funcionar!")
                break
            
            # Aguarda um pouco antes de verificar novamente
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Monitor de logs parado!")
        return True

def show_api_status():
    """Mostra status da API"""
    print("📊 Status da API AlexaGPT")
    print("=" * 50)
    
    if check_api_running():
        print("✅ API está rodando")
        try:
            response = requests.get('http://localhost:5000/health', timeout=2)
            data = response.json()
            print(f"📋 Status: {data['status']}")
            print(f"🔧 Serviço: {data['service']}")
            print(f"📦 Versão: {data['version']}")
        except Exception as e:
            print(f"⚠️  Erro ao obter status: {e}")
    else:
        print("❌ API não está rodando")
        print("💡 Execute: python start_api.py")

def main():
    """Função principal"""
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "status":
            show_api_status()
            return
        
        elif command == "monitor":
            monitor_api_logs()
            return
    
    # Comportamento padrão: mostra status
    show_api_status()

if __name__ == "__main__":
    main()
