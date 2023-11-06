from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
  # We are writing this becoz we need confirm password field in our Registratin Request
  re_password = serializers.CharField(style={'input_type':'password'}, write_only=True)
  class Meta:
    model = User
    fields=['email', 'name', 'password', 're_password']
    extra_kwargs={
      'password':{'write_only':True}
    }

  # Validating Password and Confirm Password while Registration
  def validate(self, attrs):
    password = attrs.get('password')
    re_password = attrs.get('re_password')
    if password != re_password:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    return attrs

  def create(self, validate_data):
    return User.objects.create_user(**validate_data)

class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']

class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'name', 'is_staff', 'is_superuser']

class UserLogoutSerializer(serializers.Serializer):
  refresh_token = serializers.CharField()
  default_error_messages = {
    'bad_token':'Token is Expired or Invalid'
  }

  def validate(self, attrs):
    self.token = attrs.get('refresh_token')
    return attrs

  def save(self, **kwargs):
    print('Token', self.token)
    try:
      RefreshToken(self.token).blacklist()
    except:
      self.fail('bad_token')
