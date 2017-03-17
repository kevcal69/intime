import json
from intime.site.models import TimeRecordLog


class TimeRecordMixin(object):

    def get_context_data(self, *args, **kwargs):
        context = super(TimeRecordMixin, self).get_context_data()
        usr = self.request.user
        rec = TimeRecordLog.objects.filter(owner=usr)
        records = []
        for r in rec:
            records.append(self.record_to_dict(r))
        context['vars'] = {
            'records': json.dumps(records)
        }
        return context

    def record_to_dict(self, rec):
        rec = {
            'in': rec.str_datetimein,
            'out': rec.str_datetimeout,
            'active': not rec.closed,
            'uuid': rec.uuid,
            'time': rec.get_time
        }

        return rec
