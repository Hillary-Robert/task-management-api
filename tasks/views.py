from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner
from django.utils import timezone


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsOwner]

    filterset_fields = ["status", "priority", "due_date"]
    ordering_fields = ["due_date", "priority", "created_at"]
    ordering = ["due_date"]

    def get_queryset(self):
        
        return Task.objects.filter(user=self.request.user).order_by(*self.ordering)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["post"])
    def complete(self, request, pk=None):
        task = self.get_object()
        task.status = Task.Status.COMPLETED
        task.completed_at = timezone.now()
        task.save(update_fields=["status", "completed_at", "updated_at"])
        return Response(self.get_serializer(task).data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def incomplete(self, request, pk=None):
        task = self.get_object()
        task.status = Task.Status.PENDING
        task.completed_at = None
        task.save(update_fields=["status", "completed_at", "updated_at"])
        return Response(self.get_serializer(task).data, status=status.HTTP_200_OK)
