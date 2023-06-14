from rest_framework import serializers
from .models import Team, TeamRole, Position, TeamMember, MemRole, Sprint, Card, Remark,User

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class TeamRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamRole
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'

class MemRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemRole
        fields = '__all__'

class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class RemarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remark
        fields = '__all__'
