from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

from .models import AboutModel, OurPartnersModel, ServicesModel, TestimonialModel, PortfolioModel, \
    TeamMembersModel, FaqModel, BlogModel, ContactModel, AwardsModel, ProjectCategoryModel, BlogCategoryModel
from .forms import ContactForm
from django.views.generic import ListView, DetailView


def home(request):
    return render(request, 'index.html')


def about(request):
    about = AboutModel.objects.first()
    context = {
        'about': about
    }

    return render(request, 'about.html', context)


def partners(request):
    partners = OurPartnersModel.objects.all()
    context = {
        'partners': partners
    }

    return render(request, 'partners.html', context)

def services(request):
    services = ServicesModel.objects.all()
    context = {
        'services': services
    }

    return render(request, 'services.html', context)

def testimonials(request):
    testimonials = TestimonialModel.objects.all()
    context = {
        'testimonials': testimonials
    }

    return render(request, 'testimonials.html', context)

def portfolio(request):
    portfolios = PortfolioModel.objects.all()
    portfolio_categories = ProjectCategoryModel.objects.all()
    context = {
        'portfolios': portfolios,
        'portfolio_categories': portfolio_categories
    }

    return render(request, 'portfolio.html', context)

def team(request):
    team = TeamMembersModel.objects.all()
    context = {
        'team': team
    }

    return render(request, 'our_team.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('OK')
        else:
            return HttpResponse('Something went wrong while submitting the form')
    about = AboutModel.objects.first()
    context = {
        'about': about
    }
    return render(request, 'contact.html', context)


def project_details(request, id):
    project = PortfolioModel.objects.get(id=id)
    recent_projects = PortfolioModel.objects.exclude(id=id).order_by('-created_at')[:3]
    categories = ProjectCategoryModel.objects.all()
    context = {
        'project': project,
        'categories': categories,
        'recent_projects': recent_projects,
    }
    return render(request, 'portfolio-details.html', context)


def custom_404(request):
    return render(request, '404.html', status=404)

