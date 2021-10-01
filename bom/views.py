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
        body (JSON) - {'titles': [{'id': <id>, 'title': <title>}, {'id': <id>, 'title': <title>}, ...]}
    '''
    error = False
    body = {}

    try:
        query_results = Title.query.all()
        all_titles = [{'id': result.id, 'title': result.title} for result in query_results]
        body = {'titles': all_titles}
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
        body (JSON) - {'id': <id>, 'title': '<title>'}
    '''
    error = False
    body = {}

    try:
        body['title'] = Title.getTitleByID(id)
        body['id'] = id
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

    Returns:
        body (JSON) - {'id': <id>, 'title': '<title>'}
    '''
    error = False
    body = {}

    try:
        if request.is_json:
            input_request = request.get_json()
            
            input_title = Title(title=input_request['title'])
            db.session.add(input_title)
            db.session.commit()

            body['title'] = input_title.title
            body['id'] = input_title.id
        else:
            abort(400)
    except Exception as e:
        error = True
        print('Error Occured: ', e)
    finally:
        db.session.close()

    if error:
        abort(422)
    else:
        return make_response(jsonify(body), 201)

@view.route('/titles/<id>', methods=['PUT'])
def putTitle(id):
    '''
    Update a single title
    '''
    return {'message': 'API will update {} title'.format(id)}, 200


@view.route('/titles/<id>', methods=['PATCH'])
def patchTitle(id):
    '''
    Partially update a single title
    '''
    return {'message': 'API will partially update {} title'.format(id)}, 200

@view.route('/titles/<int:id>', methods=['DELETE'])
def deleteTitle(id):
    '''
    Delete a single title

    Parameters:
        id (int): primary key of the target
    '''
    error = False
    body = {}

    try:
        input_title = Title.query.get(id)
        db.session.delete(input_title)
        db.session.commit()
        body['message'] = 'Resource Successsfully Deleted'
    except Exception as e:
        error = True
        print('Error Occured: ', e)
    finally:
        db.session.close()

    if error:
        abort(422)
    else:
        return make_response(jsonify(body), 204)