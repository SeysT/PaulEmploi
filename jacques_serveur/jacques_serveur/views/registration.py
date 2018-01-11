from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.http import require_POST

from rest_framework import status
from rest_framework.response import Response


@require_POST
def register(request):
   body = request.POST
   try:
       email = body['email']
       password = body['password']
   except MultiValueDictKeyError:
       return Response(
           {'detail': 'You must provide an email and a password.'},
           status=status.HTTP_400_BAD_REQUEST
       )
   try:
       user = User.objects.create_user(username=email, email=email, password=password)
   except IntegrityError:
       return Response(
           {'detail': 'An account with this email already exists.'},
           status=status.HTTP_400_BAD_REQUEST
       )
   return Response({'result': 'Success'})
