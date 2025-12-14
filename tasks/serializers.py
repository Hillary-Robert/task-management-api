from django.utils import timezone
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "user",
            "title",
            "description",
            "due_date",
            "priority",
            "status",
            "completed_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "user", "completed_at", "created_at", "updated_at"]

    def validate_due_date(self, value):
        if value and value < timezone.localdate():
            raise serializers.ValidationError("Due date must be today or in the future.")
        return value

    def update(self, instance, validated_data):
        # Rule: once completed, it cannot be edited unless reverted to incomplete (pending)
        incoming_status = validated_data.get("status", instance.status)

        if instance.status == Task.Status.COMPLETED and incoming_status == Task.Status.COMPLETED:
            
            editable_fields = {"status"}  #

            attempted = set(validated_data.keys()) - editable_fields
            if attempted:
                raise serializers.ValidationError(
                    "Completed tasks cannot be edited unless reverted to pending."
                )

        return super().update(instance, validated_data)
