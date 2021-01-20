from django.test import TestCase
from django.contrib.auth.models import User
from .models import Users

# Create your tests here.

class UserCreation(TestCase):
    def setUp(self):
        users = User.objects.all()
        for i in users:
            user = User.objects.create_user(username=i.username,email=i.email,password=i.password)

    def test(self):
        print("ok")
            