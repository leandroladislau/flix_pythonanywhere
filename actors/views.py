from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalPermissionClass

class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)

class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)