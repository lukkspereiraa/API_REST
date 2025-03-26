from flask import Flask, jsonify, request

app = Flask(__name__)

placas = [
    {
        'placa': 'ABC1234',
        'marca': 'Toyota',
        'modelo': 'Corolla',
        'cor': 'Prata',
        'ano': 2022,
    },
    {
        'placa': 'DEF5678',
        'marca': 'Ford',
        'modelo': 'Focus',
        'cor': 'Preto',
        'ano': 2021,
    },
    {
        'placa': 'GHI9012',
        'marca':'Honda',
        'modelo': 'Civic',
        'cor': 'Azul',
        'ano': 2020,
    },
]

@app.route('/placas', methods=['GET'])
def obter_plcas():
    return jsonify(placas)

@app.route('/placas/<string:placa>', methods=['GET'])
def obter_dados_por_placa(placa):
    for dados in placas:
        if dados.get('placa') == placa:
            return jsonify(dados)

@app.route('/placas/<string:placa>', methods=['PUT'])   
def editar_dados_por_placa(placa):
    dados_alterados = request.get_json()
    for indice, dados in enumerate(placas):
        if dados.get('placa') == placa:
            placas[indice].update(dados_alterados)
            return jsonify(placas[indice])

@app.route('/placas', methods=['POST'])
def incluir_novo_carro():
    novo_carro = request.get_json()
    placas.append(novo_carro)
    return jsonify(placas)

@app.route('/placas/<string:placa>', methods=['DELETE'])
def excluir_carro(placa):
    for indice, dados in enumerate(placas):
        if dados.get('placa') == placa:
            del placas[indice]

        return jsonify(placas)

app.run(port=5000, host='localhost', debug=True)                            