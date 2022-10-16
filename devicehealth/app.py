from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'karina1243'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route('/form')
def form():
    return render_template('form.html')
    
@app.route('/login', methods = ['POST', 'GET'])

def login():
    if request.method == 'GET':
        return "Collect data via system"
     
    if request.method == 'POST':
        name = request.form['name']
        color = request.form['Color']
        quantity = request.form['Quantity']

        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,color,quantity))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"

app.run(host='localhost', port=3306)