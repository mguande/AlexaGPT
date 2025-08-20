#!/usr/bin/env python3
"""
Script automático para iniciar API + ngrok para desenvolvimento
"""

import subprocess
import time
import requests
import json
import os
import sys
from pathlib import Path

def check_ngrok():
    """Verifica se o ngrok está instalado"""
    try:
        result = subprocess.run(["ngrok", "version"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ ngrok encontrado!")
            return True
        else:
            print("❌ ngrok não encontrado")
            return False
    except FileNotFoundError:
        print("❌ ngrok não está instalado")
        print("📥 Instale em: https://ngrok.com/download")
        return False

def start_api():
    """Inicia a API em background"""
    print("🚀 Iniciando API...")
    
    # Verifica se a API já está rodando
    try:
        response = requests.get('http://localhost:5000/health', timeout=2)
        if response.status_code == 200:
            print("✅ API já está rodando!")
            return None
    except:
        pass
    
    # Inicia a API
    try:
        api_process = subprocess.Popen(
            [sys.executable, "api/app.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(3)  # Aguarda inicializar
        
        # Verifica se iniciou corretamente
        try:
            response = requests.get('http://localhost:5000/health', timeout=5)
            if response.status_code == 200:
                print("✅ API iniciada com sucesso!")
                return api_process
            else:
                print("❌ Erro ao iniciar API")
                return None
        except:
            print("❌ Erro ao verificar API")
            return None
            
    except Exception as e:
        print(f"❌ Erro ao iniciar API: {e}")
        return None

def start_ngrok():
    """Inicia ngrok"""
    print("🌐 Iniciando ngrok...")
    
    try:
        ngrok_process = subprocess.Popen(
            ["ngrok", "http", "5000"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(5)  # Aguarda ngrok inicializar
        return ngrok_process
    except Exception as e:
        print(f"❌ Erro ao iniciar ngrok: {e}")
        return None

def get_ngrok_url():
    """Obtém a URL pública do ngrok"""
    try:
        response = requests.get("http://localhost:4040/api/tunnels", timeout=5)
        if response.status_code == 200:
            tunnels = response.json()["tunnels"]
            for tunnel in tunnels:
                if tunnel["proto"] == "https":
                    return tunnel["public_url"]
        return None
    except Exception as e:
        print(f"❌ Erro ao obter URL do ngrok: {e}")
        return None

def test_endpoint(url):
    """Testa o endpoint da API"""
    try:
        response = requests.get(f"{url}/health", timeout=10)
        if response.status_code == 200:
            print("✅ Endpoint testado com sucesso!")
            return True
        else:
            print(f"❌ Erro no endpoint: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erro ao testar endpoint: {e}")
        return False

def main():
    """Função principal"""
    print("🔧 Iniciando ambiente de desenvolvimento AlexaGPT")
    print("=" * 60)
    
    # Verifica ngrok
    if not check_ngrok():
        print("\n📋 Para instalar ngrok:")
        print("1. Acesse: https://ngrok.com/download")
        print("2. Baixe para Windows")
        print("3. Extraia e adicione ao PATH")
        print("4. Configure seu authtoken: ngrok config add-authtoken SEU_TOKEN")
        return
    
    # Inicia API
    api_process = start_api()
    if api_process is None and not api_process:
        print("❌ Não foi possível iniciar a API")
        return
    
    # Inicia ngrok
    ngrok_process = start_ngrok()
    if ngrok_process is None:
        print("❌ Não foi possível iniciar ngrok")
        if api_process:
            api_process.terminate()
        return
    
    # Aguarda um pouco mais para ngrok inicializar completamente
    time.sleep(3)
    
    # Obtém URL
    url = get_ngrok_url()
    if not url:
        print("❌ Não foi possível obter URL do ngrok")
        print("🔍 Verifique se o ngrok está rodando em: http://localhost:4040")
        if api_process:
            api_process.terminate()
        if ngrok_process:
            ngrok_process.terminate()
        return
    
    print(f"\n✅ URL pública: {url}")
    print(f"🔗 Endpoint da Alexa: {url}/alexa")
    
    # Testa o endpoint
    if test_endpoint(url):
        print("\n📋 Configure no Alexa Developer Console:")
        print(f"   Endpoint: {url}/alexa")
        print("\n🎤 Comandos para testar na Alexa:")
        print("   'Alexa, abra alexagpt'")
        print("   'Alexa, pergunte ao alexagpt: qual é a capital do Brasil?'")
        
        print("\n🔍 Para ver logs do ngrok: http://localhost:4040")
        print("⏹️  Pressione Ctrl+C para parar")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Parando serviços...")
            if api_process:
                api_process.terminate()
            if ngrok_process:
                ngrok_process.terminate()
            print("✅ Serviços parados!")
    else:
        print("❌ Falha ao testar endpoint")
        if api_process:
            api_process.terminate()
        if ngrok_process:
            ngrok_process.terminate()

if __name__ == "__main__":
    main()
