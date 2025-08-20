# 🚀 Usando ngrok para Desenvolvimento

## O que é ngrok?
ngrok cria um túnel HTTPS público para sua API local, permitindo que a Alexa acesse durante desenvolvimento.

## 📦 Instalação

### Windows (PowerShell)
```powershell
# Instalar via Chocolatey
choco install ngrok

# Ou baixar manualmente de https://ngrok.com/
```

### macOS
```bash
# Via Homebrew
brew install ngrok

# Ou baixar manualmente
```

### Linux
```bash
# Baixar e instalar
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
tar xvzf ngrok-v3-stable-linux-amd64.tgz
sudo mv ngrok /usr/local/bin
```

## 🔧 Configuração

1. **Crie conta gratuita** em https://ngrok.com/
2. **Obtenha seu authtoken** no dashboard
3. **Configure o token**:
```bash
ngrok config add-authtoken SEU_TOKEN_AQUI
```

## 🚀 Como usar

### 1. Inicie sua API
```bash
python api/app.py
```

### 2. Em outro terminal, inicie o ngrok
```bash
ngrok http 5000
```

### 3. Copie a URL HTTPS gerada
```
Forwarding    https://abc123.ngrok.io -> http://localhost:5000
```

### 4. Use no Alexa Developer Console
- Endpoint: `https://abc123.ngrok.io/alexa`

## ⚠️ Limitações do ngrok gratuito

- **URL muda** a cada reinicialização
- **Limite de conexões** simultâneas
- **Só para desenvolvimento**

## 🔄 Script automático

Crie um arquivo `start_dev.py`:

```python
import subprocess
import time
import requests
import json

def start_api():
    print("🚀 Iniciando API...")
    # Inicia a API em background
    api_process = subprocess.Popen(["python", "api/app.py"])
    time.sleep(3)  # Aguarda inicializar
    
    return api_process

def start_ngrok():
    print("🌐 Iniciando ngrok...")
    # Inicia ngrok
    ngrok_process = subprocess.Popen(["ngrok", "http", "5000"])
    time.sleep(5)  # Aguarda ngrok inicializar
    
    return ngrok_process

def get_ngrok_url():
    try:
        response = requests.get("http://localhost:4040/api/tunnels")
        tunnels = response.json()["tunnels"]
        for tunnel in tunnels:
            if tunnel["proto"] == "https":
                return tunnel["public_url"]
    except:
        return None

def main():
    print("🔧 Iniciando ambiente de desenvolvimento...")
    
    # Inicia API
    api_process = start_api()
    
    # Inicia ngrok
    ngrok_process = start_ngrok()
    
    # Obtém URL
    url = get_ngrok_url()
    
    if url:
        print(f"✅ URL pública: {url}")
        print(f"🔗 Endpoint da Alexa: {url}/alexa")
        print("\n📋 Configure no Alexa Developer Console:")
        print(f"   Endpoint: {url}/alexa")
        print("\n⏹️  Pressione Ctrl+C para parar")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Parando serviços...")
            api_process.terminate()
            ngrok_process.terminate()
            print("✅ Serviços parados!")
    else:
        print("❌ Erro ao obter URL do ngrok")

if __name__ == "__main__":
    main()
```

## 🎯 Próximos passos

1. **Configure ngrok** seguindo os passos acima
2. **Teste localmente** com `python test_api.py`
3. **Configure a skill** da Alexa com a URL do ngrok
4. **Teste na Alexa** com comandos de voz
5. **Quando funcionar**, faça deploy em um serviço permanente

---

**💡 Dica**: Use ngrok para desenvolvimento e teste, depois migre para um serviço como Railway ou Render para produção.
