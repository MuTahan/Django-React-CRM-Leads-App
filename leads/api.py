from leads.models import lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer