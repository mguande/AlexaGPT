#!/usr/bin/env python3
"""
Script de teste para a API AlexaGPT
"""

import requests
import json
import time

def test_health_endpoint():
    """Testa o endpoint de saúde"""
    print("🔍 Testando endpoint de saúde...")
    
    try:
        response = requests.get('http://localhost:5000/health')
        if response.status_code == 200:
            print("✅ Endpoint de saúde funcionando!")
            print(f"   Resposta: {response.json()}")
        else:
            print(f"❌ Erro no endpoint de saúde: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro ao conectar: {str(e)}")

def test_ai_endpoint():
    """Testa o endpoint de IA"""
    print("\n🤖 Testando endpoint de IA...")
    
    test_questions = [
        "Olá, como você está?",
        "Qual é a capital do Brasil?",
        "Como fazer um bolo de chocolate?",
        "Quem foi Albert Einstein?"
    ]
    
    for question in test_questions:
        print(f"\n📝 Testando pergunta: '{question}'")
        
        try:
            data = {
                'question': question
            }
            
            response = requests.post(
                'http://localhost:5000/test',
                json=data,
                headers={'Content-Type': 'application/json'}
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Resposta recebida!")
                print(f"   Pergunta: {result['question']}")
                print(f"   Resposta: {result['response'][:100]}...")
            else:
                print(f"❌ Erro: {response.status_code}")
                print(f"   Resposta: {response.text}")
                
        except Exception as e:
            print(f"❌ Erro ao testar: {str(e)}")
        
        time.sleep(1)  # Pausa entre testes

def test_alexa_endpoint():
    """Testa o endpoint da Alexa"""
    print("\n🎤 Testando endpoint da Alexa...")
    
    # Simula uma requisição da Alexa
    alexa_request = {
        "version": "1.0",
        "session": {
            "sessionId": "test-session-123",
            "application": {
                "applicationId": "test-app-id"
            },
            "user": {
                "userId": "test-user-123"
            }
        },
        "request": {
            "type": "IntentRequest",
            "requestId": "test-request-123",
            "timestamp": "2023-01-01T00:00:00Z",
            "intent": {
                "name": "AskQuestion",
                "slots": {
                    "question": {
                        "name": "question",
                        "value": "Qual é a capital do Brasil?"
                    }
                }
            }
        }
    }
    
    try:
        response = requests.post(
            'http://localhost:5000/alexa',
            json=alexa_request,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Requisição da Alexa processada!")
            print(f"   Versão: {result.get('version')}")
            print(f"   Speech: {result.get('response', {}).get('outputSpeech', {}).get('text', 'N/A')[:100]}...")
        else:
            print(f"❌ Erro: {response.status_code}")
            print(f"   Resposta: {response.text}")
            
    except Exception as e:
        print(f"❌ Erro ao testar endpoint da Alexa: {str(e)}")

def main():
    """Função principal de teste"""
    print("🚀 Iniciando testes da API AlexaGPT")
    print("=" * 50)
    
    # Testa se o servidor está rodando
    test_health_endpoint()
    
    # Testa o endpoint de IA
    test_ai_endpoint()
    
    # Testa o endpoint da Alexa
    test_alexa_endpoint()
    
    print("\n" + "=" * 50)
    print("✅ Testes concluídos!")

if __name__ == "__main__":
    main()

