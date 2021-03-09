from django.urls import path


from . import views


urlpatterns = [
    path('', views.ListEcSite.as_view()),
    path('<int:pk>/', views.DetailEcSite.as_view()),
]
