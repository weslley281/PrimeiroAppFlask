from flask import Flask

# Cria a aplicação Flask
app = Flask(__name__)

# Rota principal
@app.route('/')
def hello_world():
    return 'Olá, Mundo!'

# Executa a aplicação
if __name__ == '__main__':
    app.run(debug=True)
