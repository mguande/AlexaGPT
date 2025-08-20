#!/usr/bin/env python3
"""
Script simples para iniciar a API AlexaGPT com logs em tempo real
"""

import os
import sys
import subprocess
import time
import requests

def check_port_in_use(port):
    """Verifica se a porta está em uso"""
    try:
        import socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', port))
            return False
    except OSError:
        return True

def kill_process_on_port(port):
    """Mata processo na porta especificada"""
    try:
        result = subprocess.run(['netstat', '-ano'], capture_output=True, text=True)
        lines = result.stdout.split('\n')
        
        for line in lines:
            if f':{port}' in line and 'LISTENING' in line:
                parts = line.split()
                if len(parts) >= 5:
                    pid = parts[-1]
                    subprocess.run(['taskkill', '/f', '/pid', pid], capture_output=True)
                    print(f"✅ Processo {pid} na porta {port} finalizado")
                    return True
        return False
    except Exception as e:
        print(f"❌ Erro ao matar processo: {e}")
        return False

def start_api_simple():
    """Inicia a API Flask de forma simples"""
    print("🚀 Iniciando API AlexaGPT (Modo Simples)...")
    print("=" * 50)
    
    # Verifica se a porta 5000 está em uso
    if check_port_in_use(5000):
        print("⚠️  Porta 5000 está em uso. Tentando finalizar processo...")
        if kill_process_on_port(5000):
            time.sleep(2)
        else:
            print("❌ Não foi possível finalizar o processo na porta 5000")
            print("💡 Tente manualmente: taskkill /f /im python.exe")
            return False
    
    try:
        # Inicia a API diretamente (sem redirecionamento de output)
        print("✅ Iniciando API na porta 5000...")
        print("📋 Logs aparecerão abaixo:")
        print("=" * 50)
        
        # Executa a API diretamente (logs aparecem no console)
        subprocess.run([sys.executable, 'api/app.py'])
        
    except KeyboardInterrupt:
        print("\n🛑 API parada pelo usuário!")
        return True
    except Exception as e:
        print(f"❌ Erro ao iniciar API: {e}")
        return False

def main():
    """Função principal"""
    print("🔧 Script Simples de Inicialização da API AlexaGPT")
    print("=" * 50)
    
    # Verifica se o arquivo da API existe
    if not os.path.exists('api/app.py'):
        print("❌ Arquivo api/app.py não encontrado!")
        print("💡 Certifique-se de estar no diretório correto do projeto")
        return False
    
    # Inicia a API
    return start_api_simple()

if __name__ == "__main__":
    main()
