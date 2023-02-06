from django.urls import path   
from . import views



urlpatterns = [
    path("project/", views.ProjectListCreateAPIView.as_view(), name = "v1/core-project"),

    path("task/<int:project_id>", views.TaskListCreateAPIView.as_view(), name = "v1/core-task"),
    path("view/<int:project_id>", views.ViewListCreateAPIView.as_view(), name = "v1/core-view"),
    path("view-retrive/<int:pk>", views.ViewRetrieveAPIView.as_view(), name = "v1/core-view-retrive"),
    path("view-field/<int:view_id>", views.ViewFieldListCreateAPIView.as_view(), name = "v1/core-view-field"),

    path("view-field/update/<int:pk>", views.ViewFieldUpdateAPIView.as_view(), name = "v1/core-view-field-update"),

    # ViewFieldUpdateAPIView
]