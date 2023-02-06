from rest_framework import generics
from core.models import (
    View, Task, Project, ViewField
)
from .serializers import (
    ViewSerializer, TaskSerializer, ProjectSerializer, ViewFieldSerializer
)


class ViewListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ViewSerializer

    def get_queryset(self):
        project_id = self.kwargs.get("project_id")
        # view_id = self.request.query_params.get('view_id')
        # if view_id:
        #     return View.objects.filter(project_id=project_id)
        # print("project_id==>",project_id)
        return View.objects.filter(project_id=project_id)


class ViewRetrieveAPIView(generics.RetrieveAPIView):
    queryset = View.objects.all()
    serializer_class = ViewSerializer
    lookup_feild = 'pk'



class ViewFieldListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ViewFieldSerializer

    def get_queryset(self):
        view_id = self.kwargs.get("view_id")
        visible = self.request.query_params.get('visible')
        if visible == "1":
            return ViewField.objects.filter(view_id=view_id).filter(visible=1)

        return ViewField.objects.filter(view_id=view_id)


class ViewFieldUpdateAPIView(generics.UpdateAPIView):
    queryset = ViewField.objects.all()
    serializer_class = ViewFieldSerializer
    lookup_feild = 'pk'


class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        project_id = self.kwargs.get("project_id")
        condition = self.request.query_params.get('condition')
        if condition:
            return Task.objects.raw(f"""
                        SELECT * FROM core_task 
                        WHERE project_id = {project_id} 
                        AND ({condition}) """)

        return Task.objects.filter(project_id=project_id)

        return Task.objects.filter(
            Q(assignees='AT Tech', task_status='done') |
            Q(assignees='AT Tech', task_status='Done_and_approved'),
            project_id=project_id
        )

        


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
