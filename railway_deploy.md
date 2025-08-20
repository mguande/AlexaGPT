# 🚂 Deploy no Railway

Railway é uma das formas mais simples de fazer deploy da sua API AlexaGPT.

## 📋 Pré-requisitos

1. Conta no GitHub
2. Conta no Railway (https://railway.app/)
3. Projeto AlexaGPT configurado

## 🚀 Deploy Automático

### 1. Prepare o projeto

Adicione um arquivo `Procfile` na raiz do projeto:

```bash
# Procfile
web: gunicorn api.app:app --config gunicorn.conf.py
```

### 2. Configure o Railway

1. **Acesse** https://railway.app/
2. **Faça login** com sua conta GitHub
3. **Clique** em "New Project"
4. **Selecione** "Deploy from GitHub repo"
5. **Escolha** seu repositório AlexaGPT
6. **Clique** em "Deploy Now"

### 3. Configure as variáveis de ambiente

No dashboard do Railway:

1. Vá para a aba **Variables**
2. Adicione as seguintes variáveis:

```
OPENAI_API_KEY=sua_chave_openai_aqui
ALEXA_SKILL_ID=amzn1.ask.skill.seu_skill_id_aqui
SECRET_KEY=sua_chave_secreta_aqui
PORT=5000
DEBUG=False
```

### 4. Obtenha a URL

1. Vá para a aba **Settings**
2. Copie a **Domain** gerada
3. Sua URL será: `https://seu-projeto.railway.app`

### 5. Configure a Alexa

No Alexa Developer Console:

1. **Endpoint**: `https://seu-projeto.railway.app/alexa`
2. **Teste** a skill

## 🔄 Deploy Automático

A cada push para o GitHub, o Railway fará deploy automático.

## 📊 Monitoramento

- **Logs**: Veja logs em tempo real
- **Métricas**: Acompanhe uso de CPU/memória
- **Domínio**: URL personalizada disponível

## 💰 Custos

- **Gratuito**: 500 horas/mês
- **Pago**: $5/mês para uso ilimitado

## 🚨 Troubleshooting

### Erro: "Application Error"
- Verifique os logs no Railway
- Confirme se as variáveis de ambiente estão corretas
- Teste localmente primeiro

### Erro: "Build Failed"
- Verifique se o `Procfile` está correto
- Confirme se todas as dependências estão no `requirements.txt`

### Erro: "Timeout"
- A Alexa tem timeout de 8 segundos
- Otimize sua API para responder rapidamente

## 🎯 Próximos passos

1. **Teste localmente** com ngrok
2. **Faça deploy** no Railway
3. **Configure** a skill da Alexa
4. **Teste** com comandos de voz
5. **Monitore** os logs

---

**✅ Vantagens do Railway:**
- Deploy automático
- HTTPS gratuito
- Domínio personalizado
- Logs em tempo real
- Escalabilidade automática
