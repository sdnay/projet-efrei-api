from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from api.controllers import auth_controller, item_controller, move_controller, pokemon_controller, role_controller,admin_controller

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/connexion', auth_controller.login_user, name='login'),
    path('api/register', auth_controller.register_user, name='register'),
    path('api/items/<int:id>', item_controller.item_detail, name='item_detail'),
    path('api/items/<int:id>/update', item_controller.update_item, name='update_item'),
    path('api/items/<int:id>/delete', item_controller.delete_item, name='delete_item'),
    path('api/moves/<int:id>', move_controller.move_detail, name='move_detail'),
    path('api/moves/<int:id>/update', move_controller.update_move, name='update_move'),
    path('api/moves/<int:id>/delete', move_controller.delete_move, name='delete_move'),
    path('api/pokemon/<int:id>', pokemon_controller.pokemon_detail, name='pokemon_detail'),
    path('api/pokemon/<int:id>/update', pokemon_controller.update_pokemon, name='update_pokemon'),
    path('api/pokemon/<int:id>/delete', pokemon_controller.delete_pokemon, name='delete_pokemon'),
    path('api/pokemon/name/<str:name>', pokemon_controller.pokemon_detail_by_name, name='pokemon_detail_by_name'),
    path('api/pokemon/name/<str:name>/update', pokemon_controller.update_pokemon_by_name,
         name='update_pokemon_by_name'),
    path('api/pokemon/name/<str:name>/delete', pokemon_controller.delete_pokemon_by_name,
         name='delete_pokemon_by_name'),
    path('api/pokemon/types/<str:identifier>', pokemon_controller.pokemon_by_type, name='pokemon_by_type'),
    path('api/mesPokemons', pokemon_controller.my_pokemons, name='my_pokemons'),
    path('api/role', role_controller.role_list, name='role_list'),
    path('api/admin/users', admin_controller.list_users, name='admin-list-users'),

]
# swagger for doc

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Documentation for API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
