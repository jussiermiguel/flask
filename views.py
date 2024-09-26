from app import app
from flask import redirect, render_template, request, url_for
from models import User, db
# rotas
@app.route("/")
def home():
    return render_template("home.html")

@app.route('/create-user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))  # Redireciona de volta para a página inicial após criar o usuário
    return render_template('create_user.html')

@app.route('/users')
def list_users():
    users = User.query.all()  # Buscar todos os usuários no banco de dados
    return render_template('list_users.html', users=users)

@app.route('/edit-user/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get_or_404(id)  # Busca o usuário pelo ID ou retorna 404
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        db.session.commit()
        return redirect(url_for('list_users'))  # Redireciona para a lista de usuários após editar
    return render_template('edit_user.html', user=user)

@app.route('/delete-user/<int:id>', methods=['POST'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('list_users'))  # Redireciona para a lista de usuários após excluir

