#!/usr/bin/env python3
"""
Gerenciador do ngrok para AlexaGPT
"""

import subprocess
import time
import requests
import json
import os
import signal
import sys

def kill_ngrok():
    """Mata todos os processos ngrok"""
    try:
        subprocess.run(['taskkill', '/f', '/im', 'ngrok.exe'], capture_output=True)
        print("✅ Processos ngrok finalizados")
    except:
        pass

def start_ngrok(port=5000):
    """Inicia o ngrok"""
    try:
        # Mata processos existentes
        kill_ngrok()
        
        # Aguarda um pouco
        time.sleep(2)
        
        # Inicia novo processo
        print("🌐 Iniciando ngrok...")
        process = subprocess.Popen(['ngrok', 'http', str(port)], 
                                 stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE)
        
        # Aguarda inicialização
        time.sleep(5)
        
        # Verifica se está funcionando
        try:
            response = requests.get('http://localhost:4040/api/tunnels', timeout=5)
            if response.status_code == 200:
                data = response.json()
                url = data['tunnels'][0]['public_url']
                print(f"✅ ngrok iniciado: {url}")
                return url
            else:
                print("❌ ngrok não respondeu corretamente")
                return None
        except Exception as e:
            print(f"❌ Erro ao verificar ngrok: {e}")
            return None
            
    except Exception as e:
        print(f"❌ Erro ao iniciar ngrok: {e}")
        return None

def get_ngrok_url():
    """Obtém a URL atual do ngrok"""
    try:
        response = requests.get('http://localhost:4040/api/tunnels', timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data['tunnels'][0]['public_url']
        return None
    except:
        return None

def check_ngrok_status():
    """Verifica o status do ngrok"""
    url = get_ngrok_url()
    if url:
        print(f"✅ ngrok ativo: {url}")
        return True
    else:
        print("❌ ngrok não está funcionando")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "start":
            url = start_ngrok()
            if url:
                print(f"🔗 Endpoint da Alexa: {url}/alexa")
            else:
                print("❌ Falha ao iniciar ngrok")
        
        elif command == "stop":
            kill_ngrok()
            print("🛑 ngrok parado")
        
        elif command == "status":
            check_ngrok_status()
        
        elif command == "restart":
            kill_ngrok()
            time.sleep(2)
            url = start_ngrok()
            if url:
                print(f"🔄 ngrok reiniciado: {url}")
                print(f"🔗 Endpoint da Alexa: {url}/alexa")
            else:
                print("❌ Falha ao reiniciar ngrok")
    else:
        print("Uso: python manage_ngrok.py [start|stop|status|restart]")
