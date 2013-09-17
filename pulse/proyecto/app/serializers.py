from rest_framework import serializers

from .models import Enlace

class EnlaceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Enlace
		fields = ('titulo','enlace','votos',
			'usuario','timestamp',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Enlace
		fields = ('titulo','enlace','votos',
			'usuario','timestamp',)


