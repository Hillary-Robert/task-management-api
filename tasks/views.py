from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.utils import timezone

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    filterset_fields = ["status", "priority", "due_date"]
    ordering_fields = ["due_date", "priority", "created_at"]
    ordering = ["due_date"]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.status == Task.Status.COMPLETED:
            raise ValidationError({"detail": "Completed tasks cannot be edited. Mark it incomplete first."})
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.status == Task.Status.COMPLETED:
            raise ValidationError({"detail": "Completed tasks cannot be edited. Mark it incomplete first."})
        return super().partial_update(request, *args, **kwargs)

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
