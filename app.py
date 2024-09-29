from flask import Flask
from controllers.user_controller import index, create, update, list, delete

app = Flask(__name__)

# Rotas
app.add_url_rule('/', 'index', index)
app.add_url_rule('/create', 'create', create, methods=['GET', 'POST'])
app.add_url_rule('/update/<int:user_id>', 'update', update, methods=['GET', 'POST'])
app.add_url_rule('/list', 'list', list)
app.add_url_rule('/delete/<int:user_id>', 'delete', delete)

if __name__ == '__main__':
    app.run(debug=True)
