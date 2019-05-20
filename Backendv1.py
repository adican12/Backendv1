from flask import Flask ,render_template ,redirect, url_for, request
from flask import make_response
#from flask import abort
import yaml
from flask import Flask, render_template, send_file, request, session, redirect, url_for
from flask_mysqldb import MySQL



app = Flask(__name__)
#api = Api(app)
#app = connexion.FlaskApp(__name__, specification_dir='./')
#yaml.load('db.yaml',Loader=yaml.FullLoader)
#app.add_api('api/db.yaml')
#app.config['SECRET_KEY'] = 'catwifi'

#Configure db
# db = yaml.load(open('C:\\Users\\yarde\\PycharmProjects\\Backendv1\\db.yaml'),Loader=yaml.FullLoader)
# app.config['MYSQL_HOST']=db['mysql_host']
# app.config['MYSQL_USER']=db['mysql_user']
# app.config['MYSQL_PASSWORD']=db['mysql_password']
# app.config['MYSQL_DB']=db['mysql_db']
# mysql = MySQL(app)
#


@app.route('/')
def home():
    # #conn = db_connect.connect()  # connect to database
    # cur = mysql.connection.cursor()
    # #cur.execute('INSERT INTO user( name , age ) VALUES (%s,%s)',('yarden','26'))
    # #mysql.connection.commit()
    # user_agent = request.headers.get('User-Agent')
    # return '<p>Your browser is %s</p>' % user_agent
    return render_template('welcome.html')




@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

#cookie response
@app.route('/cookie')
def coockie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/api')
def api():
 pass
#
# @app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name=name)

#
# def load_user(id):
#     list_of_user=[11,22,33,44]
#     if id in list_of_user:
#         return id

# @app.route('/user/<id>')
# def get_user(id):
#   user = load_user(id)
#   if not user:
#     abort(404)
#   return '<h1>Hello, %s</h1>' % user.name

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    # if request.method == 'POST':
    #     if request.form['username'] != 'admin' or request.form['password'] != 'admin':
    #         error = 'Invalid Credentials. Please try again.'
    #     else:
    #         return redirect(url_for('home'))
    return render_template('login.html', error=error)




#error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500





if __name__ == '__main__':
    app.run(debug=True)

