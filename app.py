<<<<<<< Updated upstream
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv
import logging

# Carrega a chave do arquivo .env
load_dotenv()
CHAVE_GROQ = os.getenv("GROQ_API_KEY")

app = Flask(__name__)
CORS(app) # Isso permite que seu site fale com o servidor Python

# Configura logging
logging.basicConfig(level=logging.INFO)

@app.route('/gerar', methods=['POST'])
def gerar():
    dados_recebidos = request.get_json(silent=True)
    prompt_usuario = dados_recebidos.get('prompt') if dados_recebidos else None

    if not CHAVE_GROQ:
        app.logger.error("Chave da API não encontrada no .env")
        return jsonify({"erro": "Chave da API não encontrada. Verifique o arquivo .env."}), 500

    if not prompt_usuario:
        app.logger.warning("Prompt inválido ou ausente na requisição")
        return jsonify({"erro": "Prompt inválido ou ausente. Envie JSON com 'prompt'."}), 400

    app.logger.info(f"Gerando código para prompt: {prompt_usuario[:50]}...")

    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHAVE_GROQ}"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": "Você é um gerador de código HTML e CSS. Responda SOMENTE com código puro. NUNCA use crases, markdown ou explicações. Formato: primeiro <style> com o CSS, depois o HTML. Siga EXATAMENTE o que o usuário pedir. Se pedir algo quicando, use translateY no @keyframes. Se pedir algo girando, use rotate."
            },
            {"role": "user", "content": prompt_usuario}
        ]
    }

    try:
        resposta = requests.post(url, json=payload, headers=headers, timeout=30)
        resposta.raise_for_status()

        resultado_ia = resposta.json()
        codigo = resultado_ia.get('choices', [{}])[0].get('message', {}).get('content')

        if not codigo:
            app.logger.error("Resposta da API não contém código")
            return jsonify({"erro": "Resposta inesperada da API. Verifique o log do servidor."}), 502

        app.logger.info("Código gerado com sucesso")
        return jsonify({"codigo": codigo})
    except requests.RequestException as e:
        app.logger.error(f"Erro na requisição à API: {str(e)}")
        return jsonify({"erro": f"Erro na requisição à API: {str(e)}"}), 502
    except Exception as e:
        app.logger.error(f"Erro inesperado: {str(e)}")
        return jsonify({"erro": str(e)}), 500

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)
=======
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv
import logging

# Carrega a chave do arquivo .env
load_dotenv()
CHAVE_GROQ = os.getenv("GROQ_API_KEY")

app = Flask(__name__)
CORS(app) # Isso permite que seu site fale com o servidor Python

# Configura logging
logging.basicConfig(level=logging.INFO)

@app.route('/gerar', methods=['POST'])
def gerar():
    dados_recebidos = request.get_json(silent=True)
    prompt_usuario = dados_recebidos.get('prompt') if dados_recebidos else None

    if not CHAVE_GROQ:
        app.logger.error("Chave da API não encontrada no .env")
        return jsonify({"erro": "Chave da API não encontrada. Verifique o arquivo .env."}), 500

    if not prompt_usuario:
        app.logger.warning("Prompt inválido ou ausente na requisição")
        return jsonify({"erro": "Prompt inválido ou ausente. Envie JSON com 'prompt'."}), 400

    app.logger.info(f"Gerando código para prompt: {prompt_usuario[:50]}...")

    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHAVE_GROQ}"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": "Você é um gerador de código HTML e CSS. Responda SOMENTE com código puro. NUNCA use crases, markdown ou explicações. Formato: primeiro <style> com o CSS, depois o HTML. Siga EXATAMENTE o que o usuário pedir. Se pedir algo quicando, use translateY no @keyframes. Se pedir algo girando, use rotate."
            },
            {"role": "user", "content": prompt_usuario}
        ]
    }

    try:
        resposta = requests.post(url, json=payload, headers=headers, timeout=30)
        resposta.raise_for_status()

        resultado_ia = resposta.json()
        codigo = resultado_ia.get('choices', [{}])[0].get('message', {}).get('content')

        if not codigo:
            app.logger.error("Resposta da API não contém código")
            return jsonify({"erro": "Resposta inesperada da API. Verifique o log do servidor."}), 502

        app.logger.info("Código gerado com sucesso")
        return jsonify({"codigo": codigo})
    except requests.RequestException as e:
        app.logger.error(f"Erro na requisição à API: {str(e)}")
        return jsonify({"erro": f"Erro na requisição à API: {str(e)}"}), 502
    except Exception as e:
        app.logger.error(f"Erro inesperado: {str(e)}")
        return jsonify({"erro": str(e)}), 500

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)
>>>>>>> Stashed changes
