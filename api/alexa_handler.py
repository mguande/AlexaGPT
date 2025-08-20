#!/usr/bin/env python3
"""
AlexaGPT - Handler para requisições da Alexa
"""

import json
import logging
from flask import jsonify
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class AlexaHandler:
    """Classe para processar requisições e respostas da Alexa"""
    
    def __init__(self):
        self.supported_intents = [
            'AskQuestion',
            'AMAZON.HelpIntent',
            'AMAZON.StopIntent',
            'AMAZON.CancelIntent',
            'AMAZON.FallbackIntent',
            'AMAZON.NavigateHomeIntent'
        ]
    
    def is_valid_request(self, request) -> bool:
        """Verifica se a requisição é válida da Alexa"""
        try:
            # Verifica se tem o header correto
            if 'application/json' not in request.content_type:
                logger.warning(f"Content-Type inválido: {request.content_type}")
                return False
            
            # Verifica se tem o body
            if not request.data:
                logger.warning("Request sem dados")
                return False
            
            # Tenta fazer parse do JSON
            data = request.get_json()
            if not data:
                logger.warning("Falha ao fazer parse do JSON")
                return False
            
            # Verifica se tem os campos obrigatórios
            required_fields = ['version', 'session', 'request']
            for field in required_fields:
                if field not in data:
                    logger.warning(f"Campo obrigatório ausente: {field}")
                    return False
            
            return True
            
        except Exception as e:
            logger.error(f"Erro ao validar requisição: {str(e)}")
            return False
    
    def parse_request(self, request) -> Optional[Dict[str, Any]]:
        """Faz parse da requisição da Alexa"""
        try:
            data = request.get_json()
            logger.info(f"Requisição da Alexa: {json.dumps(data, indent=2)}")
            return data
        except Exception as e:
            logger.error(f"Erro ao fazer parse da requisição: {str(e)}")
            return None
    
    def extract_question(self, alexa_request: Dict[str, Any]) -> Optional[str]:
        """Extrai a pergunta do usuário da requisição da Alexa"""
        try:
            request_data = alexa_request.get('request', {})
            request_type = request_data.get('type')
            intent = request_data.get('intent', {})
            intent_name = intent.get('name')
            
            logger.info(f"Tipo de requisição: {request_type}")
            logger.info(f"Intent detectado: {intent_name}")
            
            # Se for um LaunchRequest, retorna mensagem de boas-vindas
            if request_type == 'LaunchRequest':
                return "welcome"
            
            # Se for uma pergunta direta
            if intent_name == 'AskQuestion':
                slots = intent.get('slots', {})
                question_slot = slots.get('question', {})
                question = question_slot.get('value', '')
                
                if question:
                    return question
            
            # Se for um fallback, pega o que foi dito
            elif intent_name == 'AMAZON.FallbackIntent':
                # Tenta extrair da query original
                query = request_data.get('query', '')
                if query:
                    # Remove palavras de ativação comuns
                    query = self._clean_query(query)
                    return query
            
            # Se for um comando direto
            elif intent_name in ['IntentRequest']:
                query = request_data.get('query', '')
                if query:
                    query = self._clean_query(query)
                    return query
            
            # Se for HelpIntent
            elif intent_name == 'AMAZON.HelpIntent':
                return "help"
            
            # Se for StopIntent ou CancelIntent
            elif intent_name in ['AMAZON.StopIntent', 'AMAZON.CancelIntent']:
                return "stop"
            
            # Se for NavigateHomeIntent
            elif intent_name == 'AMAZON.NavigateHomeIntent':
                return "stop"
            
            return None
            
        except Exception as e:
            logger.error(f"Erro ao extrair pergunta: {str(e)}")
            return None
    
    def _clean_query(self, query: str) -> str:
        """Limpa a query removendo palavras de ativação"""
        # Remove palavras de ativação comuns
        activation_words = [
            'alexa', 'pergunte ao alexagpt', 'pergunte para o alexagpt',
            'alexagpt', 'pergunte', 'diga', 'fale'
        ]
        
        query_lower = query.lower()
        for word in activation_words:
            query_lower = query_lower.replace(word.lower(), '').strip()
        
        return query_lower if query_lower else query
    
    def create_response(self, speech_text: str, should_end_session: bool = True) -> jsonify:
        """Cria uma resposta para a Alexa"""
        try:
            # Limita o tamanho da resposta para a Alexa
            if len(speech_text) > 8000:
                speech_text = speech_text[:8000] + "..."
            
            response = {
                "version": "1.0",
                "sessionAttributes": {},
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": speech_text
                    },
                    "shouldEndSession": should_end_session
                }
            }
            
            # Adiciona card se a resposta for longa ou se for um erro
            if len(speech_text) > 100 or speech_text.startswith("Erro:"):
                response["response"]["card"] = {
                    "type": "Simple",
                    "title": "AlexaGPT",
                    "content": speech_text[:500] + "..." if len(speech_text) > 500 else speech_text
                }
            
            logger.info(f"Resposta para Alexa: {speech_text[:100]}...")
            return jsonify(response)
            
        except Exception as e:
            logger.error(f"Erro ao criar resposta: {str(e)}")
            return jsonify({
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": f"Erro ao criar resposta: {str(e)}"
                    },
                    "shouldEndSession": True
                }
            })
    
    def create_help_response(self) -> jsonify:
        """Cria resposta de ajuda"""
        help_text = """
        Olá! Eu sou o AlexaGPT, seu assistente de IA. 
        Você pode me fazer perguntas sobre qualquer assunto.
        Por exemplo: "Qual é a capital do Brasil?" ou "Como fazer um bolo?"
        """
        return self.create_response(help_text, should_end_session=False)
    
    def create_welcome_response(self) -> jsonify:
        """Cria resposta de boas-vindas"""
        welcome_text = """
        Olá! Eu sou o AlexaGPT, seu assistente de IA inteligente.
        Pode me fazer qualquer pergunta que eu vou te ajudar!
        """
        return self.create_response(welcome_text, should_end_session=False)
    
    def create_stop_response(self) -> jsonify:
        """Cria resposta de parada"""
        return self.create_response("Até logo! Tenha um ótimo dia.", should_end_session=True)
    
    def create_error_response(self, error_message: str = "Desculpe, tive um problema técnico.") -> jsonify:
        """Cria resposta de erro"""
        return self.create_response(f"Erro: {error_message}", should_end_session=True)
