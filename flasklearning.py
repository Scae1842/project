from flask import Flask, render_template, jsonify, request, json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello <b>you </b>!"

@app.route('/dashboard/')
def accueil():
    return render_template("affichage.html")


@app.route('/ecoute', methods=['POST'])
def ecouteur():
    if request.headers['Content-Type'] == 'application/json':
        mes_infos = request.json
        print(mes_infos["meta"]["id"])
        return mes_infos


@app.route('/api/meteo/')
def meteo():
    dictionnaire = {
        'type': 'Prévision de température',
        'valeurs': [24, 24, 25, 26, 27, 28],
        'unite': "degrés Celcius"
    }
    return jsonify(dictionnaire)


if __name__ == "__main__":
    #app.run()
    app.run(debug=True)
