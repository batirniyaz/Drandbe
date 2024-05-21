from django.urls import path
from app.views import home, project_details, custom_404, about, partners, services, testimonials, \
    portfolio, team, contact

urlpatterns = [
    path('', home, name='home'),
    path('portfolio-details/<int:id>/', project_details, name='project_details'),

    path('about/', about, name='about'),
    path('partners/', partners, name='partners'),
    path('services/', services, name='services'),
    path('testimonials/', testimonials, name='testimonials'),
    path('portfolio/', portfolio, name='portfolio'),
    path('team/', team, name='team'),
    path('contact/', contact, name='contact'),


    path('404/', custom_404, name='404'),
]
