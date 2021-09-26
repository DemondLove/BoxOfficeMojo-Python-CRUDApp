from views import app
import unittest


class FlaskTest(unittest.TestCase):

    # Check for response 200
    def test_index_statuscode(self):
        client = app.test_client(self)

        response = client.get('/')

        statuscode = response.status_code

        self.assertEqual(statuscode, 200)

    # Check if response is application/json
    def test_index_responsetype(self):
        client = app.test_client(self)

        response = client.get('/')

        response_type = response.is_json

        self.assertEqual(response_type, True)


    # Check response content
    def test_index_responsecontent(self):
        client = app.test_client(self)

        response = client.get('/')

        response_message = response.get_json()

        self.assertEqual(response_message['message'], "Welcome to BoxOfficeMojo CRUD App")


if __name__ == '__main__':
    unittest.main()