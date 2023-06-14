from django.contrib import admin
from .models import Team, TeamRole, TeamMember, Sprint,MemRole,Position,Card,Remark

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(TeamRole)
class TeamRoleAdmin(admin.ModelAdmin):
    list_display = ['role']

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['member', 'team', 'position']

@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'end', 'team']

@admin.register(MemRole)
class ABCAdmin(admin.ModelAdmin):
    list_display = ['user', 'role_id']

@admin.register(Position)
class ABCAdmin(admin.ModelAdmin):
    list_display = ['position']

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id','complete','blocker','workingon', 'date']

@admin.register(Remark)
class RemarkAdmin(admin.ModelAdmin):
    list_display = ['remark','card']