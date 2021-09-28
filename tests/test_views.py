from bom import create_app, db

import unittest


class FlaskTest(unittest.TestCase):

    # Check for response 200
    def test_index_statuscode(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        client = self.app.test_client(self)

        response = client.get('/')

        statuscode = response.status_code

        self.assertEqual(statuscode, 200)

    # Check if response is application/json
    def test_index_responsetype(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        client = self.app.test_client(self)

        response = client.get('/')

        response_type = response.is_json

        self.assertEqual(response_type, True)


    # Check response content
    def test_index_responsecontent(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        client = self.app.test_client(self)

        response = client.get('/')

        response_message = response.get_json()

        self.assertEqual(response_message['message'], "Welcome to BoxOfficeMojo CRUD App")


if __name__ == '__main__':
    unittest.main()