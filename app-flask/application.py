import os
from flask.scaffold import F

from dotenv import load_dotenv
from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, flash, redirect, render_template, request, session


app = Flask(__name__)

app.config['SECRET_KEY'] = 'reemplazar_clave_secreta'

# Instancia de SocketIo

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route('/', methods=["GET", "POST"])
def home():

    return render_template('index.html')


@ app.route("/home/add_product", methods=["GET", "POST"])
def add_product():

    return render_template("add-product.html")


@app.route('/home/list_product')
def list_product():

    return render_template('list-product.html')


@app.route('/home/list_platillo')
def list_platillo():

    return render_template('list_platillo.html')


@app.route('/eliminar_platillos/<id>')
def eliminar_platillos(id):

    flash("producto eliminado")
    return redirect('/home/list_platillo')


@app.route('/eliminar_productos/<id>')
def eliminar_productos(id):

    flash("producto eliminado")
    return redirect('/home/list_product')


@app.route('/eliminar_ventas/<id>')
def eliminar_ventas(id):

    flash("venta eliminado")
    return redirect('/home/list_sale')


@app.route('/mensaje', methods=["GET"])
def mensaje():

    return render_template("message.html")


@app.route("/modal", methods=["GET"])
def modal():
    return render_template("modal.html")


@app.route('/home/add_sale', methods=["GET", "POST"])
def add_sale():

    return render_template('add-sale.html')


@app.route('/home/list_sale')
def list_sale():

    return render_template('list-sale.html')


@app.route('/home/add_platillo', methods=["GET", "POST"])
def add_platillo():

    return render_template('add-platillo.html')


@app.route('/home/error')
def error():
    return render_template('404.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    return render_template("register.html")


@app.route('/home/change_password', methods=["GET", "POST"])
def change():

    return render_template("change_password.html")


@app.route('/home/chat', methods=["GET", "POST"])
def chat():

    return render_template("chat.html")


@app.route('/home/report', methods=["GET", "POST"])
def report():

    return render_template("report.html")


@app.route('/home/list_report', methods=["GET", "POST"])
def list_report():

    return render_template("list-report.html")


@app.route('/report/<id>', methods=["GET", "POST"])
def report_id(id):

    return render_template("report-detallado.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


