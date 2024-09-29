from flask_mysqldb import MySQL
from flask import Flask

app = Flask(__name__)

# Configurações do MySQL
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud_flask'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # Opcional, facilita o retorno dos dados


mysql = MySQL(app)