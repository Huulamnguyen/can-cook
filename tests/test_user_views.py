"""User View tests."""
from unittest import TestCase
from models import db, User, Favorite
from app import create_app, CURR_USER_KEY
from sqlalchemy.exc import InvalidRequestError

app = create_app('testing')
app.app_context().push()
class UserViewTestCase(TestCase):
    """Test views for users."""
    def setUp(self):
        """Create test client"""
        db.drop_all()
        db.create_all()

        self.app = create_app('testing')
        self.client = self.app.test_client()

        self.testuser = User.register('Monkey Test', 'monkeytest@gmail.com', None, 'Monkeytest')
        self.uid = 1111
        self.testuser.id = self.uid

        self.testuser_favorite = Favorite(user_id = self.uid, recipe_id = 479101)
        self.testuser_favorite_id = 1212
        self.testuser_favorite.id = self.testuser_favorite_id

        db.session.add(self.testuser_favorite)

        db.session.commit()

    def tearDown(self):
        response = super().tearDown()
        db.session.rollback()
        return response

    def test_register_redirect(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id
            resp = c.post('/register', follow_redirects=True)
            self.assertEqual(resp.status_code, 200)
        
    def test_user_signup(self):
        with self.client as c:
            resp = c.post('/register',
                            data = {'username': 'Monkey Test 1', 'email':'monkeytest1@gmail.com', 'image_url': None, 'password': 'monkeytest1'},
                            follow_redirects=True)
            html = resp.get_data(as_text = True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Welcome!', html)
            self.assertIn('Monkey Test 1', html)
    
    def test_invalid_user_signup(self):
        with self.client as c:

            resp = c.post('/register', 
                            data = {'username': 'Monkey Test', 'email':'monkeytest@gmail.com', 'image_url': None, 'password': 'monkeytest1'},
                            follow_redirects = True)

            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Invalid information", html)
    
    def test_user_login(self):
        user = User.register('Monkey Two', 'monkey2@gmail.com', None, 'monkey2')
        uid = 2222
        user.id = uid

        db.session.commit()
        with self.client as c:
            resp = c.post('/login',
                            data = {'username': 'Monkey Two', 'password': 'monkey2'},
                            follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Monkey Two', html)
            self.assertIn('You are successfully logged in', html)

    def test_invalid_user_login(self):
        with self.client as c:
            resp = c.post('/login', data = {'username':'Monkey 2', 'password':'monkey2'}, follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Invalid credentials.", html)
    
    def test_user_logout(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id
                sess[CURR_USER_KEY] = None
            
            resp = c.get('/logout', follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Register', html)

    # Test Homepage with a registered user
    def test_homepage(self):
        """Test homepage"""
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id
            
            response = c.get('/')
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('Homepage', html)
            self.assertIn('Monkey Test', html)

    # Test Search Recipes with a registered user
    def test_search_recipes(self):
        """ Test Recipes page"""
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id
            response = c.get('/recipes')
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('Recipes', html)
            self.assertIn('Monkey Test', html)

    # Test show recipe detail with a registered user
    def test_recipe_details(self):
        """ Test Recipe Deatail Page"""
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id
            response = c.get("/recipes/642373")
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('Recipe Detail', html)
            self.assertIn('Elk Sliders With Pancetta Bacon and Smoked Mozzarella', html)
            self.assertIn('Monkey Test', html)
    
    def test_user_detail_page(self):
        """ Test user detail page """
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id
            resp = c.get('/user')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Monkey Test', html)
            self.assertIn('On the Job: Pan Roasted Cauliflower From Food52', html)
    
    def test_user_detail_page_with_unauthorized_user(self):
        """ Test user detail page with unauthorized user"""
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = None
            resp = c.get('/user', follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Access unauthorized.', html)

    def test_edit_user(self):
        """ Test edit user page"""
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id
            resp = c.get('/user/edit')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Edit Your Profile', html)
    
    def test_edit_user_with_unauthorized_user(self):
        """Test user edit page with unauthorized user"""
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = None
        resp = c.get('/user/edit', follow_redirects=True)
        html = resp.get_data(as_text=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Access unauthorized', html)
    
    def test_edit_user_submit(self):
        """Test user edit form submit"""
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id
            resp = c.post('/user/edit', data = {'username':'Monkey Test One', 
                                                'email':'monkeytestone@gmail.com', 
                                                'image_url': None, 
                                                'password': 'Monkeytest'},
                                        follow_redirects=True)
            html = resp.get_data(as_text = True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Monkey Test One', html)
    
    def test_edit_user_submit_with_wrong_password(self):
        """Test user edit form submit with wrong password"""
        with self.client as c:
            with c.session_transaction() as sess:
                    sess[CURR_USER_KEY] = self.testuser.id
            resp = c.post('/user/edit', data = {'username':'Monkey Test One', 
                                                'email':'monkeytestone@gmail.com', 
                                                'image_url': None, 
                                                'password': 'Monkeytestwrong'},
                                        follow_redirects=True)
            html = resp.get_data(as_text = True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Wrong password, please try again.', html)

    def test_edit_user_with_existing_info(self):
        """Test user edit submittion with existing information"""
        user = User.register('Liam Nguyen', 'liamnguyen.swe@gmail.com', None, 'Liam0671')
        uid = 3333
        user.id = uid

        db.session.commit()

        with self.assertRaises(InvalidRequestError):
            with self.client as c:
                with c.session_transaction() as sess:
                    sess[CURR_USER_KEY] = user.id
                resp = c.post('/user/edit', data = {'username': 'Liam Nguyen', 'email':'monkeytest@gmail.com', 'image_url': None, "password":"Liam0671"}, follow_redirects=True)
                html = resp.get_data(as_text=True)
                self.assertEqual(resp.status_code, 200)
                self.assertIn('Your input is already existed, please try again', html)

    def test_user_favorite_page(self):
        """Test user favorite page that show all favorite recipes."""
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id
            resp = c.get('/user/favorites')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('On the Job: Pan Roasted Cauliflower From Food52', html)