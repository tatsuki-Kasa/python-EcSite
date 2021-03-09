from rest_framework import serializers

from .models import EcSite


class EcSiteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'status',
        )
        model = EcSite
