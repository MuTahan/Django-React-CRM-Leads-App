from rest_framework import serializers
from leads.models import lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = lead
        fields = '__all__'
