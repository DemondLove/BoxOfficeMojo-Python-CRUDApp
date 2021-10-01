from bom import create_app, db
from bom.models import Title
import unittest, json


class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        
        db.create_all()
        black_swan = Title(title='Black Swan')
        grand_budapest = Title(title='The Grand Budapest Hotel')
        scream = Title(title='Scream')
        dark_knight = Title(title='The Dark Knight')
        drive = Title(title='Drive')
        somewhere = Title(title='Somewhere')
        community = Title(title='Community')
        bourne_identity = Title(title='The Bourne Identity')
        db.session.add_all([black_swan, grand_budapest, scream, dark_knight, drive, somewhere, community, bourne_identity])
        db.session.commit()
        
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_index(self):
        response = self.client.get('/api/v1/')
        
        statuscode = response.status_code
        response_type = response.is_json
        response_message = response.get_json()
        
        # Check for response 200
        self.assertEqual(statuscode, 200)
        # Check if response is application/json
        self.assertEqual(response_type, True)
        # Check response content: client recieves welcome message
        self.assertEqual(response_message['message'], "Welcome to the BoxOfficeMojo CRUD App")

    def test_getTitles(self):
        response = self.client.get('/api/v1/titles')
        
        statuscode = response.status_code
        response_type = response.is_json
        response_message = response.get_json()
        
        # Check for response 200
        self.assertEqual(statuscode, 200)
        # Check if response is application/json
        self.assertEqual(response_type, True)
        # Check response content: client recieves all ids and titles
        self.assertEqual(response_message['titles'], [{'id': 1, 'title': 'Black Swan'}
                                                      ,{'id': 2, 'title': 'The Grand Budapest Hotel'}
                                                      ,{'id': 3, 'title': 'Scream'}
                                                      ,{'id': 4, 'title': 'The Dark Knight'}
                                                      ,{'id': 5, 'title': 'Drive'}
                                                      ,{'id': 6, 'title': 'Somewhere'}
                                                      ,{'id': 7, 'title': 'Community'}
                                                      ,{'id': 8, 'title': 'The Bourne Identity'}])

    def test_getTitle(self):
        response = self.client.get('/api/v1/titles/1')
        
        statuscode = response.status_code
        response_type = response.is_json
        response_message = response.get_json()
        
        # Check for response 200
        self.assertEqual(statuscode, 200)
        # Check if response is application/json
        self.assertEqual(response_type, True)
        # Check response content: client recieves id and title
        self.assertEqual(response_message['title'], 'Black Swan')
        self.assertEqual(response_message['id'], 1)


    def test_postTitles(self):
        response = self.client.post('/api/v1/titles'
                                   , headers={'Content-Type': 'application/json'}
                                   , data=json.dumps({'title': 'Rick and Morty'}))
        
        statuscode = response.status_code
        response_type = response.is_json
        response_message = response.get_json()

        # Check for response 201
        self.assertEqual(statuscode, 201)
        # Check if response is application/json
        self.assertEqual(response_type, True)
        # Check response content: client recieves id and title
        self.assertEqual(response_message['title'], 'Rick and Morty')
        self.assertEqual(response_message['id'], 9)

        response = self.client.get('/api/v1/titles/9')
        
        response_message = response.get_json()
        
        # Check response content: client recieves id and title
        self.assertEqual(response_message['title'], 'Rick and Morty')
        self.assertEqual(response_message['id'], 9)

    def test_putTitle(self):
        response = self.client.put('/api/v1/titles/14'
                                   , headers={'Content-Type': 'application/json'}
                                   , data=json.dumps({'title': 'A Clockwork Orange'}))
        
        statuscode = response.status_code
        response_type = response.is_json
        response_message = response.get_json()

        # Check for response 201
        self.assertEqual(statuscode, 201)
        # Check if response is application/json
        self.assertEqual(response_type, True)
        # Check response content: client recieves id and title
        self.assertEqual(response_message['title'], 'A Clockwork Orange')
        self.assertEqual(response_message['id'], 9)

        response = self.client.put('/api/v1/titles/9'
                                   , headers={'Content-Type': 'application/json'}
                                   , data=json.dumps({'title': '2001: A Space Odyssey'}))
        
        statuscode = response.status_code
        response_type = response.is_json
        response_message = response.get_json()

        # Check for response 200
        self.assertEqual(statuscode, 200)
        # Check if response is application/json
        self.assertEqual(response_type, True)
        # Check response content: client recieves id and title
        self.assertEqual(response_message['title'], '2001: A Space Odyssey')
        self.assertEqual(response_message['id'], 9)

    def test_deleteTitle(self):
        response = self.client.delete('/api/v1/titles/1')
        
        statuscode = response.status_code

        # Check for response 204
        self.assertEqual(statuscode, 204)

        response = self.client.get('/api/v1/titles/1')

        statuscode = response.status_code

        # Check for response 422
        self.assertEqual(statuscode, 422)


if __name__ == '__main__':
    unittest.main()