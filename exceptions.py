from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.exceptions import TokenError

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    code = ''

    if response is not None:
        if 'code' in response.data:
            code = response.data['code']
        elif 'detail' in response.data:
            code = response.data['detail'].code
        else:
            code = ''


    print('Code============', code)
    if code and code != '':
        if code == 'token_not_valid':
            custom_response_data = {
                'error': 'Token has expired or is invalid.'
            }
            response.data = custom_response_data
            response.status_code = status.HTTP_401_UNAUTHORIZED
        elif code == 'authentication_failed':
            custom_response_data = {
                'error': 'Authentication failed.'
            }
            response.data = custom_response_data
            response.status_code = status.HTTP_401_UNAUTHORIZED
        elif code == 'not_authenticated':
            custom_response_data = {
                'error': 'Not authenticated.'
            }
            response.data = custom_response_data
            response.status_code = status.HTTP_401_UNAUTHORIZED
        elif code == 'permission_denied':
            custom_response_data = {
                'error': 'Permission denied.'
            }
            response.data = custom_response_data
            response.status_code = status.HTTP_401_UNAUTHORIZED
        elif code == 'server_error':
            custom_response_data = {
                'error': 'Server error.'
            }
            response.data = custom_response_data
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        elif code == 'not_found':
            custom_response_data = {
                'error': 'Requested resource is not found'
            }
            response.data = custom_response_data
            response.status_code = status.HTTP_404_NOT_FOUND
        elif code == 'method_not_allowed':
            custom_response_data = {
                'error': 'Method not allowed.'
            }
            response.data = custom_response_data
            response.status_code = status.HTTP_405_METHOD_NOT_ALLOWED    
    else:
        custom_response_data = {
            'error': 'Method not allowed.'
        }
        response.data = custom_response_data
        response.status_code = status.HTTP_405_METHOD_NOT_ALLOWED  

    return response
