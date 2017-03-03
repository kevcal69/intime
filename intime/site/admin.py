from django.contrib import admin
from intime.site.models import TimeRecordLog


class TimeRecordLogAdmin(admin.ModelAdmin):
    model = TimeRecordLog
    list_display = ['owner', 'get_timein', 'get_timeout']

    def get_timein(self, obj):
        if obj.datetimein:
            return obj.datetimein.datatime_records
    get_timein.admin_order_field = 'timein'
    get_timein.short_description = 'Time In record'

    def get_timeout(self, obj):
        if obj.datetimeout:
            return obj.datetimeout.datatime_records
    get_timeout.admin_order_field = 'timeout'
    get_timeout.short_description = 'Time Out record'


admin.site.register(TimeRecordLog, TimeRecordLogAdmin)
