from rest_framework import renderers
import json


class CustomRenderer(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = {}

        # Check if data is an error response
        if 'ErrorDetail' in str(data):
            response_data['errors'] = data
        else:
            # Check if data is a list or dict and null or empty
            if data is None or (isinstance(data, list) or isinstance(data, dict)) and not data:
                response_data['message'] = 'No data found'
            else:
                response_data['data'] = data

        response = json.dumps(response_data)
        return response


# from rest_framework import renderers
# import json


# class CustomRenderer(renderers.JSONRenderer):
#     charset = 'utf-8'

#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         response = ''
#         if 'ErrorDetail' in str(data):
#             # if data['code'] == 'token_not_valid':
#             #   response = json.dumps({'errors':data['messages']})
#             # else:
#             #   response = json.dumps({'errors':data})
#             response = json.dumps({'errors': data})
#         else:
#             # check if data is a list object and null or empty
#             if isinstance(data, list) and not data:
#                 response = json.dumps({'message': 'No data found'})
#             else:
#                 response = json.dumps({'data': data})

#             # check if data is a dict object and null or empty
#             if isinstance(data, dict) and not data:
#                 response = json.dumps({'message': 'No data found'})
#             else:
#                 response = json.dumps({'data': data})

#         return response
