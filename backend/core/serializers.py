from rest_framework import serializers
from .models import Asset

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['name', 'secret_key']

class MemberAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['name']
