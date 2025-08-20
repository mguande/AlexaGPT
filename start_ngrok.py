#!/usr/bin/env python3
"""
Script para iniciar apenas o ngrok
"""

import os
import sys
import subprocess
import time
import requests
import json

def check_ngrok_installed():
    """Verifica se o ngrok está instalado"""
    try:
        result = subprocess.run(['ngrok', 'version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ ngrok encontrado!")
            return True
        else:
            print("❌ ngrok não encontrado!")
            return False
    except FileNotFoundError:
        print("❌ ngrok não encontrado!")
        print("💡 Instale o ngrok: https://ngrok.com/download")
        return False

def kill_ngrok():
    """Mata todos os processos ngrok"""
    try:
        subprocess.run(['taskkill', '/f', '/im', 'ngrok.exe'], capture_output=True)
        print("✅ Processos ngrok finalizados")
        time.sleep(2)
        return True
    except Exception as e:
        print(f"⚠️  Erro ao finalizar ngrok: {e}")
        return False

def check_api_running():
    """Verifica se a API está rodando"""
    try:
        response = requests.get('http://localhost:5000/health', timeout=5)
        if response.status_code == 200:
            print("✅ API está rodando na porta 5000")
            return True
        else:
            print(f"❌ API não respondeu corretamente. Status: {response.status_code}")
            return False
    except requests.exceptions.RequestException:
        print("❌ API não está rodando na porta 5000")
        print("💡 Execute primeiro: python start_api.py")
        return False

def start_ngrok():
    """Inicia o ngrok"""
    print("🌐 Iniciando ngrok...")
    print("=" * 50)
    
    # Verifica se o ngrok está instalado
    if not check_ngrok_installed():
        return False
    
    # Verifica se a API está rodando
    if not check_api_running():
        return False
    
    # Mata processos ngrok existentes
    kill_ngrok()
    
    try:
        # Inicia o ngrok
        print("🚀 Iniciando túnel ngrok...")
        process = subprocess.Popen(['ngrok', 'http', '5000'], 
                                 stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE,
                                 text=True)
        
        # Aguarda inicialização
        time.sleep(5)
        
        # Obtém a URL do ngrok
        try:
            response = requests.get('http://localhost:4040/api/tunnels', timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data['tunnels']:
                    url = data['tunnels'][0]['public_url']
                    print("✅ ngrok iniciado com sucesso!")
                    print(f"🌐 URL pública: {url}")
                    print(f"🔗 Endpoint da Alexa: {url}/alexa")
                    print(f"🧪 Test endpoint: {url}/test")
                    print(f"🔍 Painel ngrok: http://localhost:4040")
                    print("\n📋 Configure no Alexa Developer Console:")
                    print(f"   Endpoint: {url}/alexa")
                    print("\n🎤 Comandos para testar na Alexa:")
                    print("   'Alexa, abra alexagpt'")
                    print("   'Alexa, pergunte ao alexagpt: qual é a capital do Brasil?'")
                    print("\n📋 Para parar o ngrok: Ctrl+C")
                    print("=" * 50)
                    
                    # Aguarda interrupção
                    try:
                        process.wait()
                    except KeyboardInterrupt:
                        print("\n🛑 Parando ngrok...")
                        process.terminate()
                        process.wait()
                        print("✅ ngrok parado!")
                    
                    return True
                else:
                    print("❌ Nenhum túnel ngrok encontrado")
                    process.terminate()
                    return False
            else:
                print(f"❌ Erro ao obter informações do ngrok. Status: {response.status_code}")
                process.terminate()
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao conectar com ngrok: {e}")
            process.terminate()
            return False
            
    except Exception as e:
        print(f"❌ Erro ao iniciar ngrok: {e}")
        return False

def get_ngrok_url():
    """Obtém a URL atual do ngrok"""
    try:
        response = requests.get('http://localhost:4040/api/tunnels', timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data['tunnels']:
                return data['tunnels'][0]['public_url']
        return None
    except:
        return None

def main():
    """Função principal"""
    print("🔧 Script de Inicialização do ngrok")
    print("=" * 50)
    
    # Verifica argumentos
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "url":
            url = get_ngrok_url()
            if url:
                print(f"🌐 URL atual do ngrok: {url}")
                print(f"🔗 Endpoint da Alexa: {url}/alexa")
            else:
                print("❌ ngrok não está rodando")
            return
        
        elif command == "stop":
            if kill_ngrok():
                print("✅ ngrok parado!")
            return
        
        elif command == "status":
            url = get_ngrok_url()
            if url:
                print(f"✅ ngrok ativo: {url}")
            else:
                print("❌ ngrok não está rodando")
            return
    
    # Inicia o ngrok
    start_ngrok()

if __name__ == "__main__":
    main()
