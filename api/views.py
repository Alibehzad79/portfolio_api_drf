from django.shortcuts import render
from rest_framework.views import APIView
from account_app.models import Profile, Email
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from api.serializers import ProfileSerializer, EmailSerializer
# Create your views here.

class ProfileAPI(APIView):
    """
    View to list all profile in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    def get(self, request, format=None):
        
        profile = Profile.objects.last()
        profile_s = ProfileSerializer(profile)
        context = {
            'profile': profile_s.data,
        }
        return Response(context)

class EmailAPI(APIView):
    # authentication_classes = [authentication.UNAUTHENTICATED_TOKEN]
    permission_classes = [permissions.AllowAny]
    # def get(self, request, format=None):
    #     email = Email.objects.last()
    #     email_s = EmailSerializer(email)
    #     context = {
    #         'emails': email_s.data,
    #     }
    #     return Response(context)
    def post(self, request, format=None):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)