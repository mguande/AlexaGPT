# 🚀 AlexaGPT - Integração Alexa + IA

Um projeto Python que integra a Amazon Alexa com inteligência artificial, permitindo que sua Alexa responda perguntas usando IA avançada.

## ✨ Funcionalidades

- 🤖 **Integração com OpenAI**: Respostas inteligentes usando GPT
- 🎤 **Compatível com Alexa**: Funciona com Alexa física e simulador
- 🔄 **Fallback Inteligente**: Respostas específicas para perguntas comuns
- 🛡️ **Tratamento de Erros**: Mensagens específicas para diferentes tipos de erro
- 📊 **Logs Detalhados**: Monitoramento completo de todas as requisições
- 🌐 **HTTPS via ngrok**: Túnel seguro para desenvolvimento local

## 📁 Estrutura do Projeto

```
AlexaGPT/
├── api/
│   ├── __init__.py
│   ├── app.py              # Servidor Flask principal
│   ├── alexa_handler.py    # Processamento de requisições Alexa
│   └── ai_service.py       # Integração com IA
├── alexa-skill/
│   ├── interaction-model.json  # Modelo de interação da Alexa
│   └── skill.json             # Configuração da skill
├── scripts/
│   ├── start_api_windows.py   # Inicia apenas a API (Windows)
│   ├── start_ngrok.py         # Inicia apenas o ngrok
│   ├── stop_all.py            # Para todos os serviços
│   └── monitor_logs.py        # Monitora logs
├── requirements.txt
├── .env.example
└── README.md
```

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/mguande/AlexaGPT.git
cd AlexaGPT
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente
```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações:
```env
# OpenAI API Key (obrigatório)
OPENAI_API_KEY=sua_chave_openai_aqui

# Alexa Skill ID (opcional, para validação)
ALEXA_SKILL_ID=amzn1.ask.skill.seu_skill_id

# Configurações do servidor
PORT=5000
DEBUG=False

# Chave secreta para Flask (gerada automaticamente)
SECRET_KEY=sua_chave_secreta_aqui
```

### 4. Configure o ngrok
1. Baixe o ngrok: https://ngrok.com/download
2. Configure seu token: `ngrok config add-authtoken SEU_TOKEN`
3. Adicione o ngrok ao PATH do sistema

## 🎯 Como Usar

### Opção 1: Scripts Separados (Recomendado)

#### Terminal 1 - API:
```bash
python start_api_windows.py
```

#### Terminal 2 - ngrok:
```bash
python start_ngrok.py
```

#### Para parar tudo:
```bash
python stop_all.py
```

### Opção 2: Script Original
```bash
python start_dev.py
```

## 📱 Configuração da Alexa

### 1. Acesse o Alexa Developer Console
- Vá para: https://developer.amazon.com/alexa/console/ask
- Faça login com sua conta Amazon

### 2. Crie uma nova Skill
- Clique em "Create Skill"
- Escolha "Custom" e "Provision your own"
- Nome: "AlexaGPT"
- Idioma: Português (Brasil)

### 3. Configure o Modelo de Interação
- Vá em "Interaction Model" > "JSON Editor"
- Cole o conteúdo do arquivo `alexa-skill/interaction-model.json`
- Clique em "Save Model"

### 4. Configure o Endpoint
- Vá em "Endpoint"
- Em "Default Region", cole a URL do ngrok:
  ```
  https://[seu-id].ngrok-free.app/alexa
  ```
- Clique em "Save Endpoints"

### 5. Configure o Manifest
- Vá em "Skill Manifest" > "JSON Editor"
- Cole o conteúdo do arquivo `alexa-skill/skill.json`
- Clique em "Save"

### 6. Teste a Skill
- Vá em "Test"
- Ative "Test is enabled for this account"
- Teste: "Alexa, abra alexagpt"

## 🎤 Comandos da Alexa

- **"Alexa, abra alexagpt"** - Abre a skill
- **"Alexa, pergunte ao alexagpt: qual é a capital do Brasil?"** - Faz uma pergunta
- **"Alexa, pergunte ao alexagpt: como fazer bolo?"** - Outra pergunta
- **"Alexa, pergunte ao alexagpt: qual é a distância da terra ao sol?"** - Pergunta específica

## 🔧 Scripts Disponíveis

### `start_api_windows.py`
Inicia apenas a API com logs em tempo real
```bash
python start_api_windows.py
```

### `start_ngrok.py`
Inicia apenas o túnel ngrok
```bash
python start_ngrok.py
```

### Comandos do ngrok:
```bash
python start_ngrok.py url      # Ver URL atual
python start_ngrok.py status   # Ver status
python start_ngrok.py stop     # Parar ngrok
```

### `stop_all.py`
Para todos os serviços
```bash
python stop_all.py
```

### `monitor_logs.py`
Monitora logs da API
```bash
python monitor_logs.py status  # Ver status
python monitor_logs.py monitor # Monitorar logs
```

## 📊 URLs Importantes

### API Local:
- **URL:** `http://localhost:5000`
- **Health:** `http://localhost:5000/health`
- **Test:** `http://localhost:5000/test`
- **Alexa:** `http://localhost:5000/alexa`

### ngrok:
- **Painel:** `http://localhost:4040`
- **API pública:** `https://[id].ngrok-free.app`
- **Endpoint Alexa:** `https://[id].ngrok-free.app/alexa`

## 🧪 Testando a API

### Health Check:
```bash
curl http://localhost:5000/health
```

### Teste de Pergunta:
```bash
curl -X POST http://localhost:5000/test \
  -H "Content-Type: application/json" \
  -d '{"question": "qual é a capital do Brasil?"}'
```

### Teste da Alexa:
```bash
curl -X POST http://localhost:5000/alexa \
  -H "Content-Type: application/json" \
  -d '{
    "version": "1.0",
    "session": {
      "sessionId": "test",
      "application": {"applicationId": "test"},
      "user": {"userId": "test"}
    },
    "request": {
      "type": "LaunchRequest",
      "requestId": "test",
      "timestamp": "2023-01-01T00:00:00Z"
    }
  }'
```

## 🔑 Variáveis de Ambiente

### Obrigatórias:
- `OPENAI_API_KEY`: Sua chave da API OpenAI

### Opcionais:
- `ALEXA_SKILL_ID`: ID da skill Alexa (para validação)
- `PORT`: Porta do servidor (padrão: 5000)
- `DEBUG`: Modo debug (padrão: False)
- `SECRET_KEY`: Chave secreta do Flask (gerada automaticamente)

## 🛠️ Troubleshooting

### API não inicia:
- Verifique se a porta 5000 está livre
- Execute: `python stop_all.py` e tente novamente
- Verifique se o arquivo `api/app.py` existe

### ngrok não inicia:
- Verifique se a API está rodando na porta 5000
- Execute: `python start_api_windows.py` primeiro
- Verifique se o ngrok está instalado e configurado

### Erro de autenticação do ngrok:
- Configure o token: `ngrok config add-authtoken [seu_token]`

### Alexa não responde:
- Verifique se a URL do ngrok está atualizada no Developer Console
- Teste o endpoint manualmente com curl
- Verifique os logs da API

## 📝 Logs

A API gera logs detalhados incluindo:
- IP do cliente
- Headers da requisição
- Perguntas e respostas
- Erros e exceções
- Timestamps

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🙏 Agradecimentos

- Amazon Alexa Developer Console
- OpenAI API
- Flask Framework
- ngrok para túnel HTTPS
