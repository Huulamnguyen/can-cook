""" Application """
from flask import Flask, render_template, request, g, session, redirect, flash
from flask_bcrypt import Bcrypt
from models import connect_db, User, Favorite, db
from forms import RegisterForm, LoginForm
from config import app_config, Config
from sqlalchemy.exc import IntegrityError
from .parser import strip_tags
from .recipe import get_random_joke, get_random_recipes, search_recipes, get_recipe_detail, visualize_recipe_equipments, visualize_recipe_ingredients, get_analyzed_recipe_instructions

CURR_USER_KEY = "curr_user"
bcrypt = Bcrypt()
app = Flask(__name__)
app.config['SECRET_KEY'] = Config.SECRET_KEY

def create_app(config_name):
    app.config.from_object(app_config[config_name])
    app_config[config_name].init(app)
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
@app.route('/user', methods=['GET'])
def show_user():
    """Show detail of user"""
    if not g.user:
        flash('Access unauthorized. PLease register or login first', 'danger')
        return redirect('/')
    
    user_favorites = Favorite.query.filter(Favorite.user_id == g.user.id).all()
    likes = [ favorite.recipe_id for favorite in user_favorites ]

    favorites = []

    for rec_id in likes:
        recipe = get_recipe_detail(rec_id)
        favorites.append(recipe)

    return render_template('users/user_detail.html', user = g.user, favorites = favorites)

# todo: user's favorites route - show all logged-in user favorite recipes and a function to remove recipe from favorites
@app.route('/user/favorites', methods=['GET', 'POST'])
def user_favorites():
    """ Show all logged-in user favorite recipes and a function to remove a recipe from favorite list."""
    if not g.user:
        flash('Access unauthorized. Please register or login first', 'danger')
        return redirect('/')
    
    user_favorites = Favorite.query.filter(Favorite.user_id == g.user.id).all()
    likes = [ favorite.recipe_id for favorite in user_favorites ]

    favorites = []

    for rec_id in likes:
        recipe = get_recipe_detail(rec_id)
        favorites.append(recipe)
        
    return render_template('users/user_favorites.html', user = g.user, favorites = favorites)
    
# todo: show edit user form and submit the edit form to database
@app.route('/user/edit', methods=['GET','POST'])
def edit_user_detail():
    """Edit and update for current user"""
    if not g.user:
        flash('Access unauthorized. Please register or login first', 'danger')
        return redirect('/')
    
    user = g.user
    form = RegisterForm(obj=user)

    if form.validate_on_submit():
        if User.authenticate(user.username, form.password.data):
            # Catch error if user try to update with existed information
            try:
                user.username = form.username.data
                user.email = form.email.data
                user.image_url = form.image_url.data
                db.session.commit()
                return redirect('/user')
            except IntegrityError:
                # If there is any error it will flash this message.
                flash('Your input is already existed, please try again', 'danger')
                return redirect('/user')
        flash('Wrong password, please try again.', 'danger')
    return render_template('users/user_edit.html', form = form, user = user)

# todo: delete user
@app.route('/user/delete', methods=['POST'])
def delete_user():
    """Delete user and related favorite recipes """
    if not g.user:
        flash('Access unauthorized. Please register or login first', 'danger')
        return redirect('/')
    
    user_to_delete_favorites = Favorite.query.filter(Favorite.user_id == g.user.id).all()

    for user_to_delete_favorite in user_to_delete_favorites:
        db.session.delete(user_to_delete_favorite)
    
    do_logout()

    db.session.delete(g.user)
    db.session.commit()

    return redirect("/register")

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
    return render_template('home_anon.html', random_recipes = random_recipes, random_joke=random_joke)

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

    if g.user:
        user_favorites = Favorite.query.filter(Favorite.user_id == g.user.id).all()
        favs = [ recipe.recipe_id for recipe in user_favorites ]
        return render_template('recipes/recipe_detail.html', 
                            recipe_detail = recipe_detail,
                            recipe_summary = strip_tags(recipe_detail['summary']),
                            recipe_equipments = recipe_equipments,
                            recipe_ingredients = recipe_ingredients,
                            analyzed_instructions = analyzed_instructions,
                            favorites = favs)
    else:
        return render_template('recipes/recipe_detail.html', 
                            recipe_detail = recipe_detail,
                            recipe_summary = strip_tags(recipe_detail['summary']),
                            recipe_equipments = recipe_equipments,
                            recipe_ingredients = recipe_ingredients,
                            analyzed_instructions = analyzed_instructions)

# todo: /recipes/id/like - toggle the like button to add/remove a favorite recipe for the current logged-in user
@app.route('/recipes/<int:recipe_id>/like', methods=['POST'])
def add_favorite_recipe(recipe_id):
    """Toggle a favorite recipe for the current logged-in user"""
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    user_favorites = Favorite.query.filter(Favorite.user_id == g.user.id).all()
    likes = [ recipe.recipe_id for recipe in user_favorites ]

    if recipe_id in likes:
        Favorite.query.filter(Favorite.user_id == g.user.id, Favorite.recipe_id == recipe_id).delete()
        db.session.commit()
    else:
        favorite = Favorite(user_id=g.user.id, recipe_id=recipe_id)
        db.session.add(favorite)
        db.session.commit()
        
    return redirect(f"/recipes/{recipe_id}")

# todo: remove favorite recipe from favorite list
@app.route('/recipes/<int:recipe_id>/remove', methods=['POST'])
def remove_favorite(recipe_id):
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
    
    # Get id of recipe (not recipe_id of API) in favorites table
    recipe_to_delete_id = Favorite.query.filter(Favorite.user_id == g.user.id, Favorite.recipe_id == recipe_id).one().id
    
    recipe_to_delete = Favorite.query.get_or_404(recipe_to_delete_id)
    db.session.delete(recipe_to_delete)
    db.session.commit()

    return redirect("/user/favorites")
