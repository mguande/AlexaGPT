#!/usr/bin/env python3
"""
Script para configurar o arquivo .env
"""

import os
import secrets
from pathlib import Path

def generate_secret_key():
    """Gera uma chave secreta aleatória"""
    return secrets.token_urlsafe(32)

def create_env_file():
    """Cria o arquivo .env"""
    env_file = Path(".env")
    
    if env_file.exists():
        print("✅ Arquivo .env já existe!")
        return True
    
    print("📝 Criando arquivo .env...")
    
    # Gera chave secreta
    secret_key = generate_secret_key()
    
    env_content = f"""# Configurações da API OpenAI
OPENAI_API_KEY=sua_chave_openai_aqui

# Configurações da Alexa Skill
ALEXA_SKILL_ID=amzn1.ask.skill.seu_skill_id_aqui

# Configurações do Servidor
PORT=5000
DEBUG=True

# Configurações de Segurança
SECRET_KEY={secret_key}
"""
    
    try:
        with open(env_file, 'w', encoding='utf-8') as f:
            f.write(env_content)
        print("✅ Arquivo .env criado com sucesso!")
        print("\n📋 Próximos passos:")
        print("1. Obtenha sua chave OpenAI em: https://platform.openai.com/api-keys")
        print("2. Substitua 'sua_chave_openai_aqui' pela sua chave real")
        print("3. Quando criar a skill da Alexa, substitua o ALEXA_SKILL_ID")
        return True
    except Exception as e:
        print(f"❌ Erro ao criar arquivo .env: {e}")
        return False

def show_openai_instructions():
    """Mostra instruções para obter a chave OpenAI"""
    print("\n🔑 Como obter sua chave OpenAI:")
    print("1. Acesse: https://platform.openai.com/")
    print("2. Faça login ou crie uma conta")
    print("3. Vá para 'API Keys' no menu lateral")
    print("4. Clique em 'Create new secret key'")
    print("5. Dê um nome como 'AlexaGPT'")
    print("6. Copie a chave (começa com 'sk-...')")
    print("7. Cole no arquivo .env substituindo 'sua_chave_openai_aqui'")

def main():
    """Função principal"""
    print("🔧 Configurando arquivo .env para AlexaGPT")
    print("=" * 50)
    
    # Cria arquivo .env
    if create_env_file():
        show_openai_instructions()
        
        print("\n💡 Dica: A chave OpenAI é necessária para respostas inteligentes.")
        print("   Sem ela, a API usará respostas básicas de fallback.")
        
        print("\n🎯 Após configurar a chave:")
        print("   - Reinicie a API: python start_dev.py")
        print("   - Teste na Alexa: 'Alexa, pergunte ao alexagpt: qual é a capital do Brasil?'")

if __name__ == "__main__":
    main()
