
firebase  = pyrebase.pyrebase.initialize_app(firebaseConfing)
db = firebase.database()


from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    sepalLength = db.child("iris").child("sepalLength").get()

    return sepalLength.val()

app.run(debug=True)
