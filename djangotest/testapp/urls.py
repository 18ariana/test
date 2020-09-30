from django.urls import path
from . import views

urlpatterns = [
    path('people/', views.PeopleListView.as_view()),
    path('people_info/', views.AdminPeopleListView.as_view())
]
