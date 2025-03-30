from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import DatabaseManager
from forms import RegistrationForm, LoginForm, PostForm

routes = Blueprint('routes', __name__)
db = DatabaseManager('data.db')

@routes.route('/')
def index():
    user_id = session.get('user_id', 'public')
    if user_id == 'public':
        flash('You are viewing as a public user.', 'info')
        posts = db.post_of_all()  # Fetch posts for public users
    else:
        posts = db.post_of_user(user_id)  # Replace 'user_id' with actual user ID logic
    return render_template('index.html', posts=posts)

@routes.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        db.register_user(user_id, password)
        flash('Registration successful!', 'success')
        return redirect(url_for('routes.login'))
    return render_template('register.html', form=form)

@routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Implement login logic here
        flash('Login successful!', 'success')
        user_id = form.user_id.data
        password = form.password.data
        # TODO: Implement login logic to verify user credentials
        if password != db.get_password(user_id):
            flash('Invalid credentials', 'danger')
            session['user_id'] = 'public'  # Clear session if login fails
            return redirect(url_for('routes.login'))
        else:
            flash('Login successful!', 'success')
            session['user_id'] = user_id  # Store user_id in session
        return redirect(url_for('routes.index'))
    return render_template('login.html', form=form)

@routes.route('/logout')
def logout():
    session["user_id"] = 'public'  # Clear session
    flash('Logged out successfully!', 'success')
    return redirect(url_for('routes.index'))

@routes.route('/delete_user/<user_id>', methods=['POST'])
def delete_user(user_id):
    db.delete_user(user_id)
    flash('User deleted successfully!', 'success')
    return redirect(url_for('routes.index'))

@routes.route('/update_password/<user_id>', methods=['POST'])
def update_password(user_id):
    new_password = request.form.get('new_password')
    db.update_user_password(user_id, new_password)
    flash('Password updated successfully!', 'success')
    return redirect(url_for('routes.index'))
import uuid
from datetime import datetime
@routes.route('/create_post', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        content = form.content.data
        # Implement post creation logic here, e.g., save to database
        post_id = str(uuid.uuid4())
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Assuming user_id is stored in session
        user_id = session.get('user_id', 'public')
        # Save the post to the database
        db.add_post(post_id, time, content, user_id)
        flash('Post created successfully!', 'success')
        return redirect(url_for('routes.index'))
    return render_template('create_post.html', form=form)