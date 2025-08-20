#!/usr/bin/env python3
"""
AlexaGPT - Serviço de IA
"""

import os
import logging
import random
from typing import Optional
from openai import OpenAI

logger = logging.getLogger(__name__)

class AIService:
    """Classe para gerenciar comunicação com a IA"""
    
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.fallback_responses = [
            "Desculpe, não consegui processar sua pergunta no momento. Tente novamente em alguns instantes.",
            "Estou com dificuldades técnicas agora. Pode reformular sua pergunta?",
            "Não consegui acessar as informações agora. Tente perguntar de outra forma.",
            "Estou temporariamente indisponível. Aguarde um momento e tente novamente.",
            "Houve um problema técnico. Pode repetir sua pergunta?",
            "Não consegui processar isso agora. Tente em alguns segundos.",
            "Estou com problemas de conexão. Tente novamente.",
            "Desculpe, não consegui responder agora. Pode tentar mais tarde?",
            "Estou temporariamente offline. Tente novamente em alguns instantes.",
            "Houve um erro técnico. Pode reformular sua pergunta?"
        ]
        
        # Respostas específicas para perguntas comuns
        self.specific_responses = {
            "capital do brasil": "A capital do Brasil é Brasília, inaugurada em 21 de abril de 1960.",
            "capital do brasil": "Brasília é a capital do Brasil desde 1960.",
            "distancia terra sol": "A distância média da Terra ao Sol é de aproximadamente 149,6 milhões de quilômetros (1 unidade astronômica). Esta medida foi calculada usando técnicas como radar, paralaxe e observações de trânsitos planetários.",
            "distância terra sol": "A distância média da Terra ao Sol é de cerca de 149,6 milhões de quilômetros. Esta medida foi determinada através de métodos astronômicos como radar e paralaxe.",
            "distancia da terra ao sol": "A distância média da Terra ao Sol é de aproximadamente 149,6 milhões de quilômetros. Esta medida foi calculada usando técnicas como radar, paralaxe e observações astronômicas.",
            "distância da terra ao sol": "A distância média da Terra ao Sol é de cerca de 149,6 milhões de quilômetros. Esta medida foi determinada através de métodos astronômicos como radar e paralaxe.",
            "como fazer bolo": "Para fazer um bolo básico, você precisa de farinha, ovos, açúcar, leite e fermento. Misture os ingredientes secos, adicione os líquidos, bata bem e asse em forno pré-aquecido a 180°C por cerca de 30-40 minutos.",
            "receita de bolo": "Para um bolo simples: 2 xícaras de farinha, 2 ovos, 1 xícara de açúcar, 1 xícara de leite, 1 colher de fermento. Misture tudo e asse por 30-40 minutos a 180°C.",
            "quem criou a alexa": "A Alexa foi criada pela Amazon e foi apresentada pela primeira vez em 2014 junto com o Echo, o primeiro dispositivo Echo.",
            "quem inventou a alexa": "A Alexa foi desenvolvida pela Amazon e foi lançada em 2014 como assistente virtual para o dispositivo Echo.",
            "que horas são": "Desculpe, não tenho acesso ao horário atual. Você pode perguntar à Alexa diretamente sobre o horário.",
            "que dia é hoje": "Não tenho acesso à data atual. Você pode perguntar à Alexa sobre a data de hoje."
        }
    
    def get_response(self, question: str) -> str:
        """Obtém resposta da IA, com fallback se necessário"""
        try:
            # Primeiro tenta respostas específicas
            response = self._get_specific_response(question)
            if response:
                return response
            
            # Se não encontrar resposta específica, tenta OpenAI
            response = self._get_openai_response(question)
            if response:
                return response
            
            # Se não encontrar, usa fallback genérico
            return self._get_fallback_response()
            
        except Exception as e:
            logger.error(f"Erro ao obter resposta: {str(e)}")
            return self._get_error_response()
    
    def _get_openai_response(self, question: str) -> Optional[str]:
        """Obtém resposta da OpenAI"""
        try:
            logger.info(f"Processando pergunta: {question}")
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente útil e amigável. Responda de forma clara e concisa em português brasileiro."},
                    {"role": "user", "content": question}
                ],
                max_tokens=150,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            error_message = str(e)
            logger.error(f"Erro na API OpenAI: {error_message}")
            
            # Tratamento específico de erros
            if "insufficient_quota" in error_message or "quota" in error_message:
                return "Desculpe, minha conta de IA está sem crédito no momento. Estou usando respostas básicas até resolver isso. Pode tentar perguntas simples como 'qual é a capital do Brasil?'"
            
            elif "429" in error_message or "Too Many Requests" in error_message:
                return "Estou recebendo muitas perguntas agora. Aguarde alguns minutos e tente novamente, ou faça uma pergunta mais simples."
            
            elif "503" in error_message or "Service Unavailable" in error_message:
                return "O serviço de IA está temporariamente indisponível. Estou usando respostas básicas por enquanto."
            
            elif "timeout" in error_message or "connection" in error_message:
                return "Tive problemas de conexão com o serviço de IA. Tente novamente em alguns segundos."
            
            elif "authentication" in error_message or "unauthorized" in error_message:
                return "Problema de autenticação com o serviço de IA. Vou usar respostas básicas por enquanto."
            
            else:
                return None
    
    def _get_specific_response(self, question: str) -> Optional[str]:
        """Obtém resposta específica para perguntas conhecidas"""
        question_lower = question.lower()
        
        for key, response in self.specific_responses.items():
            if key in question_lower:
                logger.info(f"Usando resposta específica para: {key}")
                return response
        
        return None
    
    def _get_fallback_response(self) -> str:
        """Obtém resposta de fallback aleatória"""
        response = random.choice(self.fallback_responses)
        logger.info("Usando resposta de fallback")
        return response
    
    def _get_error_response(self) -> str:
        """Obtém resposta de erro"""
        return "Desculpe, tive um problema técnico. Tente novamente em alguns instantes."
    
    def test_connection(self) -> bool:
        """Testa conexão com OpenAI"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "Teste"}],
                max_tokens=5
            )
            return True
        except Exception as e:
            logger.error(f"Erro no teste de conexão: {str(e)}")
            return False
    
    def update_settings(self, **kwargs):
        """Atualiza configurações do serviço"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
                logger.info(f"Configuração atualizada: {key} = {value}")
