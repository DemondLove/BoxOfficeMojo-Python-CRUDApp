from bom import db
from flask import Blueprint, request, jsonify, make_response, abort, url_for
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
        
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 8, type=int)
        paginate = Title.query.paginate(page=page, per_page=limit, error_out=False)
        paginated_titles = [{'id': result.id, 'title': result.title} for result in paginate.items]
        
        prev_url = None
        if paginate.has_prev:
            prev_url = url_for('view.getTitles', page=page-1)

        next_url = None
        if paginate.has_next:
            next_url = url_for('view.getTitles', page=page+1)

        body = {'titles': paginated_titles
                , 'prev_url': prev_url
                , 'next_url': next_url
                , 'count': paginate.total
               }
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

@view.route('/titles/<int:id>', methods=['PUT'])
def putTitle(id):
    '''
    Update a single title

    Params:
        id (int): primary key of the target

    Returns:
        body (JSON) - {'id': <id>, 'title': '<title>'}
    '''
    error = False
    body = {}
    return_status = 500

    try:
        if request.is_json:
            input_request = request.get_json()
            
            request_title = Title.query.get(id)

            if request_title:
                request_title.title = input_request['title']
                return_status = 200
            else:
                request_title = Title(title=input_request['title'])
                db.session.add(request_title)
                return_status = 201

            
            db.session.commit()

            body['title'] = request_title.title
            body['id'] = request_title.id
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
        return make_response(jsonify(body), return_status)

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