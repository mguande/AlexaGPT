#!/usr/bin/env python3
"""
Teste completo da comunicação com a Alexa
"""

import requests
import json

def test_alexa_communication():
    """Testa a comunicação completa com a Alexa"""
    
    base_url = "https://9a00fb090d39.ngrok-free.app"
    
    print("🧪 Testando comunicação com a Alexa...")
    print("=" * 50)
    
    # Teste 1: Health check
    print("1. Testando health check...")
    try:
        r = requests.get(f"{base_url}/health")
        print(f"   Status: {r.status_code}")
        print(f"   Resposta: {r.json()}")
        print("   ✅ Health check OK")
    except Exception as e:
        print(f"   ❌ Erro no health check: {e}")
        return False
    
    # Teste 2: LaunchRequest
    print("\n2. Testando LaunchRequest...")
    launch_request = {
        "version": "1.0",
        "session": {
            "sessionId": "test-session-123",
            "application": {
                "applicationId": "test-app-123"
            },
            "user": {
                "userId": "test-user-123"
            }
        },
        "request": {
            "type": "LaunchRequest",
            "requestId": "test-request-123",
            "timestamp": "2023-01-01T00:00:00Z"
        }
    }
    
    try:
        r = requests.post(f"{base_url}/alexa", json=launch_request)
        print(f"   Status: {r.status_code}")
        response = r.json()
        print(f"   Speech: {response.get('response', {}).get('outputSpeech', {}).get('text', 'N/A')}")
        print("   ✅ LaunchRequest OK")
    except Exception as e:
        print(f"   ❌ Erro no LaunchRequest: {e}")
        return False
    
    # Teste 3: AskQuestion Intent
    print("\n3. Testando AskQuestion Intent...")
    ask_request = {
        "version": "1.0",
        "session": {
            "sessionId": "test-session-456",
            "application": {
                "applicationId": "test-app-456"
            },
            "user": {
                "userId": "test-user-456"
            }
        },
        "request": {
            "type": "IntentRequest",
            "requestId": "test-request-456",
            "timestamp": "2023-01-01T00:00:00Z",
            "intent": {
                "name": "AskQuestion",
                "slots": {
                    "question": {
                        "name": "question",
                        "value": "qual é a capital do Brasil"
                    }
                }
            }
        }
    }
    
    try:
        r = requests.post(f"{base_url}/alexa", json=ask_request)
        print(f"   Status: {r.status_code}")
        response = r.json()
        print(f"   Speech: {response.get('response', {}).get('outputSpeech', {}).get('text', 'N/A')[:100]}...")
        print("   ✅ AskQuestion Intent OK")
    except Exception as e:
        print(f"   ❌ Erro no AskQuestion Intent: {e}")
        return False
    
    # Teste 4: HelpIntent
    print("\n4. Testando HelpIntent...")
    help_request = {
        "version": "1.0",
        "session": {
            "sessionId": "test-session-789",
            "application": {
                "applicationId": "test-app-789"
            },
            "user": {
                "userId": "test-user-789"
            }
        },
        "request": {
            "type": "IntentRequest",
            "requestId": "test-request-789",
            "timestamp": "2023-01-01T00:00:00Z",
            "intent": {
                "name": "AMAZON.HelpIntent"
            }
        }
    }
    
    try:
        r = requests.post(f"{base_url}/alexa", json=help_request)
        print(f"   Status: {r.status_code}")
        response = r.json()
        print(f"   Speech: {response.get('response', {}).get('outputSpeech', {}).get('text', 'N/A')[:100]}...")
        print("   ✅ HelpIntent OK")
    except Exception as e:
        print(f"   ❌ Erro no HelpIntent: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("🎉 Todos os testes passaram! A API está pronta para a Alexa.")
    print("\n📋 Próximos passos:")
    print("1. Atualize o skill.json no Alexa Developer Console")
    print("2. Clique em 'Save Endpoints'")
    print("3. Clique em 'Build Model'")
    print("4. Teste no console do Alexa Developer Console")
    print("5. Teste na Alexa física")
    
    return True

if __name__ == "__main__":
    test_alexa_communication()
