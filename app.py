from flask import Flask, render_template, request

# Criando a aplicação Flask
app = Flask(__name__)

# Rota principal
@app.route('/')
def home():
    return "Olá! O Flask está funcionando corretamente."

# Exemplo de rota com formulário
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        return f"Usuário: {usuario}, Senha: {senha}"
    return '''
        <form method="POST">
            Usuário: <input type="text" name="usuario"><br>
            Senha: <input type="password" name="senha"><br>
            <input type="submit" value="Entrar">
        </form>
    '''

# Executando o app
if __name__ == '__main__':
    app.run(debug=True)
