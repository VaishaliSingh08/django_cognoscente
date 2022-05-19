from django.urls import path
from dashboard import views
from cognoscente import settings
from django.conf.urls.static import static


urlpatterns = [

    path('dashboard', views.dashboard, name='dashboard'),
    path('queries', views.queries, name='queries'),
    path('view_query/<int:id>', views.view_query, name='view_query'),
    path('delete_query', views.delete_query, name='delete_query'),
    path('delete_skill/<int:id>', views.delete_skill, name='delete_skill'),
    path('dash_services', views.dash_services, name='dash_services'),
    path('edit_services/<int:id>', views.edit_services, name='edit_services'),
    path('dash_skills', views.dash_skills, name='dash_skills'),
    path('edit_skills/<int:id>', views.edit_skills, name='edit_skills'),
    path('add_skill', views.add_skill, name='add_skill'),
    path('dash_faqs', views.dash_faqs, name='dash_faqs'),
    path('dash_reviews', views.dash_reviews, name='dash_reviews'),
    path('edit_reviews/<int:id>', views.edit_reviews, name='edit_reviews'),
    path('add_review', views.add_review, name='add_review'),
    path('delete_review/<int:id>', views.delete_review, name='delete_review'),
    path('dash_projects', views.dash_projects, name='dash_projects'),
    path('add_project', views.add_project, name='add_project'),
    path('delete_project/<int:id>', views.delete_project, name='delete_project'),
    path('edit_project/<int:id>', views.edit_project, name='edit_project'),
    path('dash_blogs', views.dash_blogs, name='dash_blogs'),
    path('add_blog', views.add_blog, name='add_blog'),
    path('edit_blog/<int:id>', views.edit_blog, name='edit_blog'),
    path('delete_blog/<int:id>', views.delete_blog, name='delete_blog'),
    path('logout', views.logout, name='logout'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

##attached media folder
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)