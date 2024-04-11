from flask import Flask, jsonify
from consultas import fazerConsulta

app = Flask(__name__)

# Rota para obter todos os bancos
@app.route('/bancos', methods=['GET'])
def obter_bancos_route():
    # Chama a função de consulta
    df = fazerConsulta()
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
