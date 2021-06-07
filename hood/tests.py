from django import test
from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth

class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username = 'natasha', email = 'kinuthia@gmail.com', password = 'passwadd')
        self.user.save()
        self.kevin = Profile(bio = 'A python Programmer', user = self.user)

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.kevin,Profile))

    def test_save(self):
        Profile.objects.create()
        self.kevin.save_user_profile(self.user)
        users = Profile.objects.all()
        self.assertTrue(len(users)>0)


class HoodTest(TestCase):
    def setUp(self):
        self.user = User(username='natasha', email='natasha1594@gmail.com', password='passwadd')
        self.user.save()
        self.natasha = Profile(bio='A python Programmer', user=self.user)
        self.NeighbourHood = NeighbourHood(name = 'Ngong',bio = "Milimani",admin = self.user)

    def tearDown(self):
        Profile.objects.all().delete()
        self.NeighbourHood.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.hood,NeighbourHood))

    def test_save(self):
        self.NeighbourHood.save_hood()
        hoods = NeighbourHood.objects.all()
        self.assertTrue(len(hoods) == 1)



class PostTest(TestCase):
    def setUp(self):
        self.user = User(username='natasha1594', email='natasha1594@gmail.com', password='passwadd')
        self.user.save()
        self.kevin = Profile(bio='A python Programmer', user=self.user)
        self.NeighbourHood = NeighbourHood(name='Ngong', bio="Milimani", admin=self.user)
        self.business = Business(name="brian", owner = self.user, business_description= 'langat',
                                 locale = self.hood,business_number = 4322323)
        self.post = Post(title='Postings',post = 'This is the post',
                         hood = self.hood, poster = self.user)

    def tearDown(self):
        Profile.objects.all().delete()
        self.NeighbourHood.delete()
        self.business.delete()
        self.post.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_save(self):
        self.post.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) == 1)