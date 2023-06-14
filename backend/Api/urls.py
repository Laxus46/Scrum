from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SprintViewSet
from .views import TeamViewSet,TeamMemberViewSet,MemRoleViewset
from .views import CardViewSet
from .views import data_view
#from .views import   TeamRoleViewSet, TeamMemberViewSet

router = DefaultRouter()
#router.register(r'sprints', SprintViewSet, basename='sprint')
#router.register(r'team',TeamViewSet, basename='team')



router.register(r'sprints', SprintViewSet)
router.register(r'team',TeamViewSet)



router.register(r'teamroles', MemRoleViewset)
router.register(r'teammembers', TeamMemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('data/', data_view, name='data-view'),
]


# urlpatterns = [
#     #URL patterns 
#     path('api/', include(router.urls)),
#     path('api/sprints/', SprintViewSet.as_view({'get': 'list'}), name='sprint-list'),
#     path('api/team/',TeamViewSet.as_view({'get:list'}),name='team-list'),
# ]
