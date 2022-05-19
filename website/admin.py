from django.contrib import admin
from .models import User, Skills, Services, Contact, Faqs, Reviews, Projects, Blog

# Register your models here.
admin.site.register(User)
admin.site.register(Skills)
admin.site.register(Services)
admin.site.register(Contact)
admin.site.register(Faqs)
admin.site.register(Reviews)
admin.site.register(Projects)
admin.site.register(Blog)