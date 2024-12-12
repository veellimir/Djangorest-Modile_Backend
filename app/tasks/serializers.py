from typing import Any, Dict

from rest_framework import serializers

from .models import Tasks, Organization


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model: type[Tasks] = Tasks
        fields: list[str] = [
            'id',
            'organization',
            'user',
            'status_task',
            'title',
            'description',
            'created_at'
        ]
        read_only_fields: list[str] = [
            'created_at'
        ]

    def validate_organization(self, organization: type[Organization]) -> Organization:
        request = self.context['request']

        if not organization.members.filter(id=request.user.id).exists():
            raise serializers.ValidationError(
                "Вы не являетесь участником этой организации"
            )
        return organization

    def save(self, **kwargs: Any) -> Tasks:
        kwargs['user'] = self.context['request'].user
        return super().save(**kwargs)


class TaskStatusesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['status_task']
        