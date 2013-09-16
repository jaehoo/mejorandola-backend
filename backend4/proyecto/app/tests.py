"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from .models import Categoria, Enlace
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class SimpleTest(TestCase):

    def setUp(self):
		self.categoria = Categoria.objects.create(titulo ='Categoria de Prueba')
		self.usuario = User.objects.create_user(username='alberto', password='test')

    def test_es_popular(self):
    	# si un enlace tiene < 11 votos no es popular
    	# > 11 es popular
		
		enlace = Enlace.objects.create(titulo='Prueba', enlace='http://mejorando.la',
		votos= 0,categoria= self.categoria, usuario = self.usuario)
		
		self.assertEqual(enlace.votos, 0)
		self.assertEqual(enlace.es_popular(), False)
		self.assertFalse(enlace.es_popular())

		enlace.votos = 20
		enlace.save()

		self.assertEqual(enlace.votos, 20)
		self.assertEqual(enlace.es_popular(), True)
		self.assertTrue(enlace.es_popular())

    def test_views(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)

        res = self.client.get(reverse('enlaces'))
        self.assertEqual(res.status_code, 200)

        res = self.client.get(reverse('about'))
        self.assertEqual(res.status_code, 200)
      
        self.assertTrue(self.client.login(username='alberto', password='test'))

        res = self.client.get(reverse('add'))
        self.assertEqual(res.status_code, 200)

    def test_add(self):
    	self.assertTrue(self.client.login(username='alberto', password='test'))
    	self.assertEqual(Enlace.objects.count(),0)
    	data = {}
        data['titulo']='Test Tilulo'
        data['enlace']='http://mejorando.la/'
        data['categoria']=self.categoria.id

        res = self.client.post(reverse('add'),data)
        self.assertEqual(res.status_code, 302)
        self.assertEqual(Enlace.objects.count(),1)
        
        enlace = Enlace.objects.all()[0]
        self.assertEqual(enlace.titulo, data['titulo'])
        self.assertEqual(enlace.enlace, data['enlace'])
        self.assertEqual(enlace.categoria, self.categoria)

        #def test_basic_addition(self):
        #"""
        #Tests that 1 + 1 always equals 2.
        #"""
        #self.assertEqual(1 + 1, 2)