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

@app.route('/titles/<name>', methods=['GET'])
def getTitle(name):
    '''
    Get a single title
    '''
    return {'message': 'API will return {} title'.format(name)}, 200

@app.route('/titles', methods=['POST'])
def postTitles():
    '''
    Create a new title
    '''
    return {'message': 'API will create new title'}, 200

@app.route('/titles', methods=['PUT'])
def putTitles():
    '''
    Update all titles
    '''
    return {'message': 'API will update all titles'}, 200

@app.route('/titles/<name>', methods=['PUT'])
def putTitle(name):
    '''
    Update a single title
    '''
    return {'message': 'API will update {} title'.format(name)}, 200

@app.route('/titles', methods=['PATCH'])
def patchTitles():
    '''
    Partially update all titles
    '''
    return {'message': 'API will partially update all titles'}, 200

@app.route('/titles/<name>', methods=['PATCH'])
def patchTitle(name):
    '''
    Partially update a single title
    '''
    return {'message': 'API will partially update {} title'.format(name)}, 200

@app.route('/titles', methods=['DELETE'])
def deleteTitles():
    '''
    Delete all titles
    '''
    return {'message': 'API will delete all titles'}, 200

@app.route('/titles/<name>', methods=['DELETE'])
def deleteTitle(name):
    '''
    Delete a single title
    '''
    return {'message': 'API will delete {} title'.format(name)}, 200