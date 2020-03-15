from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import QuestionarySerializer
from .models import Questionary

class QuestionaryList(APIView):
    """
    List all questionaries, or create a new questionary
    """
    def post(self, request, format=None):
        serializer = QuestionarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
