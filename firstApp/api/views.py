from rest_framework.decorators import api_view,  permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated


@api_view(["GET"])
@permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def firstFuntion(request):
    print(request.query_params)
    print(request.query_params['id'])
    return Response({'message': "We received your request"})