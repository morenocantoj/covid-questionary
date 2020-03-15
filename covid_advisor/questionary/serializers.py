# serializers.py

from rest_framework import serializers
from .models import Questionary, PersonalInfo

class PersonalInfoSerializer(serializers.HyperlinkedModelSerializer):
    """docstring for PersonalInfoSerializer"""

    class Meta:
        model = PersonalInfo
        fields = ('name', 'surname', 'age', 'phone', 'email')

class QuestionarySerializer(serializers.HyperlinkedModelSerializer):
    """docstring for QuestionarySerializer."""
    personal_info = PersonalInfoSerializer(required=True)

    class Meta:
        model = Questionary
        fields = ('cough', 'breathing_difficulties', 'throat_pain', 'fever', 'corporal_temperature',
                  'contact_risk_people', 'other_symptoms', 'personal_info')

    def create(self, validated_data):
        """
        Overriding the default crate method of the Model serializer
        :param validated_data: data containing all the details of the questionary
        """
        personal_info_data = validated_data.pop('personal_info')
        personal_info = PersonalInfoSerializer.create(PersonalInfoSerializer(), validated_data=personal_info_data)
        questionary, created = Questionary.objects.update_or_create(validated_data, personal_info=personal_info)
        return questionary
