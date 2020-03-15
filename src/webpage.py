from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_User'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'leasesco_FreeLanceX'

mySql = MySQL(app)

@app.route('/')
def casa():
    return render_template('inicio.html')

@app.route('/login')
def log():
    return render_template('login.html')

@app.route('/loginData', methods=['POST'])
def login():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        clave = request.form['Clave']
        cur = mySql.connection.cursor()
        cur.excecute('INSERT INTO Usuarios (Nombre, Clave) VALUES (%s, %s)', (nombre, clave))
        mySql.connection.commit()
        return 'Correcto'

if __name__ == '__main__':
    app.run(debug=True)

