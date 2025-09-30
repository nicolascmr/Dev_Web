from .app import app
from flask import render_template, request
from monApp.models import Auteur,Livre
@app.route('/')
@app.route('/index/')
def index():
    # si pas de paramètres
    if len(request.args)==0:
        return render_template("index.html",title="R3.01 Dev Web avec Flask",name="Cricri")
    else :
        param_name = request.args.get('name')
    return render_template("index.html",title="R3.01 Dev Web avec Flask",name=param_name)
@app.route('/about/')
def about():
    return render_template("about.html",title ="R3.01 Dev Web avec Flask",name="Cricri", text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer egestas tempus sem. Maecenas vitae leo erat. Quisque fermentum quis nisl quis finibus. Donec auctor velit eu erat laoreet, sed dignissim est euismod. Vestibulum nec augue in felis laoreet tincidunt sed sit amet diam. Integer laoreet luctus nisl, ut interdum nisl efficitur eget. Vestibulum in augue id diam malesuada gravida eu accumsan lacus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum consequat pretium sagittis. Suspendisse ut ornare quam, nec convallis libero. Pellentesque ut augue malesuada, egestas justo eget, aliquet nisi. Donec tincidunt id dolor a feugiat. Ut sit amet ornare odio.")
@app.route('/contact/')
def contact():
    return render_template("contact.html",title ="R3.01 Dev Web avec Flask",name="Cricri", text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer egestas tempus sem. Maecenas vitae leo erat. Quisque fermentum quis nisl quis finibus. Donec auctor velit eu erat laoreet, sed dignissim est euismod. Vestibulum nec augue in felis laoreet tincidunt sed sit amet diam. Integer laoreet luctus nisl, ut interdum nisl efficitur eget. Vestibulum in augue id diam malesuada gravida eu accumsan lacus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum consequat pretium sagittis. Suspendisse ut ornare quam, nec convallis libero. Pellentesque ut augue malesuada, egestas justo eget, aliquet nisi. Donec tincidunt id dolor a feugiat. Ut sit amet ornare odio.")

@app.route('/auteurs/')
def getAuteurs():
    lesAuteurs = Auteur.query.all()
    return render_template('auteurs_list.html', title="R3.01 Dev Web avec Flask", auteurs=lesAuteurs)

@app.route('/livres/')
def getLivres():
    lesLivres = Livre.query.all()
    return render_template('livres_list.html', title="R3.01 Dev Web avec Flask", livres=lesLivres)


if __name__ == "__main__":
    app.run()