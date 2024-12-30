from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    result = val_user * val_user
    return render_template('result.html', operation='square', value=val_user, result=result)

@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    result = valeur1 + valeur2
    parite = "paire" if result % 2 == 0 else "impaire"
    return render_template('result.html', operation='sum', values=(valeur1, valeur2), result=result, parite=parite)

@app.route('/sommes', methods=['GET'])
def somme_param():
    valeurs = request.args.getlist('valeur')
    
    try:
        valeurs = [int(v) for v in valeurs]
    except ValueError:
        return "Toutes les valeurs doivent être des entiers", 400
    
    total = sum(valeurs)
    return render_template('result.html', operation='sum_multiple', values=valeurs, result=total)

if __name__ == "__main__":
    app.run(debug=True)
