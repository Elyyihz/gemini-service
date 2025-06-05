from flask import Flask, jsonify, request
from flask_cors import CORS
from naoeduca import make_question

app = Flask(__name__)
CORS(app)

@app.route('/api/', methods=['GET'])
def question_jano():
    question = request.args.get('question')
    if not question:
        return jsonify({'erro': 'Parâmetro "question" ausente'}), 400

    try:
        resposta = make_question(question)
        return jsonify({'resposta': resposta})
    except Exception as e:
        print("Erro no Gemini:", e)
        return jsonify({'erro': 'Erro ao processar a pergunta'}), 500
