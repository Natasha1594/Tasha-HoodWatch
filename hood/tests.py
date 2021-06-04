from django.test import TestCase
from .models import NeighbourHood, Profile, Business, Post
from django.contrib.auth.models import User

class ProfileTest(TestCase):
    def setUp(self):
        self.dorcas = User(username = 'Natasha',email = 'kinuthianatasha@gmail.com')
        self.dorcas = Profile(user = Self.dorcas,user = 1,Bio = 'tests',photo = 'test.jpg',date_craeted='dec,01.2020')