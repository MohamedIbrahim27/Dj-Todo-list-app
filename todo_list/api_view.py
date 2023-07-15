from.models import Task
from.serializer import TaskSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView

# this is api decomation
# http://127.0.0.1:6589/api-documentation/



class TaskAPiList(ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class = TaskSerializers
    permission_classes = [IsAuthenticated]


class TaskAPiDetail(RetrieveUpdateDestroyAPIView):
    queryset=Task.objects.all()
    serializer_class = TaskSerializers
    permission_classes = [IsAuthenticated]