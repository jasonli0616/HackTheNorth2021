from flask import Flask, json, render_template, url_for, request, redirect, session, flash, jsonify
import pymongo
import hashlib
import dotenv
import os

dotenv.load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Configure MongoDB
mongodb_client = pymongo.MongoClient(os.getenv('MONGODB_URI'))
mongodb_cluster = mongodb_client['Cluster0']
mongodb_users = mongodb_cluster['users']

def toHash(value:str):
    '''Returns hashed string'''
    hash_obj = hashlib.sha256(bytes(value, 'utf8'))
    return hash_obj.hexdigest()

@app.route('/')
def index():
    if 'user' in session:
        # get 
        try:
            budget = mongodb_users.find_one({'username': session['user']})['budget']
        except:
            budget = {}
        
        return render_template('budget.html', session=session, user=session['user'], budget=budget)
    return render_template('index.html', session=session)



'''
User authentication
------------------------------
'''

@app.route('/login', methods=['GET', 'POST'])
def login():

    if "user" in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        email = request.form['email']
        password = toHash(request.form['password'])

        user = mongodb_users.find_one({'email': email, 'password': password})

        if user:
            # if username and password correct
            session["user"] = user['username']
            flash('You are logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Incorrect email or password', 'danger')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():

    # if user already logged in redirect to home page
    if "user" in session:
        return redirect(url_for('index'))

    # if registering
    if request.method == 'POST':
        success = True

        # get data from form
        username = request.form['username']
        email = request.form['email']
        password = toHash(request.form['password'])
        confirm_password = toHash(request.form['confirm-password'])

        # if passwords don't match return error
        if password != confirm_password:
            success = False
            flash("Passwords don't match. Please try again.", 'danger')

        # if equals nothing return error
        if not username:
            success = False
            flash('Please enter a username.', 'danger')
        if not email:
            success = False
            flash('Please enter an email.', 'danger') 
        if not password:
            success = False
            flash('Please enter a password.', 'danger')

        if mongodb_users.find_one({'username': username}):
            success = False
            flash('Username already exists. Please try with a different username.', 'danger')
        if mongodb_users.find_one({'email': email}):
            success = False
            flash('Email already exists. Please try with a different email.', 'danger')

        # if success then flash success message and take to login page
        if success:

            user = {
                'username': username,
                'email': email,
                'password': password,
                'budget': {}
            }
            mongodb_users.insert_one(user)

            flash('Your account has been created.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    '''Logout page'''
    # if user not logged in send to login page
    if not "user" in session:
        return redirect(url_for('login'))
    # Remove data from session
    session.pop("user")
    return redirect(url_for('index'))

'''
------------------------------
'''



'''
Creating and managing budgets
------------------------------
'''

@app.route('/api/create-budget/', methods=['POST'])
def api_create_budget():
    mongodb_users.update_one(
        {'username': session['user']},
        {'$set': {'budget': request.json}}
    )
    
    return jsonify(request.json)


@app.route('/api/get-budget/')
def api_get_budget():
    return jsonify(mongodb_users.find_one({'username': session['user']})['budget'])

@app.route('/view')
def view():
    if "user" in session:
        return render_template('chart.html', session=session, budget=mongodb_users.find_one({'username': session['user']})['budget'])
    else:
        return redirect(url_for('index'))

'''
------------------------------
'''

def main():
    app.run(debug=True)
    # app.run('0.0.0.0', 443)


if __name__ == '__main__':
    main()

