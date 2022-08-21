# Imports here

#creates flask app wuth the secret key for debugging
app = Flask(__name__)
app.config['SECRET_KEY'] = "1234"

#only for flask debug toolbar 
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

#only for flask-sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

#routes here
