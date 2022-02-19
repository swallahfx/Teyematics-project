from curses.ascii import isdigit
from rest_framework.test import APITestCase


class TestFileUpload(APITestCase):
    add_comment_url = "api/v1/add/comment/"
    search_by_comment = "api/v1/search/"

    def test_addComment(self):
        # definition
    
        data = {
            'postId':3,
            'name': 'adebbbi', 
            'email':'adebbbi@gmail.com',
            'body':'my name is awesome in da lord'
        }

        # processing
        response = self.client.post(self.add_comment_url, data=data)
        result = response.json()

        # assertions
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(result["id"], 1)# Create your tests here.
        
    def test_search_by_comment(self):
        # definition
       
        data = {
    
            'search':'molesti',
            
        }

        # processing
        response = self.client.post(self.search_by_comment, data=data)
        result = response.json()

        # assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["id"], isdigit)# Create your tests here.
