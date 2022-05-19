from django.db.models import Q
from .models import User

def check_user_exist(username, password):
    object_values = User.objects.filter(username=username, password=password)
    print(object_values)
    return object_values
