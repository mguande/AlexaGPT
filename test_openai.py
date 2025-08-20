#!/usr/bin/env python3
"""
Script para testar a conexão com OpenAI
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

def test_openai_connection():
    """Testa a conexão com OpenAI"""
    print("🔍 Testando conexão com OpenAI...")
    
    # Carrega variáveis de ambiente
    load_dotenv()
    
    # Obtém a chave
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key or api_key == 'sua_chave_openai_aqui':
        print("❌ Chave OpenAI não configurada!")
        print("📝 Configure a chave no arquivo .env")
        print("🔗 Obtenha em: https://platform.openai.com/api-keys")
        return False
    
    try:
        # Inicializa cliente
        client = OpenAI(api_key=api_key)
        
        # Testa com uma pergunta simples
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": "Olá! Como você está?"}
            ],
            max_tokens=50
        )
        
        answer = response.choices[0].message.content
        print("✅ Conexão com OpenAI funcionando!")
        print(f"🤖 Resposta: {answer}")
        return True
        
    except Exception as e:
        print(f"❌ Erro na conexão com OpenAI: {str(e)}")
        return False

def main():
    """Função principal"""
    print("🧪 Teste de Conexão OpenAI")
    print("=" * 30)
    
    if test_openai_connection():
        print("\n🎉 Tudo funcionando! Sua AlexaGPT terá respostas inteligentes!")
        print("\n🚀 Próximos passos:")
        print("1. Reinicie a API: python start_dev.py")
        print("2. Teste na Alexa: 'Alexa, pergunte ao alexagpt: qual é a capital do Brasil?'")
    else:
        print("\n⚠️  Configure a chave OpenAI primeiro!")

if __name__ == "__main__":
    main()
