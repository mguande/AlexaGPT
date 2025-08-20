#!/usr/bin/env python3
"""
Script de deploy para AlexaGPT
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def check_python_version():
    """Verifica a versão do Python"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 ou superior é necessário")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detectado")
    return True

def install_dependencies():
    """Instala as dependências"""
    print("📦 Instalando dependências...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False

def create_env_file():
    """Cria arquivo .env se não existir"""
    env_file = Path(".env")
    
    if env_file.exists():
        print("✅ Arquivo .env já existe")
        return True
    
    print("📝 Criando arquivo .env...")
    
    env_content = """# Configurações da API OpenAI
OPENAI_API_KEY=sua_chave_openai_aqui

# Configurações da Alexa Skill
ALEXA_SKILL_ID=amzn1.ask.skill.seu_skill_id_aqui

# Configurações do Servidor
PORT=5000
DEBUG=True

# Configurações de Segurança
SECRET_KEY=sua_chave_secreta_aqui
"""
    
    try:
        with open(env_file, 'w', encoding='utf-8') as f:
            f.write(env_content)
        print("✅ Arquivo .env criado!")
        print("⚠️  IMPORTANTE: Configure suas chaves no arquivo .env")
        return True
    except Exception as e:
        print(f"❌ Erro ao criar arquivo .env: {e}")
        return False

def test_imports():
    """Testa se as importações funcionam"""
    print("🔍 Testando importações...")
    
    try:
        import flask
        import requests
        import openai
        print("✅ Todas as importações funcionando!")
        return True
    except ImportError as e:
        print(f"❌ Erro de importação: {e}")
        return False

def show_next_steps():
    """Mostra os próximos passos"""
    print("\n" + "=" * 60)
    print("🎉 Deploy concluído com sucesso!")
    print("=" * 60)
    print("\n📋 Próximos passos:")
    print("1. Configure suas chaves no arquivo .env:")
    print("   - OPENAI_API_KEY: Obtenha em https://platform.openai.com/")
    print("   - ALEXA_SKILL_ID: Será gerado ao criar a skill")
    print("   - SECRET_KEY: Gere uma chave secreta aleatória")
    print("\n2. Execute a API:")
    print("   python api/app.py")
    print("\n3. Teste a API:")
    print("   python test_api.py")
    print("\n4. Configure a skill da Alexa:")
    print("   - Acesse https://developer.amazon.com/alexa")
    print("   - Crie uma nova skill")
    print("   - Use os arquivos em alexa-skill/")
    print("   - Configure o endpoint da sua API")
    print("\n5. Teste na Alexa:")
    print("   'Alexa, abra alexagpt'")
    print("   'Alexa, pergunte ao alexagpt: [sua pergunta]'")
    print("\n📚 Documentação completa no README.md")

def main():
    """Função principal"""
    print("🚀 Deploy AlexaGPT")
    print("=" * 30)
    
    # Verifica versão do Python
    if not check_python_version():
        return
    
    # Instala dependências
    if not install_dependencies():
        return
    
    # Cria arquivo .env
    if not create_env_file():
        return
    
    # Testa importações
    if not test_imports():
        return
    
    # Mostra próximos passos
    show_next_steps()

if __name__ == "__main__":
    main()

