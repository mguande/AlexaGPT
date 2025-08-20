# Configuração do Gunicorn para AlexaGPT
import os
import multiprocessing

# Configurações básicas
bind = f"0.0.0.0:{os.getenv('PORT', '5000')}"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

# Configurações de logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Configurações de segurança
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# Configurações de performance
max_requests = 1000
max_requests_jitter = 50
preload_app = True

# Configurações específicas para Alexa
# A Alexa tem timeout de 8 segundos, então configuramos para ser mais rápido
worker_timeout = 25
graceful_timeout = 30

