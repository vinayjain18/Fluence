from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import ContentGeneration
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main import generate_response
import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from bs4 import BeautifulSoup
import asyncio

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    return render(request, 'index.html')

def signin(request):
    return render(request, 'signin.html')

def logout_view(request):
    logout(request)
    return redirect("/")

@login_required(login_url='/signin/')
def dashboard(request):
    if request.method == "POST":
        ig_username = request.POST.get("ig_username")
        industry = request.POST.get("industry")
        niche = request.POST.get("niche")
        about_ig_page = request.POST.get("about_ig_page")
        weeks = request.POST.get("weeks")
        response = asyncio.run(generate_response(ig_username, industry, niche, about_ig_page, weeks))
        # response = generate_response(ig_username, industry, niche, about_ig_page, weeks)
        if response.startswith("```html") and response.endswith("```"):
            response = response[7:-3]  # Remove the leading and trailing markdown code blocks
        messages.success(request, "Content plan generated successfully")
        input_context = f"IG Username: {ig_username}\nIndustry: {industry}\nNiche: {niche}\nAbout IG Page: {about_ig_page}\nWeeks: {weeks}"
        ContentGeneration.objects.create(email=request.user.email, input_context=input_context, content_output=response).save()
        return render(request, 'dashboard.html', {'response': response})
    
    return render(request, 'dashboard.html')

@login_required(login_url='/signin/')
def history(request):
    content_generations = ContentGeneration.objects.filter(email=request.user.email).order_by('-datetime')
    return render(request, 'history.html', {'content_generations': content_generations})

@login_required(login_url='/signin/')
def download_content(request, content_id):
    content_generation = get_object_or_404(ContentGeneration, pk=content_id)
    content_html = content_generation.content_output

    # Use BeautifulSoup to strip HTML tags
    soup = BeautifulSoup(content_html, "html.parser")
    clean_text = soup.get_text()
    response = HttpResponse(clean_text, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="content_{content_id}_{content_generation.email}.txt"'
    return response

@login_required(login_url='/signin/')
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('/dashboard/')
    user_details = User.objects.all().order_by('-date_joined')
    return render(request, 'admin.html', {'user_details': user_details})