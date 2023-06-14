from django.db import connection
from rest_framework import viewsets, permissions
from .models import Sprint,MemRole,Card,Remark
from .models import Team,TeamMember,TeamRole,User,Card, TeamMember, Remark
from .serializers import SprintSerializer,TeamSerializer,TeamMemberSerializer,TeamRoleSerializer
from .serializers import CardSerializer,RemarkSerializer,MemRoleSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .Permission import IsSuperUser,ScrumMaster
from rest_framework.decorators import api_view

class SprintViewSet(viewsets.ModelViewSet):
    serializer_class = SprintSerializer
    #authentication_classes = [JWTAuthentication]  
    queryset = Sprint.objects.all()
    
    def list(self, request):
        print(request.user.username)
        print(request.user.id)
        
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM public."Api_sprint"')  
            results = cursor.fetchall()

        sprints = []
        for row in results:
            sprint = {
                'id': row[0],
                'name': row[1],
                'description': row[2],
                'end': row[3],
                'team': row[4],
            }
            sprints.append(sprint)
        
        team_ids = [sprint['team'] for sprint in sprints]
        #print(team_ids)
        teams = Team.objects.filter(id__in=team_ids).values('id', 'name')
        
        team_mapping = {team['id']: team['name'] for team in teams}
        for sprint in sprints:
            team_id = sprint['team']
            sprint['team'] = team_mapping.get(team_id)

        return Response(sprints, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data['name']
        description = serializer.validated_data['description']
        end = serializer.validated_data['end']
        team = serializer.validated_data['team']

        with connection.cursor() as cursor:
            print(team)
            print(dir(team))
            cursor.execute(
                'INSERT INTO public."Api_sprint" (name, description, "end", team_id) VALUES (%s, %s, %s, %s)',
                [name, description, end, team['name']]
            )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
#class TeamViewSet(viewsets.ModelViewSet):
        
        serializer_class=TeamSerializer
        queryset=Team.objects.all()

        def list(self,request):
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM public."Api_team"')  
                results = cursor.fetchall()
            teams=[]
            for row in results:
                team = {
                'id': row[0],
                'name': row[1]
                }
                teams.append(team)
            return Response(teams, status=status.HTTP_200_OK)
        
        def create(self,request):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            name = serializer.validated_data['name']
            with connection.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO public."Api_team"()'
                )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset=TeamMember.objects.all()
    serializer_class=TeamMemberSerializer


class MemRoleViewset(viewsets.ModelViewSet):
    queryset=TeamRole.objects.all()
    serializer_class=TeamRoleSerializer

    

class CardViewSet(viewsets.ModelViewSet):
    queryset= Card.objects.all()
    serializer_class=CardSerializer



@api_view(['GET'])
def data_view(request):
    
    cards = Card.objects.all()
    card_data = []
    
    print(cards)
    
        
    for card in cards:
        team_members = TeamMember.objects.filter(team=card.sprint_id.team)
        team_member_data = []

        for team_member in team_members:
            team_member_data.append({
                'id': team_member.id,
                'member_name': team_member.member.username,
                'position_name': team_member.position.position,
                'team_name': team_member.team.name
            })
        card_data.append({
            'id': card.id,
            'complete': card.complete,
            'workingon': card.workingon,
            'blocker': card.blocker,
            'date': str(card.date),
            'sprint_id': card.sprint_id.id,
            'team_members': team_member_data,
            'remarks':  [
                            {
                                "member_name": remark.member.member.username,
                                "remark": remark.remark
                            } 
                            for remark in Remark.objects.filter(card=card)
                        ]
                        })

    return Response(card_data)

