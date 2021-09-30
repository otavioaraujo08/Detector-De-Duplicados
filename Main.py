from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from services.detect_duplicator import DetectDuplicator
import openpyxl

# Chamando a classe princiapal
app = Flask(__name__)
detect_duplicator = DetectDuplicator()


# Configurando a página inicial como Siac.html
@app.route("/")
def receber_excel():
    return render_template("Index.html")


# Requisitando/Salvando/Abrindo/ funções da Classe para o Arquivo
@app.route("/open_spreadsheet", methods=["POST"])
def open_spreadsheet():
    file = request.files["file"]
    file_name = file.filename
    print(file_name)
    file.save(secure_filename(file_name))

    detect_duplicator.open_excel(file_name)
    return redirect(url_for("select_columns"))


# Recebendo a Coluna a Ser Filtrada
@app.route("/select_columns")
def select_columns():
    return render_template("Colun_Filter.html", columns=detect_duplicator.get_columns())


# Recebendo Os Valores do Input e Redirecionando para Outra Página
@app.route("/filter_values", methods=["POST"])
def filter_values():
    columns = list(request.form.values())
    detect_duplicator.filter_duplicated(columns)

    return redirect(url_for("export_excel"))


# Apos a Filtragem criar um novo arquivo
@app.route("/export_excel")
def export_excel():
    detect_duplicator.export_excel("output_teste.xlsx")

    return send_file("output_teste.xlsx")


# Caso Debug = True, Está em Período de Produção
app.run(debug=True)
