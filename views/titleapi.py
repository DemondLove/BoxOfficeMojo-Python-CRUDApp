from views import app
from flask import request, jsonify, make_response


@app.route('/', methods=['GET'])
def index():
    '''
    API root
    '''
    return {'message': 'Welcome to BoxOfficeMojo CRUD App'}, 200


@app.route('/titles', methods=['GET'])
def getTitles():
    '''
    Get all titles w/ pagination
    '''
    return {'message': 'API will return all titles'}, 200


@app.route('/titles/<id>', methods=['GET'])
def getTitle(id):
    '''
    Get a single title
    '''
    return {'message': 'API will return {} title'.format(id)}, 200


@app.route('/titles', methods=['POST'])
def postTitles():
    '''
    Create a new title
    '''
    if request.is_json:
        input_request = request.get_json()

    response = {
        "message": "API will create new title"
    }
    return make_response(jsonify(response), 200)


@app.route('/titles', methods=['PUT'])
def putTitles():
    '''
    Update all titles
    '''
    return {'message': 'API will update all titles'}, 200


@app.route('/titles/<id>', methods=['PUT'])
def putTitle(id):
    '''
    Update a single title
    '''
    return {'message': 'API will update {} title'.format(id)}, 200


@app.route('/titles', methods=['PATCH'])
def patchTitles():
    '''
    Partially update all titles
    '''
    return {'message': 'API will partially update all titles'}, 200


@app.route('/titles/<id>', methods=['PATCH'])
def patchTitle(id):
    '''
    Partially update a single title
    '''
    return {'message': 'API will partially update {} title'.format(id)}, 200


@app.route('/titles', methods=['DELETE'])
def deleteTitles():
    '''
    Delete all titles
    '''
    return {'message': 'API will delete all titles'}, 200


@app.route('/titles/<id>', methods=['DELETE'])
def deleteTitle(id):
    '''
    Delete a single title
    '''
    return {'message': 'API will delete {} title'.format(id)}, 200