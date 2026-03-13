import os
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def conectar():
    return mysql.connector.connect(
        host=os.environ.get("MYSQLHOST", "localhost"),
        port=int(os.environ.get("MYSQLPORT", 3306)),
        user=os.environ.get("MYSQLUSER", "root"),
        password=os.environ.get("MYSQLPASSWORD", ""),
        database=os.environ.get("MYSQLDATABASE", "votacion_app")
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registro")
def registro():
    return render_template("registro.html")


@app.route("/consulta")
def consulta():
    return render_template("consulta.html")


@app.route("/guardar", methods=["POST"])
def guardar():

    nombre = request.form["nombre"]
    documento = request.form["documento"]
    lugar = request.form["lugar"]
    direccion = request.form["direccion"]
    mesa = request.form["mesa"]

    zona = "Urbana"

    db = conectar()
    cursor = db.cursor()

    sql = """INSERT INTO ciudadanos
    (nombre,documento,lugar_votacion,direccion,mesa,zona)
    VALUES (%s,%s,%s,%s,%s,%s)"""

    cursor.execute(sql,(nombre,documento,lugar,direccion,mesa,zona))

    db.commit()
    db.close()

    return redirect("/")


@app.route("/buscar", methods=["POST"])
def buscar():

    documento = request.form["documento"]

    db = conectar()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM ciudadanos WHERE documento=%s",(documento,))
    ciudadano = cursor.fetchone()

    db.close()

    return render_template("resultado.html", ciudadano=ciudadano)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
