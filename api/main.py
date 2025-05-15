from flask import request
from flask import Flask, redirect, url_for, session, request, abort
from functools import wraps
from data import db_session
from data.users import User
from data.apps import Apps
from forms.user import RegisterForm
from forms.user import LoginForm
from flask import render_template, make_response
import datetime
from flask_login import LoginManager
from flask_login import login_user
from flask_login import login_required
from flask_login import current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365
)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@app.route("/")
def index():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        apps = db_sess.query(Apps)
    else:
        apps = db_sess.query(Apps)
    return render_template("index.html", apps=apps)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Passwords do not match")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="User already have")
        user = User(
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/app_get_approve_status/<int:id>&<int:need_approve>', methods=['GET', 'POST'])
@login_required
def news_delete(id, need_approve):
    db_sess = db_session.create_session()
    apps = db_sess.query(Apps).filter(Apps.id == id,
                                      ).first()
    if apps:
        apps.approve = bool(need_approve)
        apps.seen = True
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')

@app.route("/session_test")
def session_test():
    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(
        f"Вы пришли на эту страницу {visits_count + 1} раз")

if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')
