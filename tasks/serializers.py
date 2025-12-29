from django.utils import timezone
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "due_date",
            "priority",
            "status",
            "completed_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "completed_at",
            "created_at",
            "updated_at",
        ]

    def validate_due_date(self, value):
        """
        Ensure due date is today or in the future.
        """
        if value and value < timezone.localdate():
            raise serializers.ValidationError(
                "Due date must be today or in the future."
            )
        return value

    def update(self, instance, validated_data):
        """
        Prevent editing completed tasks unless first reverted to pending.
        Also prevent editing other fields while reverting.
        """
        incoming_status = validated_data.get("status", instance.status)

        if instance.status == Task.Status.COMPLETED:

            # Trying to edit while still completed
            if incoming_status == Task.Status.COMPLETED:
                attempted = set(validated_data.keys()) - {"status"}
                if attempted:
                    raise serializers.ValidationError(
                        {"detail": "Completed tasks cannot be edited. Mark it incomplete first."}
                    )

            # Trying to revert but also change other fields
            if incoming_status == Task.Status.PENDING:
                attempted = set(validated_data.keys()) - {"status"}
                if attempted:
                    raise serializers.ValidationError(
                        {"detail": "First mark task incomplete, then update other fields in a new request."}
                    )

        return super().update(instance, validated_data)
