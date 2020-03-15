# serializers.py

from rest_framework import serializers
from .models import Questionary

class QuestionarySerializer(serializers.HyperlinkedModelSerializer):
    """docstring for QuestionarySerializer."""

    class Meta:
        model = Questionary
        fields = ('cough', 'breathing_difficulties', 'throat_pain', 'fever', 'corporal_temperature',
                  'contact_risk_people', 'other_symptoms')
        
