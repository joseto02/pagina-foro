from django.shortcuts import render
from django_user_agents.utils import get_user_agent

# Create your views here.

def index(request):
    context = {}
    user_agent = get_user_agent(request)
    
    if user_agent.is_mobile:
        print("estoy en un celular")
    elif user_agent.is_pc:
        print("Estoy en una pc")
    return render(request, 'app/index.html', context)