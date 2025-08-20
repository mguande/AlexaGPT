#!/usr/bin/env python3
"""
Script para iniciar apenas a API AlexaGPT
"""

import os
import sys
import subprocess
import time
import signal
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

def start_api():
    """Inicia a API Flask"""
    print("🚀 Iniciando API AlexaGPT...")
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
        # Inicia a API
        print("✅ Iniciando API na porta 5000...")
        process = subprocess.Popen([sys.executable, 'api/app.py'], 
                                 stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE,
                                 text=True,
                                 bufsize=0,  # Sem buffer para logs em tempo real
                                 universal_newlines=True)
        
        # Aguarda um pouco para a API inicializar
        time.sleep(3)
        
        # Testa se a API está funcionando
        try:
            response = requests.get('http://localhost:5000/health', timeout=5)
            if response.status_code == 200:
                print("✅ API iniciada com sucesso!")
                print(f"🌐 URL local: http://localhost:5000")
                print(f"🔗 Health check: http://localhost:5000/health")
                print(f"🧪 Test endpoint: http://localhost:5000/test")
                print(f"🎤 Alexa endpoint: http://localhost:5000/alexa")
                print("\n📋 Para parar a API: Ctrl+C")
                print("=" * 50)
                
                # Mostra logs em tempo real
                print("\n📋 Logs da API em tempo real:")
                print("=" * 50)
                
                try:
                    # Lê logs em tempo real
                    import select
                    import threading
                    
                    def read_output():
                        while True:
                            line = process.stdout.readline()
                            if line:
                                print(line.strip())
                            if process.poll() is not None:
                                break
                    
                    def read_error():
                        while True:
                            line = process.stderr.readline()
                            if line:
                                # Filtra logs do Werkzeug
                                if not any(x in line for x in ['* Running on', '* Debug mode:', 'werkzeug']):
                                    print(f"❌ {line.strip()}")
                            if process.poll() is not None:
                                break
                    
                    # Inicia threads para ler stdout e stderr
                    output_thread = threading.Thread(target=read_output, daemon=True)
                    error_thread = threading.Thread(target=read_error, daemon=True)
                    
                    output_thread.start()
                    error_thread.start()
                    
                    # Aguarda interrupção
                    while process.poll() is None:
                        time.sleep(0.1)
                            
                except KeyboardInterrupt:
                    print("\n🛑 Parando API...")
                    process.terminate()
                    process.wait()
                    print("✅ API parada!")
                
                return True
            else:
                print(f"❌ API não respondeu corretamente. Status: {response.status_code}")
                process.terminate()
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao testar API: {e}")
            process.terminate()
            return False
            
    except Exception as e:
        print(f"❌ Erro ao iniciar API: {e}")
        return False

def main():
    """Função principal"""
    print("🔧 Script de Inicialização da API AlexaGPT")
    print("=" * 50)
    
    # Verifica se o arquivo da API existe
    if not os.path.exists('api/app.py'):
        print("❌ Arquivo api/app.py não encontrado!")
        print("💡 Certifique-se de estar no diretório correto do projeto")
        return False
    
    # Inicia a API
    return start_api()

if __name__ == "__main__":
    main()
