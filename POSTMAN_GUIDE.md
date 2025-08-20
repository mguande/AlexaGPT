# 🚀 Guia do Postman - AlexaGPT API

## 📋 **Como importar a coleção:**

### **1. Abra o Postman**
- Baixe e instale o [Postman](https://www.postman.com/downloads/)

### **2. Importe a coleção:**
- Clique em **"Import"**
- Arraste o arquivo `AlexaGPT_Postman_Collection.json`
- Ou clique em **"Upload Files"** e selecione o arquivo

### **3. Importe o ambiente:**
- Clique em **"Import"** novamente
- Arraste o arquivo `AlexaGPT_Postman_Environment.json`
- Ou clique em **"Upload Files"** e selecione o arquivo

### **4. Ative o ambiente:**
- No canto superior direito, clique no seletor de ambiente
- Selecione **"AlexaGPT Environment"**

## 🧪 **Testes disponíveis:**

### **1. Health Check**
- **Método:** GET
- **URL:** `{{base_url}}/health`
- **Descrição:** Verifica se a API está funcionando
- **Resposta esperada:** Status 200 com informações da API

### **2. Test Endpoint**
- **Método:** POST
- **URL:** `{{base_url}}/test`
- **Body:** `{"question": "qual é a capital do Brasil?"}`
- **Descrição:** Testa o endpoint de perguntas
- **Resposta esperada:** Resposta da IA

### **3. Alexa - LaunchRequest**
- **Método:** POST
- **URL:** `{{base_url}}/alexa`
- **Body:** JSON completo da requisição Alexa
- **Descrição:** Simula "Alexa, abra alexagpt"
- **Resposta esperada:** Mensagem de boas-vindas

### **4. Alexa - AskQuestion Intent**
- **Método:** POST
- **URL:** `{{base_url}}/alexa`
- **Body:** JSON com intent AskQuestion
- **Descrição:** Simula uma pergunta do usuário
- **Resposta esperada:** Resposta da IA

### **5. Alexa - HelpIntent**
- **Método:** POST
- **URL:** `{{base_url}}/alexa`
- **Body:** JSON com intent HelpIntent
- **Descrição:** Simula pedido de ajuda
- **Resposta esperada:** Instruções de uso

### **6. Alexa - StopIntent**
- **Método:** POST
- **URL:** `{{base_url}}/alexa`
- **Body:** JSON com intent StopIntent
- **Descrição:** Simula comando de parada
- **Resposta esperada:** Mensagem de despedida

### **7. Test - Distância Terra-Sol**
- **Método:** POST
- **URL:** `{{base_url}}/test`
- **Body:** `{"question": "qual é a distancia da terra ao sol"}`
- **Descrição:** Testa resposta específica
- **Resposta esperada:** Informações sobre distância Terra-Sol

### **8. Test - Receita de Bolo**
- **Método:** POST
- **URL:** `{{base_url}}/test`
- **Body:** `{"question": "como fazer bolo"}`
- **Descrição:** Testa resposta sobre receita
- **Resposta esperada:** Instruções para fazer bolo

### **9. Test - Quem criou a Alexa**
- **Método:** POST
- **URL:** `{{base_url}}/test`
- **Body:** `{"question": "quem criou a alexa"}`
- **Descrição:** Testa resposta sobre Alexa
- **Resposta esperada:** Informações sobre criação da Alexa

### **10. Test - Pergunta Genérica**
- **Método:** POST
- **URL:** `{{base_url}}/test`
- **Body:** `{"question": "qual é a história do Brasil"}`
- **Descrição:** Testa pergunta que pode usar OpenAI
- **Resposta esperada:** Resposta da IA ou fallback

## 🔧 **Como atualizar a URL:**

### **Quando a URL do ngrok mudar:**

1. **Atualize a variável `base_url`:**
   - Clique no ícone de engrenagem (⚙️) no canto superior direito
   - Selecione **"AlexaGPT Environment"**
   - Atualize o valor de `base_url` para a nova URL
   - Clique em **"Save"**

2. **Ou atualize diretamente na coleção:**
   - Clique com botão direito na coleção
   - Selecione **"Edit"**
   - Vá na aba **"Variables"**
   - Atualize o valor de `base_url`
   - Clique em **"Save"**

## 🎯 **Ordem recomendada de testes:**

1. **Health Check** - Verificar se a API está funcionando
2. **Test Endpoint** - Testar pergunta básica
3. **Alexa - LaunchRequest** - Testar abertura da skill
4. **Alexa - AskQuestion Intent** - Testar pergunta via Alexa
5. **Test - Distância Terra-Sol** - Testar resposta específica
6. **Test - Receita de Bolo** - Testar outra resposta específica
7. **Alexa - HelpIntent** - Testar ajuda
8. **Alexa - StopIntent** - Testar parada
9. **Test - Pergunta Genérica** - Testar OpenAI/fallback

## 📊 **Respostas esperadas:**

### **Health Check:**
```json
{
  "status": "healthy",
  "service": "AlexaGPT API",
  "version": "1.0.0"
}
```

### **Test Endpoint:**
```json
{
  "question": "qual é a capital do Brasil?",
  "response": "Brasília é a capital do Brasil desde 1960.",
  "status": "success"
}
```

### **Alexa Endpoint:**
```json
{
  "version": "1.0",
  "response": {
    "outputSpeech": {
      "type": "PlainText",
      "text": "Resposta da IA..."
    },
    "shouldEndSession": true
  }
}
```

## ⚠️ **Dicas importantes:**

1. **Sempre teste o Health Check primeiro**
2. **Verifique se a URL está atualizada**
3. **Use o ambiente correto**
4. **Monitore os logs da API**
5. **Teste todos os cenários antes de usar na Alexa**

## 🔄 **Atualização automática:**

Para facilitar a atualização da URL, você pode:

1. **Usar o script Python:**
   ```bash
   python -c "import requests; r = requests.get('http://localhost:4040/api/tunnels'); data = r.json(); print('Nova URL:', data['tunnels'][0]['public_url'])"
   ```

2. **Copiar a URL e atualizar no Postman**

## 🎉 **Pronto para testar!**

Agora você tem uma coleção completa do Postman para testar toda a API AlexaGPT!
