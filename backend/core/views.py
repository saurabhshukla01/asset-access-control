from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Asset
from .serializers import AssetSerializer, MemberAssetSerializer
from .permissions import IsOrgMember

class AssetListView(APIView):
    permission_classes = [IsOrgMember]

    def get(self, request):
        user = request.user
        assets = Asset.objects.filter(organization=user.organization)

        if user.role == 'ADMIN':
            serializer = AssetSerializer(assets, many=True)
        elif user.role == 'MEMBER':
            serializer = MemberAssetSerializer(assets, many=True)
        else:
            return Response({'detail': 'Forbidden'}, status=403)

        return Response(serializer.data)
