from django.contrib.auth.models import User
from django.db import models

class Team(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Member(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=75)

    def __str__(self):
        return"{0}{1}".format(self.first_name,self.last_name)
    

class TeamRole(models.Model):
    role=models.CharField(max_length=100)

    def __str__(self):
        return self.role
    

class Position(models.Model):
    position=models.CharField(max_length=100)

    def __str__(self):
        return self.position


class TeamMember(models.Model):
    member = models.ForeignKey(User,on_delete=models.CASCADE)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
    team=models.ForeignKey(Team,on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.member.username},{self.team.name})'


class MemRole(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    role_id= models.ForeignKey(TeamRole,on_delete=models.CASCADE)


class Sprint(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    end = models.DateField(unique=True)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)

    def __str__(self):
        team_name = self.team.name if self.team else 'N/A'
        return f'{self.name}'


class Card(models.Model):
    sprint_id = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    complete = models.CharField(max_length=100)  # Adjust the max_length as per your requirements
    workingon = models.CharField(max_length=100)  # Adjust the max_length as per your requirements
    blocker = models.CharField(max_length=100)  # Adjust the max_length as per your requirements
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Card (Sprint: {self.sprint_id.name}, Team: {self.sprint_id.team.name}, Date: {self.date})'
  

class Remark(models.Model):
    remark=models.CharField()
    member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    card=models.ForeignKey(Card, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Remark ({self.member.member.username}): {self.remark}'