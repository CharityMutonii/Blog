import unittest 
from app.models import Post

class test_postModel(unittest.TestCase):

    # to test behaivours in the post model

    def setUp(self):
        self.user_Me = User(firstname ='charity', secondname = 'mutoni',username = 'cm', password = 'hhh', email = 'charity@gmail.com')
        self.new_post = Post(title = 'pray', content = 'praying is important',user_id =  1, category = 'prayers',author='Me')

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.title, 'pray')
        self.assertEquals(self.new_post.content, 'praying is important' )
        self.assertEquals(self.new_post.user_id, 1)
        self.assertEquals(self.new_post.category, 'prayer')
        self.assertEquals(self.new_post.author, 'Me')

    def tearDown(self):
        Post.query.delete()
        User.query.delete()
    
    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all()),1)

    def test_delete_post(self):
        self.new_post.delete_post()
        self.assertTrue(len(Post.query.all()),0)


    




