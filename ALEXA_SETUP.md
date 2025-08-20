# 🎤 Configuração da Skill da Alexa

Este guia te ajudará a configurar a skill da Alexa para o AlexaGPT.

## 📋 Pré-requisitos

1. Conta no [Alexa Developer Console](https://developer.amazon.com/alexa)
2. API rodando e acessível via HTTPS
3. Domínio público para sua API

## 🚀 Passo a Passo

### 1. Criar a Skill

1. Acesse o [Alexa Developer Console](https://developer.amazon.com/alexa)
2. Clique em "Create Skill"
3. Escolha "Custom" como modelo
4. Selecione "Provision your own" como método de hospedagem
5. Clique em "Create skill"

### 2. Configurar Informações Básicas

1. **Skill name**: `AlexaGPT`
2. **Default language**: `Portuguese (BR)`
3. **Primary category**: `Knowledge & Trivia`
4. **Secondary category**: `Productivity`

### 3. Configurar Interaction Model

1. Vá para "Interaction Model" → "Intents"
2. Clique em "JSON Editor"
3. Cole o conteúdo do arquivo `alexa-skill/interaction-model.json`
4. Clique em "Save Model"
5. Clique em "Build Model"

### 4. Configurar Endpoint

1. Vá para "Endpoint"
2. Selecione "HTTPS"
3. **Default Region**: Cole a URL da sua API + `/alexa`
   - Exemplo: `https://seu-dominio.com/alexa`
4. Clique em "Save Endpoints"

### 5. Configurar Manifest

1. Vá para "Skill Information"
2. Cole o conteúdo do arquivo `alexa-skill/skill.json` no JSON Editor
3. Clique em "Save"

### 6. Testar a Skill

1. Vá para "Test"
2. Ative o "Skill testing is enabled in development"
3. Teste com comandos como:
   - "Alexa, abra alexagpt"
   - "Alexa, pergunte ao alexagpt qual é a capital do Brasil"

## 🔧 Configurações Importantes

### Invocation Name
- **Nome**: `alexagpt`
- **Exemplo de uso**: "Alexa, abra alexagpt"

### Intents Principais

#### AskQuestion
- **Slots**: `question` (AMAZON.SearchQuery)
- **Exemplos**:
  - "pergunte {question}"
  - "pergunte ao alexagpt {question}"
  - "diga {question}"
  - "fale {question}"

#### Intents do Sistema
- `AMAZON.HelpIntent`
- `AMAZON.StopIntent`
- `AMAZON.CancelIntent`
- `AMAZON.FallbackIntent`

## 🌐 Configuração de HTTPS

A Alexa requer HTTPS. Opções para obter:

### 1. ngrok (Desenvolvimento)
```bash
# Instale ngrok
npm install -g ngrok

# Exponha sua API
ngrok http 5000

# Use a URL HTTPS gerada no endpoint da skill
```

### 2. Serviços de Hosting (Produção)
- **Heroku**: Deploy automático com HTTPS
- **Railway**: Deploy simples com HTTPS
- **Render**: Deploy gratuito com HTTPS
- **Vercel**: Deploy com HTTPS

### 3. VPS com Certificado SSL
- Use Let's Encrypt para certificado gratuito
- Configure nginx como proxy reverso

## 📱 Testando no Dispositivo

1. **Desenvolvimento**:
   - Use o simulador do Developer Console
   - Teste com "Alexa, abra alexagpt"

2. **Produção**:
   - Publique a skill (requer revisão da Amazon)
   - Ative no seu dispositivo Alexa
   - Teste com comandos de voz

## 🚨 Troubleshooting

### Erro: "The skill is not responding"
- Verifique se a API está rodando
- Confirme se o endpoint está correto
- Verifique logs da API

### Erro: "I'm having trouble understanding"
- Verifique o interaction model
- Confirme se os intents estão configurados
- Teste com frases mais simples

### Erro: "The skill is not available"
- Verifique se a skill está publicada
- Confirme se está ativa no dispositivo
- Verifique se o idioma está correto

## 📊 Monitoramento

1. **CloudWatch Logs**: Ative para ver logs da skill
2. **API Logs**: Monitore logs da sua API
3. **Métricas**: Acompanhe uso e erros

## 🔒 Segurança

1. **Validação de Skill ID**: Implemente no código
2. **Rate Limiting**: Configure na API
3. **HTTPS**: Sempre use HTTPS
4. **Logs**: Não logue dados sensíveis

## 📞 Suporte

- [Alexa Developer Documentation](https://developer.amazon.com/docs/alexa)
- [Alexa Skills Kit](https://developer.amazon.com/alexa-skills-kit)
- [Alexa Developer Forums](https://forums.developer.amazon.com/)

---

**Próximo passo**: Configure sua API e teste a integração!

