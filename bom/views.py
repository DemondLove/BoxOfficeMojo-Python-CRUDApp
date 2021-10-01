from bom import db
from flask import Blueprint, request, jsonify, make_response, abort
from bom.models import Title

view = Blueprint('view', __name__)

# Status Code Errors
@view.errorhandler(400)
def handle_400_error(_error):
    return make_response(jsonify({'Error': 'Bad Request'}), 400)

@view.errorhandler(404)
def handle_404_error(_error):
    return make_response(jsonify({'Error': 'Endpoint Not Found'}), 404)

@view.errorhandler(405)
def handle_405_error(_error):
    return make_response(jsonify({'Error': 'Method Not Allowed'}), 405)

@view.errorhandler(422)
def handle_422_error(_error):
    return make_response(jsonify({'Error': 'Unreachable Entity'}), 422)

@view.errorhandler(500)
def handle_500_error(_error):
    return make_response(jsonify({'Error': 'Internal Server Error'}), 500)

@view.route('/', methods=['GET'])
def index():
    '''
    API root

    Returns:
        body (JSON) - {'message': 'Welcome to the BoxOfficeMojo CRUD App'}
    '''
    
    return make_response(jsonify({'message': 'Welcome to the BoxOfficeMojo CRUD App'}), 200)

@view.route('/titles', methods=['GET'])
def getTitles():
    '''
    Get all titles w/ pagination

    Returns:
        body (JSON) - {'message': 'Welcome to the BoxOfficeMojo CRUD App'}
    '''
    error = False
    body = {}

    try:
        query_results = Title.query.all()
        all_titles = [result.title for result in query_results]
        body = {'message': all_titles}
    except Exception as e:
        error = True
        print('Error Occured: ', e)

    if error:
        abort(500)
    else:
        return make_response(jsonify(body), 200)

@view.route('/titles/<int:id>', methods=['GET'])
def getTitle(id):
    '''
    Get a single title

    Parameters:
        id (int): primary key of the target

    Returns:
        body (JSON) - {'message': 'Welcome to the BoxOfficeMojo CRUD App'}
    '''
    error = False
    body = {}

    try:
        body['message'] = Title.getTitleByID(id)
    except Exception as e:
        error = True
        print('Error Occured: ', e)

    if error:
        abort(422)
    else:
        return make_response(jsonify(body), 200)

@view.route('/titles', methods=['POST'])
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

@view.route('/titles', methods=['PUT'])
def putTitles():
    '''
    Update all titles
    '''
    return {'message': 'API will update all titles'}, 200

@view.route('/titles/<id>', methods=['PUT'])
def putTitle(id):
    '''
    Update a single title
    '''
    return {'message': 'API will update {} title'.format(id)}, 200

@view.route('/titles', methods=['PATCH'])
def patchTitles():
    '''
    Partially update all titles
    '''
    return {'message': 'API will partially update all titles'}, 200

@view.route('/titles/<id>', methods=['PATCH'])
def patchTitle(id):
    '''
    Partially update a single title
    '''
    return {'message': 'API will partially update {} title'.format(id)}, 200

@view.route('/titles', methods=['DELETE'])
def deleteTitles():
    '''
    Delete all titles
    '''
    return {'message': 'API will delete all titles'}, 200

@view.route('/titles/<id>', methods=['DELETE'])
def deleteTitle(id):
    '''
    Delete a single title
    '''
    return {'message': 'API will delete {} title'.format(id)}, 200