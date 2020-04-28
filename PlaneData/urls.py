from django.urls import path
from . import views

urlpatterns = [
    path('', views.UpdateWaypoint.as_view()),
    path('<int:pk>',views.DeleteWaypoint.as_view()),
]
