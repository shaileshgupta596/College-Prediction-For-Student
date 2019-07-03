from flask import Flask, render_template, redirect, url_for,request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from wtforms_sqlalchemy.fields import QuerySelectField
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\\Users\\Gupta Niwas\\Downloads\\PBL SEM 4\\Webpage\\tejack_pbl\\database.db'
app.config['SQLALCHEMY_BINDS'] = {'two': r'sqlite:///C:\\Users\\Gupta Niwas\\Downloads\\PBL SEM 4\\Webpage\\tejack_pbl\\Details.db',
                                    'one': r'sqlite:///C:\\Users\\Gupta Niwas\\Downloads\\PBL SEM 4\\Webpage\\tejack_pbl\\database.db'}
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    __bind_key__ ='one'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])



class Details(db.Model):
    __bind_key__ ='two'

    index = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(70))
    Locality = db.Column(db.String(70))
    Course = db.Column(db.String(100))
    Fees = db.Column(db.Integer)
    Exam = db.Column(db.String(70))
    Affiliation = db.Column(db.String(70))
    
    

    def __repr__(self):
        return '[Choice {},{},{},{}]'.format(self.Locality,self.Name,self.Course,self.Exam)

def Details_query():
    return Details.query

class ChoiceForm(FlaskForm):
   
    stream = QuerySelectField(query_factory=Details_query, allow_blank=True, get_label='Name')
    course = QuerySelectField(query_factory=Details_query, allow_blank=True, get_label='Course')
    locality = QuerySelectField(query_factory=Details_query, allow_blank=True, get_label='Locality')
    exam = QuerySelectField(query_factory=Details_query, allow_blank=True, get_label='Exam')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return '<h1>Invalid username or password</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h1>'
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)

@app.route('/dashboard',methods=['GET', 'POST'])
@login_required
def dashboard():
    form = ChoiceForm()
    form.stream.query = db.session.query(Details).distinct(Details.Name).group_by(Details.Name)
    form.locality.query = db.session.query(Details).distinct(Details.Locality).group_by(Details.Locality)
    form.course.query = db.session.query(Details).distinct(Details.Course).group_by(Details.Course)
    form.exam.query = db.session.query(Details).distinct(Details.Exam).group_by(Details.Exam)
    if form.validate_on_submit():
        return render_template('col_disp.html')
    return render_template('dashboard.html', name=current_user.username,form=form)

@app.route('/submit' ,methods=['GET', 'POST'])
def submit():
    form = ChoiceForm()
    #if form.validate_on_submit():
    if request.method == 'POST':
       # print (request.form)

        return '<html><h1>{}</h1></html>'.format(form.locality.data) 

    return render_template('index.html', form=form)
   


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
