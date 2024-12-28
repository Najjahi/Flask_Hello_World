from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')   #IMAN

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
  result = val_user * val_user  # Calcul de la somme
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user) 

@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    result = valeur1 + valeur2  # Calcul de la somme
    return f"La somme de {valeur1} et {valeur2} est {result}"
  if somme % 2 == 0:
        parite = "paire"
    else:
        parite = "impaire"
    
    # Retourner la réponse formatée
    return (f"Le carré de {valeur1} est {carre_valeur1}, le carré de {valeur2} est {carre_valeur2}, "
            f"et la somme de {valeur1} et {valeur2} est {somme}, qui est {parite}.")

@app.route('/somme', methods=['GET'])
def somme():
    # Récupérer les valeurs depuis les paramètres de la requête
    valeurs = request.args.getlist('valeur')  # Liste des valeurs passées dans l'URL
    
    # Convertir les valeurs en entiers
    try:
        valeurs = [int(v) for v in valeurs]
    except ValueError:
        return "Toutes les valeurs doivent être des entiers", 400
    
    # Calculer la somme avec une boucle
    total = 0
    for valeur in valeurs:
        total += valeur
    
    return f"La somme des valeurs {valeurs} est {total}"

                                                                                                               
if __name__ == "__main__":
  app.run(debug=True) 
