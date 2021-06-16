from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name="adminDashboard"),
    path('course/add', views.add_course, name="add_course"),
    path('department/add', views.add_department, name="add_department"),
    path('department/edit/<int:id>', views.edit_department, name="edit_department"),
    path('department/delete/<int:id>',
         views.delete_department, name="delete_department"),
]
