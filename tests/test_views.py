from bom import create_app, db
from bom.models import Title

import unittest


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

        response = self.client.get('/')
        
        statuscode = response.status_code
        response_type = response.is_json
        response_message = response.get_json()
        
        # Check for response 200
        self.assertEqual(statuscode, 200)
        # Check if response is application/json
        self.assertEqual(response_type, True)
        # Check response content: client recieves welcom message
        self.assertEqual(response_message['message'], "Welcome to the BoxOfficeMojo CRUD App")

    def test_getTitles(self):

        response = self.client.get('/titles')
        
        statuscode = response.status_code
        response_type = response.is_json
        response_message = response.get_json()
        
        # Check for response 200
        self.assertEqual(statuscode, 200)
        # Check if response is application/json
        self.assertEqual(response_type, True)
        # Check response content: client recieves welcom message
        self.assertEqual(response_message['message'], ['Black Swan', 'The Grand Budapest Hotel', 'Scream', 'The Dark Knight', 'Drive', 'Somewhere', 'Community', 'The Bourne Identity'])

    def test_getTitle(self):

        response = self.client.get('/titles/1')
        
        statuscode = response.status_code
        response_type = response.is_json
        response_message = response.get_json()
        
        # Check for response 200
        self.assertEqual(statuscode, 200)
        # Check if response is application/json
        self.assertEqual(response_type, True)
        # Check response content: client recieves welcom message
        self.assertEqual(response_message['message'], "Black Swan")

if __name__ == '__main__':
    unittest.main()