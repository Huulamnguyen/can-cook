"""User View tests."""
from unittest import TestCase
from models import db, User
from app import create_app, CURR_USER_KEY

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
    
    def test_user_detail_page_with_unauthorized_user(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = None
            resp = c.get('/user', follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Access unauthorized.', html)