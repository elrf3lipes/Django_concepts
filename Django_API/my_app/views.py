from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from rest_framework.permissions import IsAuthenticated


class TodoView(APIView):

    def post(self, request):
        data = request.data
        todo = Todo.objects.create(task=data['task'], completed=data['completed'])
        return Response({"message": "Todo created successfully"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        items = [{"task": x.task, "completed": x.completed} for x in Todo.objects.all()]
        return Response(items, status=status.HTTP_200_OK)


'''
View inherits the API view class from the django rest framework
This class has two functions: post and get, in the parameter we gave it a request object
'''


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'This is a protected view'})
