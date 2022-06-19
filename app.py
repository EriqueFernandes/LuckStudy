import yaml
from yaml import Loader

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html" )

@app.route("/calculo")
def calculo():
    f = open("yaml/calculo.yaml",encoding='utf8')
    yam = yaml.load_all(f,Loader=Loader)
    return render_template("questoes.html", dados = yam )

@app.route("/modelagem")
def modelagem():
    f = open("yaml/modelagem.yaml",encoding='utf8')
    yam = yaml.load_all(f,Loader=Loader)
    return render_template("questoes.html", dados = yam )

@app.route("/ga")
def ga():
    f = open("yaml/ga.yaml",encoding='utf8')
    yam = yaml.load_all(f,Loader=Loader)
    return render_template("questoes.html", dados = yam )
    
@app.route("/fundamentos")
def fundamentos():
    f = open("yaml/fundamentos.yaml",encoding='utf8')
    yam = yaml.load_all(f,Loader=Loader)
    return render_template("questoes.html", dados = yam )

@app.route("/ic")
def ic():
    f = open("yaml/ic.yaml",encoding='utf8')
    yam = yaml.load_all(f,Loader=Loader)
    return render_template("questoes.html", dados = yam )

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")
