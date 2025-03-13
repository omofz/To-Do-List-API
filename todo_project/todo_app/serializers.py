from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    is_overdue = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = [
            'id',
            'title',
            'description',
            'status',
            'created_at',
            'updated_at',
            'due_date',
            'is_overdue',
        ]

    def get_is_overdue(self, obj):
        return obj.is_overdue()
