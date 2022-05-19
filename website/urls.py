from django.urls import path
from website import views
from cognoscente import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('projects', views.projects, name='projects'),
    path('project_desc/<int:id>', views.project_desc, name='project_desc'),
    path('blog', views.blog, name='blog'),
    path('blog_desc/<int:id>', views.blog_desc, name='blog_desc'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('webDevelopment', views.webDevelopment, name='webDevelopment'),
    path('digitalProducts', views.digitalProducts, name='digitalProducts'),
    path('ux_ui_design', views.ux_ui_design, name='ux_ui_design'),
    path('applicationDevelopment', views.applicationDevelopment, name='applicationDevelopment'),
    path('softwareSolutions', views.softwareSolutions, name='softwareSolutions'),
    path('onlineMarketing', views.onlineMarketing, name='onlineMarketing'),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)