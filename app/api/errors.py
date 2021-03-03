from . import api



@api.app_errorhandler(400)
def bad_request(err):
    return ('bad request',400)

@api.app_errorhandler(404)
def not_found(err):
    return ('internal server error',500)

@api.app_errorhandler(500)
def internal_server_error(err):
    return ('internal server error',500)

