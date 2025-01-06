from flask import Flask, render_template, redirect, url_for, flash,request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import bcrypt
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'oracle123' 
app.config['MYSQL_DB'] = 'col-bi'
app.secret_key = 'my_secret_key'

mysql = MySQL(app)

# Registration Form
class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Register')

# Login Form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route("/", methods=["GET"])
def welcome():
    return redirect(url_for('register'))

@app.route("/index", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/find")
def find():
    return render_template('find.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/teammates")
def teammates():
    return render_template('teammates.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        try:
            # Insert the user into the database
            cursor = mysql.connection.cursor()
            cursor.execute(
                "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                (name, email, hashed_password)
            )
            mysql.connection.commit()
            cursor.close()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'Error: {e}', 'danger')
            return redirect(url_for('register'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        # Check user credentials in the database
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT password FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()

        if user and bcrypt.checkpw(password.encode('utf-8'), user[0].encode('utf-8')):
            flash('Login successful!', 'success')
            return render_template('index.html')
        else:
            flash('Invalid email or password', 'danger')
    return render_template('login.html', form=form)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        # Get the search input from the user
        search_specs = request.form.get('teammate_spec')  # Corrected form retrieval

        cursor = mysql.connection.cursor()
        try:
            # Query to find matched teammates
            query = """
SELECT DISTINCT *
FROM find_teammate
WHERE LOWER(teammate_specs) LIKE LOWER(%s);
"""

            cursor.execute(query, (search_specs,))  # Passing the user input as a parameter
            results = cursor.fetchall()  # Fetch all matching rows
        except Exception as e:
            flash(f"An error occurred: {e}", "danger")
            results = []
        finally:
            cursor.close()
            return render_template('search.html', results=results)
    else:
        # Render the search form for GET requests (in case needed)
        return render_template('search.html', results=None)

@app.route('/find', methods=['POST', 'GET'])
def find_teammate():
    if request.method == 'POST':
        # Get the form data submitted by the user
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        gender = request.form['gender']
        field = request.form['field']
        current_proj = request.form['current_proj']
        teammate_specs = request.form['teammate_specs']

        cursor = mysql.connection.cursor()
        try:
            # Insert all user-provided details directly into the find_teammate table
            insert_query = """
            INSERT INTO find_teammate (name, email, age, gender, field, current_proj, teammate_specs)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(insert_query, (name, email, age, gender, field, current_proj, teammate_specs))
            mysql.connection.commit()

            # Query to fetch matched rows
            match_query = """
            SELECT DISTINCT f2.*
            FROM find_teammate f1
            JOIN find_teammate f2
            ON (f1.teammate_specs LIKE CONCAT('%', f2.teammate_specs, '%') 
                OR f2.teammate_specs LIKE CONCAT('%', f1.teammate_specs, '%'))  -- Bidirectional match
            WHERE f1.id = (SELECT MAX(id) FROM find_teammate)  -- Last inserted row
            AND f1.id != f2.id;  -- Exclude the last row itself

            """
            cursor.execute(match_query)
            results = cursor.fetchall()  # Fetch all matching rows

        except Exception as e:
            flash(f'An error occurred: {e}', 'danger')
            return redirect(url_for('find_teammate'))
        finally:
            cursor.close()

        # Render the matched results
        return render_template('teammates.html', results=results)

    # Render the form for GET requests
    return render_template('find_teammate.html')


if __name__ == "__main__":
    app.run(debug=True)
