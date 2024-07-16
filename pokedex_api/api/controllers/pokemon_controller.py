from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..services import pokemon_service


@api_view(['GET'])
def pokemon_detail(request, id):
    pokemon = pokemon_service.get_pokemon_by_id(id)
    if pokemon:
        return Response(pokemon, status=200)
    return Response({'message': 'Pokemon not found'}, status=404)


@api_view(['PUT'])
def update_pokemon(request, id):
    result = pokemon_service.update_pokemon(id, request.data)
    return Response(result, status=200 if result['success'] else 400)


@api_view(['DELETE'])
def delete_pokemon(request, id):
    result = pokemon_service.delete_pokemon(id)
    return Response({'message': 'Deleted' if result else 'Pokemon not found'}, status=200 if result else 404)


@api_view(['GET'])
def pokemon_detail_by_name(request, name):
    pokemon = pokemon_service.get_pokemon_by_name(name)
    if pokemon:
        return Response(pokemon, status=200)
    return Response({'message': 'Pokemon not found'}, status=404)


@api_view(['PUT'])
def update_pokemon_by_name(request, name):
    result = pokemon_service.update_pokemon_by_name(name, request.data)
    return Response(result, status=200 if result['success'] else 400)


@api_view(['DELETE'])
def delete_pokemon_by_name(request, name):
    result = pokemon_service.delete_pokemon_by_name(name)
    return Response({'message': 'Deleted' if result else 'Pokemon not found'}, status=200 if result else 404)


@api_view(['GET'])
def pokemon_by_type(request, identifier):
    pokemons = pokemon_service.get_pokemon_by_type(identifier)
    if pokemons:
        return Response(pokemons, status=200)
    return Response({'message': 'No Pokemon found for this type'}, status=404)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_pokemons(request):
    if request.user.is_authenticated:
        result = pokemon_service.get_my_pokemon(request.user)
        return Response(result, status=200)
    else:
        return Response({"message": "Please log in first."}, status=401)
