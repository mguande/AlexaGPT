#!/usr/bin/env python3
"""
AlexaGPT API - Servidor Flask para integração Alexa + IA
"""

import os
import json
import logging
import traceback
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from alexa_handler import AlexaHandler
from ai_service import AIService

# Carrega variáveis de ambiente
load_dotenv()

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Configurações
ALEXA_SKILL_ID = os.getenv('ALEXA_SKILL_ID')
SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
app.config['SECRET_KEY'] = SECRET_KEY

# Inicializa serviços
alexa_handler = AlexaHandler()
ai_service = AIService()

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint de verificação de saúde da API"""
    logger.info("🏥 Health check solicitado")
    logger.info(f"📊 IP: {request.remote_addr}")
    return jsonify({
        'status': 'healthy',
        'service': 'AlexaGPT API',
        'version': '1.0.0'
    })

@app.route('/alexa', methods=['POST'])
def alexa_endpoint():
    """Endpoint principal para requisições da Alexa"""
    try:
        # Log da requisição
        logger.info("🌐 Recebida requisição da Alexa")
        logger.info(f"📊 IP: {request.remote_addr}")
        logger.info(f"📋 Headers: {dict(request.headers)}")
        
        # Verifica se é uma requisição válida da Alexa
        if not alexa_handler.is_valid_request(request):
            error_msg = "Erro: Requisição inválida da Alexa"
            logger.warning(error_msg)
            return alexa_handler.create_response(error_msg)
        
        # Processa a requisição da Alexa
        alexa_request = alexa_handler.parse_request(request)
        
        if not alexa_request:
            error_msg = "Erro: Falha ao processar requisição da Alexa"
            logger.warning(error_msg)
            return alexa_handler.create_response(error_msg)
        
        # Extrai a pergunta do usuário
        user_question = alexa_handler.extract_question(alexa_request)
        
        logger.info(f"Pergunta extraída: {user_question}")
        
        # Trata casos especiais
        if user_question == "welcome":
            return alexa_handler.create_welcome_response()
        elif user_question == "help":
            return alexa_handler.create_help_response()
        elif user_question == "stop":
            return alexa_handler.create_stop_response()
        elif not user_question:
            error_msg = "Erro: Nenhuma pergunta encontrada na requisição"
            logger.warning(error_msg)
            return alexa_handler.create_response(error_msg)
        
        logger.info(f"Pergunta do usuário: {user_question}")
        
        # Obtém resposta da IA
        ai_response = ai_service.get_response(user_question)
        
        if not ai_response:
            error_msg = "Erro: Falha ao obter resposta da IA"
            logger.error(error_msg)
            return alexa_handler.create_response(error_msg)
        
        logger.info(f"Resposta da IA: {ai_response}")
        
        # Cria resposta para a Alexa
        alexa_response = alexa_handler.create_response(ai_response)
        
        return alexa_response
        
    except Exception as e:
        error_msg = f"Erro interno: {str(e)}"
        logger.error(f"Erro no endpoint da Alexa: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        return alexa_handler.create_response(error_msg)

@app.route('/test', methods=['POST'])
def test_endpoint():
    """Endpoint para testes da API"""
    try:
        data = request.get_json()
        question = data.get('question', 'Olá, como você está?')
        
        logger.info("🧪 Recebida requisição de teste")
        logger.info(f"📊 IP: {request.remote_addr}")
        logger.info(f"❓ Pergunta: {question}")
        
        # Obtém resposta da IA
        ai_response = ai_service.get_response(question)
        
        return jsonify({
            'question': question,
            'response': ai_response,
            'status': 'success'
        })
        
    except Exception as e:
        error_msg = f"Erro no teste: {str(e)}"
        logger.error(f"Erro no endpoint de teste: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        return jsonify({
            'question': question if 'question' in locals() else 'N/A',
            'response': error_msg,
            'status': 'error',
            'error': str(e)
        })

@app.errorhandler(404)
def not_found(error):
    """Handler para rotas não encontradas"""
    error_msg = f"Erro 404: Endpoint não encontrado - {request.url}"
    logger.error(error_msg)
    return jsonify({'error': error_msg}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handler para erros internos"""
    error_msg = f"Erro 500: Erro interno do servidor - {str(error)}"
    logger.error(error_msg)
    logger.error(f"Traceback: {traceback.format_exc()}")
    return jsonify({'error': error_msg}), 500

@app.errorhandler(Exception)
def handle_exception(e):
    """Handler genérico para todas as exceções"""
    error_msg = f"Erro não tratado: {str(e)}"
    logger.error(error_msg)
    logger.error(f"Traceback: {traceback.format_exc()}")
    return jsonify({'error': error_msg}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    
    logger.info(f"Iniciando AlexaGPT API na porta {port}")
    logger.info(f"Modo debug: {debug}")
    
    # Desabilita logs do Werkzeug em modo debug
    if debug:
        import logging
        werkzeug_logger = logging.getLogger('werkzeug')
        werkzeug_logger.setLevel(logging.ERROR)
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug,
        use_reloader=False  # Evita duplicação de processos
    )
