import unittest 
from app.models import User

class test_userModel(unittest.TestCase):

    # to test behaivours in the user model

    def setUp(self):
        self.new_user = User(password='mypass')

    def test_setPassword(self):
        # to test if there is a password
        self.assertTrue(self.new_user.password is not None)
    def  test_check_password(self):
        
        self.assertTrue(self.new_user.check_password('mypass'))

    def test_save_user(self):

        self.user_Me = User( firstname = 'charity' ,secondname = 'Mutoni',username = 'cm', password = 'charity', email = 'charity@gmail.com')
        self.user_Me.save()
        self.assertTrue(len(User.query.all()),1)

    def test_delete_user(self):
        self.user_Me = User( firstname = 'charity' ,secondname = 'Mutoni',username = 'cm', password = 'charity', email = 'charity@gmail.com')
        self.user_Me.save()
        self.me = User(firstname='chch',secondname='mumu',username='muto',password='hhh',email='charity6@gmail.com')
        self.me.save()
        self.me.delete()
        self.assertTrue(len(User.query.all()),1)
    




