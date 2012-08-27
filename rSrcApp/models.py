import datetime
from django.db import models
from django.utils import timezone

class Sponsor(models.Model):
    name = models.CharField(max_length=80)
    
    SPONSOR_TYPE_CHOICES = (
        ('BU',  'Business and Commercial'),
        ('EDU', 'Educational and Academic'),
        ('NPO', 'Non-profit Organization'))
    
    type = models.CharField(max_length=4, choices=SPONSOR_TYPE_CHOICES)

            
class Project(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    LICENSE_CHOICES = (
        ('OS', 'Open Source'),
        ('GPL', 'GNU License'),
        ('COM', 'Commercial/Closed'))
    license = models.CharField(max_length=4, choices=LICENSE_CHOICES)

    price = models.IntegerField(null=True)
    max_participants = models.IntegerField(null=True)
    #post_date = models.DateTimeField(verbose_name='Date job was posted', auto_now_add=True)
    post_date = models.DateTimeField(verbose_name='Date job was posted')
    due_date = models.DateField('Date job is needed')
    
    def __unicode__(self):
        return self.title

    def job_length(self):
        return self.due_date - timezone.now()
        
    def is_new(self):
        return self.open_date >= timezone.now() - datetime.timedelta(days=1)

class ProjectSkill(models.Model):
    description = models.CharField(max_length=25)
    level = models.IntegerField(verbose_name='Skill Level needed', null=True)
    job = models.ForeignKey(Project)
    
    def __unicode__(self):
        return self.description

    
class Participant(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class ParticipantSkill(models.Model):
    description = models.CharField(max_length=25)
    level = models.IntegerField()
    contractor = models.ForeignKey(Participant)
    
    def __unicode__(self):
        return self.description


#
#  Contracts, associations between entities
#
class WorkOnContract(models.Model):
    name = models.CharField(max_length=100)
    terms = models.CharField(max_length=500)
    late_penalty = models.IntegerField()
    early_bonus = models.IntegerField()
    project = models.ForeignKey(Project)
    participant = models.ForeignKey(Participant)

class SponsorContract(models.Model):
    name = models.CharField(max_length=100)
    terms = models.CharField(max_length=500)
    late_penalty = models.IntegerField()
    early_bonus = models.IntegerField()
    project = models.ForeignKey(Project)
    Sponsor = models.ForeignKey(Sponsor)
        