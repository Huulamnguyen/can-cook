""" Application """
from flask import Flask, render_template, request, g, session, redirect, flash
from flask_bcrypt import Bcrypt
from models import connect_db, User, db
from forms import RegisterForm, LoginForm
from config import app_config
from sqlalchemy.exc import IntegrityError
from .parser import strip_tags
from .recipe import get_random_joke, get_random_recipes, search_recipes, get_recipe_detail, visualize_recipe_equipments, visualize_recipe_ingredients, get_analyzed_recipe_instructions

CURR_USER_KEY = "curr_user"
bcrypt = Bcrypt()
app = Flask(__name__)

def create_app(config_name):
    app.config.from_object(app_config[config_name])
    connect_db(app)
    return app

@app.before_request
def add_user_to_g():
    """If user has logged in, add current user to Flask global object."""
    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])
    else:
        g.user = None

def do_login(user):
    """Method logs in the user."""
    session[CURR_USER_KEY] = user.id

def do_logout():
    """Method logs out user."""
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

# todo: register route
@app.route('/register', methods=['GET', 'POST'])
def register_user():
    """ Handle User Sign-up. """
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            user = User.register(username = form.username.data, email = form.email.data, image_url = form.image_url.data, password = form.password.data)
            db.session.commit()
            do_login(user)
            flash("Welcome!", "success")
            return redirect('/')
        except IntegrityError:
            flash("Invalid information", 'danger')
            return render_template('users/user_register.html', form = form)
    else:
        return render_template('users/user_register.html', form = form)

# todo: user route
@app.route('/user', methods=['GET', 'POST'])
def show_user():
    """Show detail of user"""
    return render_template('users/user_detail.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login"""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.authenticate(form.username.data, form.password.data)
        if user:
            do_login(user)
            # Flash a message if user successfully logged in
            flash("You are successfully logged in", 'success')
            return redirect('/')
        # Flash a message if there is no match username and password
        flash("Invalid credentials.", 'danger')
    return render_template('users/user_login.html', form = form)

@app.route('/logout')
def logout():
    """Handle user logout."""
    do_logout()
    # Flash a message if user successfully logged out
    flash("Successfully logged out!", "success")
    return redirect("/")

# todo: to app homepage
@app.route('/', methods=['GET'])
def homepage():
    """ Show Home Page - Navbar - Random Food Joke - Random Recipes"""
    random_recipes = get_random_recipes()
    random_joke = get_random_joke()
    return render_template('home.html', random_recipes = random_recipes, random_joke=random_joke)


# todo: /recipes - return recipes by searching name
@app.route('/recipes', methods=['GET'])
def recipes():
    """Page with listing of recipes. Can take a 'q' param in querystring to search by that name."""
    name = request.args.get('q')
    recipes = search_recipes(name)
    return render_template('recipes/recipes.html', recipes=recipes)

# todo: /recipes/id - return recipe detail including title, image, summary, equipments, ingredients and other information
@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def recipe_detail(recipe_id):
    """ Show recipe detail by id"""
    recipe_detail = get_recipe_detail(recipe_id)
    recipe_equipments = visualize_recipe_equipments(recipe_id)
    recipe_ingredients = visualize_recipe_ingredients(recipe_id)
    analyzed_instructions = get_analyzed_recipe_instructions(recipe_id)
    return render_template('recipes/recipe_detail.html', 
                            recipe_detail = recipe_detail,
                            recipe_summary = strip_tags(recipe_detail['summary']),
                            recipe_equipments = recipe_equipments,
                            recipe_ingredients = recipe_ingredients,
                            analyzed_instructions = analyzed_instructions)