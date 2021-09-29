from bom import create_app, db
from bom.models import Title

import unittest


class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        title = Title(title='Black Swan')
        db.session.add(title)
        db.session.commit()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # Check for response 200
    def test_index_statuscode(self):

        response = self.client.get('/')

        statuscode = response.status_code

        self.assertEqual(statuscode, 200)

    # Check if response is application/json
    def test_index_responsetype(self):

        response = self.client.get('/')

        response_type = response.is_json

        self.assertEqual(response_type, True)


    # Check response content
    def test_index_responsecontent(self):
        response = self.client.get('/')

        response_message = response.get_json()

        self.assertEqual(response_message['message'], "Welcome to the BoxOfficeMojo CRUD App")


if __name__ == '__main__':
    unittest.main()