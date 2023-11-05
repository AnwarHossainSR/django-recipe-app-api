from rest_framework import renderers
import json

class UserRenderer(renderers.JSONRenderer):
  charset='utf-8'
  def render(self, data, accepted_media_type=None, renderer_context=None):
    response = ''
    if 'ErrorDetail' in str(data):
      # if data['code'] == 'token_not_valid':
      #   response = json.dumps({'errors':data['messages']})
      # else:
      #   response = json.dumps({'errors':data})
      response = json.dumps({'errors':data})
    else:
      response = json.dumps(data)
    
    return response