from __future__ import unicode_literals

from django.db import models
from django.auth.contrib import User

from timetable.utils import get_a_uuid

# Create your models here.
class Profile(models.Model):
    owner = models.ForeignKey(User, related_name='owner')

class TimeRecord(models.Model):
    datatime_records = models.DateTimeField(auto_now_add=True)

class TimeRecordLogManager(models.Manager):

    def timeIn(self, usr):
        timerec = TimeRecord.objects.create()
        self.create(owner=usr, datetimeIn=timerec, uuid=get_a_uuid())

    def timeout(self, uuid):
        timerecord = self.filter(uuid=uuid, datetimeout=null).last()
        if timerecord:
            timerec = TimeRecord.objects.create()
            timerecord.datetimeout = timerec
            timerecord.save()


class TimeRecordLog(models.Model):
    owner = models.ForeignKey(User, related_name='timelog')

    datetimeIn = models.ForeignKey(
        TimeRecord, null=True, blank=True, related_name='datetimein')
    datetimeout = models.ForeignKey(
        TimeRecord, null=True, blank=True, related_name='datetimeout')

    created = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)

    uuid = models.CharField(max_length=50, blank=False, null=False)
    objects = TimeRecordLogManager()



    def save(self, *args, **kwargs):
        if (not self.closed and self.datetimeIn and
            not self.datetimeout and kwargs['timeout']):
            self.closed = True
            del kwargs['timeout']
        super(TimeinRecords, self).save(*args, **kwargs)
