from flask import *
from models.vegetablesFruits import Vegetablesfruits
from models.animal import Animals
from models.user import User
import bcrypt
import mlab

app = Flask(__name__)
app.secret_key = 'mysecret'
mlab.connect()


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "GET":
       return render_template("login.html")
    elif request.method == "POST":
        form = request.form 
        username = form["username"]
        password = form["pass"]
    login_user = User.objects(username=username).first() 
    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('learn'))
    flash('Username or password wrong! Please try again!')
    return redirect(url_for('login'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "GET":
         return render_template('register.html')
       
    if request.method == 'POST':
        existing_user = User.objects(username = request.form["username"]).first()

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users = User(
                username = request.form['username'], 
                password = hashpass
                )
            users.save()
            session['username'] = request.form['username']
            return redirect(url_for('login'))
        if existing_user:
            flash('Username address already exists')
            return redirect(url_for('register'))

@app.route('/logout')
def logout():
    del session["username"]
    return redirect("/login")


@app.route('/learn')
def learn():
    return render_template("learn.html")

@app.route('/vegetablesAndFruits')
def vegetablesAndFruits():
    list_audio = []
    list_word  = []
    list_image = []
    list_pronunciation = []
    list_id = []
     # get all document from dabase
    total_vegetablesAndFruits = Vegetablesfruits.objects()
    for i in total_vegetablesAndFruits:
        audio = i.audio_link
        word  = i.word
        image = i.image
        pronunciation = i.pronunciation
        id = i.id
        list_audio.append(audio)
        list_word.append(word)
        list_image.append(image)
        list_pronunciation.append(pronunciation)
        list_id.append(id)
    return render_template("vegetablesAndFruits.html",
                            list_audio=list_audio,
                            list_word=list_word,
                            list_image=list_image,
                            list_pronunciation=list_pronunciation,
                            list_id=list_id)
    
@app.route('/vegetablesAndFruitsDetail/<id>')
def vegetablesAndFruitsDetail(id):
    vegetables_fruits_id = Vegetablesfruits.objects.with_id(id)
    return render_template("vegetablesAndFruitsDetail.html",
                            vegetables_fruits_id=vegetables_fruits_id)

@app.route('/animals')
def animals():
    list_audio = []
    list_word  = []
    list_image = []
    list_pronunciation = []
    list_id = []
     # get all document from dabase
    total_animals = Animals.objects()
    for i in total_animals:
        audio = i.audio_link
        word  = i.word
        image = i.image
        pronunciation = i.pronunciation
        id = i.id
        list_audio.append(audio)
        list_word.append(word)
        list_image.append(image)
        list_pronunciation.append(pronunciation)
        list_id.append(id)
    return render_template("animals.html",
                            list_audio=list_audio,
                            list_word=list_word,
                            list_image=list_image,
                            list_pronunciation=list_pronunciation,
                            list_id=list_id)


@app.route('/animalDetail/<id>')
def animalDetail(id):
    animal_id = Animals.objects.with_id(id)
    return render_template("animalDetail.html",animal_id=animal_id)

if __name__ == '__main__':
    app.run(debug=True)