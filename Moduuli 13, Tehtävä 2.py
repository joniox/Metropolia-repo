# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja
# kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
# Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
# Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

from flask import Flask, jsonify
import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='lentopeli',
    user='root',
    password='root_pw',
    autocommit=True
)

app = Flask(__name__)

@app.route('/kenttä/<icao>')
def hae_lentokentän_tiedot(icao):
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()

    if tulos:
        airport, municipality = tulos
        print(f"ICAO: {icao}, Name: {airport}, Municipality: {municipality}")
        return jsonify({
            "ICAO": icao,
            "Name": airport,
            "Municipality": municipality
        })
    else:
        return jsonify({"error": "Airport not found"}), 404


if __name__ == '__main__':
    app.json.sort_keys = False
    app.run(use_reloader=True, host='127.0.0.1', port=3000)



