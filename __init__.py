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
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)

@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
     #return "<h2>La somme de nos deux valeures est : </h2>" + str(val_user + val_user)      
    result = valeur1 + valeur2  # Calcul de la somme

    if result % 2 == 0:
        return f"<h2>La somme de {valeur1} et {valeur2} est {result}, et c'est un nombre pair.</h2>"
    else:
        return f"<h2>La somme de {valeur1} et {valeur2} est {result}, et c'est un nombre impair.</h2>"

@app.route('/sommes', methods=['GET'])
def somme_param():
    valeurs = request.args.getlist('valeur')  # recuperer la Liste des valeurs passées dans l'URL
    if not valeurs:  # Vérifier que des valeurs ont été envoyées
        return "Veuillez saisir des valeurs en utilisant le paramètre 'valeur'. Exemple : ?valeur=1&valeur=2&valeur=3", 400

    try:
        valeurs = [int(v) for v in valeurs]    # Convertir les valeurs en entiers
    except ValueError:
        return "Toutes les valeurs doivent être des entiers", 400    

    total = sum(valeurs)       # Calculer la somme des valeurs
    try:
        valeurs = [int(v) for v in valeurs] # Convertir les valeurs en entiers
    except ValueError:
        return "Toutes les valeurs doivent être des entiers", 400
    
    total = sum(valeurs)  # Calculer la somme des valeurs
    if total % 2 == 0:   # Vérifier si la somme est pair ou impair
        return f"<h2>La somme des valeurs {valeurs} est {total}, et c'est un nombre pair.</h2>"
    else:
        return f"<h2>La somme des valeurs {valeurs} est {total}, et c'est un nombre impair.</h2>"

@app.route('/cv')
def cv():
    return render_template('cv.html')

    
if __name__ == "__main__":
    app.run(debug=True)
