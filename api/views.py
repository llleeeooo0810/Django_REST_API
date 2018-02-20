from django.shortcuts import render
from rest_framework import generics
from api.serializers import UserSerializer
from api.forms import newUser
from api.models import User
from django.contrib import messages

class CreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def index(request):
    return render(request, 'api/index.html')

def register(request):
    form = newUser()

    if request.method == "POST":
        form = newUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'USER RESGISTERED!')
            return render(request, "api/user.html", {'form':form, })
        else:
            messages.error(request, '')

    return render(request, "api/user.html", {'form':form, })

    
