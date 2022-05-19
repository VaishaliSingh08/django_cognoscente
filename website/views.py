from django.shortcuts import render, redirect
from .models import Contact, Skills, Services, Faqs, Reviews, Projects, Blog
from website import utilities as utl
from django.http import HttpResponse
import datetime
from django.core.files.storage import FileSystemStorage


# Create your views here.
### Home Page ###
def home(request):
    active = "home"
    skills = Skills.objects.all()
    services = Services.objects.all()
    reviews = Reviews.objects.all()
    projects = Projects.objects.all()
    blogs = Blog.objects.all()
    faqs = Faqs.objects.filter(f_id_pk=1).values()
    data ={"skills": skills, 'services':services, 'reviews':reviews, 'active':active,'blogs':blogs,
                   'faqs': faqs, 'projects':projects}
    return render(request,'home/index.html',  data)

def about(request):
    active = "about"
    skills = Skills.objects.all()
    reviews = Reviews.objects.all()
    faqs = Faqs.objects.filter(f_id_pk=1).values()
    data = {'active':active, 'skills':skills, 'reviews':reviews, 'faqs':faqs}
    return render(request,'home/about.html', data)

def services(request):
    active = "services"
    ser = Services.objects.all()
    return render(request,'home/pricing.html', {'active':active, 'ser':ser})

def projects(request):
    active = "projects"
    projects = Projects.objects.all()
    data = {'projects':projects, 'active':active}
    return render(request,'home/portfolio.html', data)

def project_desc(request, id):
    project = Projects.objects.filter(p_id_pk=id).values()
    return render(request,'home/portfolio-single.html', {'project':project[0]})

def blog(request):
    active = "blog"
    services = Services.objects.all()
    blogs = Blog.objects.all()
    data = {'services':services, 'active':active, 'blogs':blogs}
    return render(request,'home/blog.html', data)

def blog_desc(request, id):
    blogs = Blog.objects.all()
    blog_des = Blog.objects.filter(b_id_pk=id).values()

    return render(request,'home/blog-single.html', {'blogs':blogs, 'blog_des':blog_des[0]} )

def contact(request):
    active = "contact"
    if request.method == 'POST' or  request.FILES.getlist('img'):
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        code = request.POST['tele-hidden']
        contact_number = request.POST['contact_number']
        budget = request.POST['budget']
        date = datetime.datetime.now()
        date = date.strftime("%d/%m/%Y")

        attachment = request.FILES.getlist('img')
        attachments = []
        print(attachment)
        for i in attachment:
            fs = FileSystemStorage(location='media/queries/')
            filename_1 = fs.save(i.name, i)
            f_name_1 = 'queries/' + filename_1
            uploaded_file_urls = fs.url(f_name_1)
            print(uploaded_file_urls)
            attachments.append(uploaded_file_urls)


        print(attachments)
        contact_deets = Contact.objects.create(name=name, email=email, subject= subject, message=message, countrycode= code,  contact_number=contact_number, budget= budget, attachment= attachments, date= date, read_status='false')
        contact_deets.save()

    return render(request,'home/contact.html', {'active':active})


def webDevelopment(request):
    web_dev = Services.objects.filter(ser_id_pk=5).values()
    data = {'web_dev':web_dev[0]}
    return render(request, 'home/web_Development.html',data)

def digitalProducts(request):
    dg_prods = Services.objects.filter(ser_id_pk=1).values()
    data = {'dg_prods': dg_prods[0]}
    return render(request, 'home/digitalProducts.html', data)

def ux_ui_design(request):
    ui_ux = Services.objects.filter(ser_id_pk=6).values()
    data = {'ui_ux':ui_ux[0]}
    return render(request, 'home/ux_ui_design.html',data)

def applicationDevelopment(request):
    app_dev = Services.objects.filter(ser_id_pk=4).values()
    data = {'app_dev':app_dev[0]}
    return render(request, 'home/applicationDEvelopment.html',data)

def softwareSolutions(request):
    software_sol = Services.objects.filter(ser_id_pk=3).values()
    data = {'software_sol':software_sol[0]}
    return render(request, 'home/softwareSolutions.html',data)

def onlineMarketing(request):
    online_marketing = Services.objects.filter(ser_id_pk=2).values()
    data = {'online_marketing':online_marketing[0]}
    return render(request, 'home/onlineMarketing.html', data)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_valid = utl.check_user_exist(username, password)
        if user_valid:
            request.session['username'] = username
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')

def index(request):
    print(request.session['username'])
    if request.session['username']:
        return render(request, 'dashboard/index.html')
    else:
        return HttpResponse("404")


