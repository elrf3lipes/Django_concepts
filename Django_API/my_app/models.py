from django.db import models


class Todo(models.Model):
    task = models.CharField(max_length=200, blank=True, default='')
    completed = models.BooleanField(default=False)


'''
Django applications access and manage data through python objects, which are models.
Models define the structure of the stored data.
Here I created one module "todo" which has the task to tell us if its completed or not.
To test the model, run the following command from terminal:

curl -X POST -d task="learn django" -d completed=True http://127.0.0.1:8000/todo

curl -X GET localhost:8000/todo

all credits to: watch?v=newaz3DA6e4&t=297s
'''