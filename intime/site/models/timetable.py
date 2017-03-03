from __future__ import unicode_literals
from datetime import timedelta, datetime

from django.db import models
from django.contrib.auth.models import User

from intime.site.utils import get_a_uuid

# Create your models here.
class Profile(models.Model):
    owner = models.ForeignKey(User, related_name='owner')

class TimeRecord(models.Model):
    datatime_records = models.DateTimeField(auto_now_add=True)


class TimeRecordLogManager(models.Manager):

    def timein(self, usr):
        timerec = TimeRecord.objects.create()
        a = self.create(owner=usr, datetimein=timerec, uuid=get_a_uuid())
        print a

    def timeout(self, usr, uuid):
        timerecord = self.filter(owner=usr, uuid=uuid, datetimeout=None).last()
        if timerecord:
            timerec = TimeRecord.objects.create()
            timerecord.datetimeout = timerec
            timerecord.closed = True
            timerecord.save()


class TimeRecordLog(models.Model):
    owner = models.ForeignKey(User, related_name='timelog')

    datetimein = models.ForeignKey(
        TimeRecord, null=True, blank=True, related_name='datetimein')
    datetimeout = models.ForeignKey(
        TimeRecord, null=True, blank=True, related_name='datetimeout')

    created = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)

    uuid = models.CharField(max_length=50, blank=False, null=False)
    objects = TimeRecordLogManager()


    @property
    def str_datetimein(self):
        if self.datetimein:
            return self.datetimein.datatime_records.strftime('%Y-%m-%d %H:%M')
        else:
            return ""

    @property
    def str_datetimeout(self):
        if self.datetimeout:
            return self.datetimeout.datatime_records.strftime('%Y-%m-%d %H:%M')
        else:
            return ""

    @property
    def get_time(self):
        if self.datetimeout:
            diff = (self.datetimeout.datatime_records -
                self.datetimein.datatime_records)
            return str(diff)[0:str(diff).rindex(':')]
        else:
            return 0
