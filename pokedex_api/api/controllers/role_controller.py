from django.http import JsonResponse
from rest_framework.response import Response
from ..services import role_service
from rest_framework.decorators import api_view, permission_classes
from ..utils.permissions import IsAdminUserCustom


@api_view(['GET'])
@permission_classes([IsAdminUserCustom])
def role_list(request):
    if not request.user.is_authenticated:
        return Response({"message": "Authentication required"}, status=401)

    elif request.user.is_authenticated:
        roles = role_service.get_all_roles()
        return JsonResponse(roles, safe=False, status=200)
    else:
        return Response({"message": "Unauthorized"}, status=403)
