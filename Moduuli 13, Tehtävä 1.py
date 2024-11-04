# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
# Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    if luku < 2:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, int(luku ** 0.5) + 1):
            if luku % i == 0:
                is_prime = False
                break

    return jsonify({"Number": luku, "isPrime": is_prime})

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


