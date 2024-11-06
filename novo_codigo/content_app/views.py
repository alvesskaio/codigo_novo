from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Member
from .serializers import MemberSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)