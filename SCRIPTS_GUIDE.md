# 🚀 Guia dos Scripts Separados - AlexaGPT

## 📋 **Scripts disponíveis:**

### **1. `start_api.py` - Inicia apenas a API (com logs em tempo real)**
### **2. `start_ngrok.py` - Inicia apenas o ngrok**
### **3. `stop_all.py` - Para todos os serviços**
### **4. `monitor_logs.py` - Monitora logs da API**

## 🎯 **Como usar:**

### **Opção 1: Scripts separados (Recomendado)**

#### **Terminal 1 - API:**
```bash
python start_api.py
```

#### **Terminal 2 - ngrok:**
```bash
python start_ngrok.py
```

#### **Para parar tudo:**
```bash
python stop_all.py
```

#### **Para monitorar logs:**
```bash
python monitor_logs.py status
```

### **Opção 2: Script original (tudo junto)**
```bash
python start_dev.py
```

## 🔧 **Comandos do ngrok:**

### **Ver URL atual:**
```bash
python start_ngrok.py url
```

### **Ver status:**
```bash
python start_ngrok.py status
```

### **Parar ngrok:**
```bash
python start_ngrok.py stop
```

### **Ver status da API:**
```bash
python monitor_logs.py status
```

### **Monitorar logs da API:**
```bash
python monitor_logs.py monitor
```

## 📊 **URLs importantes:**

### **API local:**
- **URL:** `http://localhost:5000`
- **Health:** `http://localhost:5000/health`
- **Test:** `http://localhost:5000/test`
- **Alexa:** `http://localhost:5000/alexa`

### **ngrok:**
- **Painel:** `http://localhost:4040`
- **API pública:** `https://[id].ngrok-free.app`
- **Endpoint Alexa:** `https://[id].ngrok-free.app/alexa`

## 🎯 **Ordem de execução:**

### **1. Iniciar API primeiro:**
```bash
python start_api.py
```

### **2. Aguardar API inicializar e depois iniciar ngrok:**
```bash
python start_ngrok.py
```

### **3. Copiar URL do ngrok e configurar no Alexa Developer Console**

## ⚠️ **Dicas importantes:**

### **Se a API não iniciar:**
- Verifique se a porta 5000 está livre
- Execute: `python stop_all.py` e tente novamente
- Verifique se o arquivo `api/app.py` existe

### **Se o ngrok não iniciar:**
- Verifique se a API está rodando na porta 5000
- Execute: `python start_api.py` primeiro
- Verifique se o ngrok está instalado

### **Se der erro de autenticação do ngrok:**
- Configure o token do ngrok: `ngrok config add-authtoken [seu_token]`

## 🔄 **Fluxo completo:**

1. **Terminal 1:** `python start_api.py`
2. **Aguardar:** "✅ API iniciada com sucesso!"
3. **Terminal 2:** `python start_ngrok.py`
4. **Copiar:** URL do ngrok
5. **Configurar:** Alexa Developer Console
6. **Testar:** Na Alexa física

## 🛑 **Para parar:**

### **Parar tudo de uma vez:**
```bash
python stop_all.py
```

### **Parar individualmente:**
- **API:** Ctrl+C no terminal da API
- **ngrok:** `python start_ngrok.py stop`

## 📱 **Teste no Postman:**

### **URLs para testar:**
- **Local:** `http://localhost:5000`
- **ngrok:** `https://[id].ngrok-free.app`

### **Endpoints:**
- `GET /health` - Verificar se está funcionando
- `POST /test` - Testar perguntas
- `POST /alexa` - Simular requisições da Alexa

## 🎉 **Vantagens dos scripts separados:**

✅ **Mais controle** sobre cada serviço
✅ **Debug mais fácil** - pode ver logs separados
✅ **Reiniciar apenas um serviço** quando necessário
✅ **Melhor para desenvolvimento** e testes
✅ **Evita conflitos** entre serviços

## 🚀 **Pronto para usar!**

Agora você tem controle total sobre cada parte do sistema!
