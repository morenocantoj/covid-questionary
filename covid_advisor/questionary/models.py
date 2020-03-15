from django.db import models

class Questionary(models.Model):
    """docstring for Questionary."""

    cough = models.BooleanField()
    breathing_difficulties = models.BooleanField()
    throat_pain = models.BooleanField()
    fever = models.BooleanField()
    corporal_temperature = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    contact_risk_people = models.BooleanField()
    other_symptoms = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return print(f'Cough: {self.cough} - Breathing difficulties: {self.breathing_difficulties}, Throat pain: {self.throat_pain}, Fever: {self.fever}')
