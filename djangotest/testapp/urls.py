from django.urls import path
from . import views

urlpatterns = [
    path('people/', views.PeopleListView.as_view()),
    path('people/', views.AdminPeopleListView.as_view())
]
