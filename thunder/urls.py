from django.urls import path
from thunder import views
urlpatterns = [
    path('', views.homepage, name='home'),
    path('<int:member_id>', views.memberdetails, name='memberdetails'),
]
