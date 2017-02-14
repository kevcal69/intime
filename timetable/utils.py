import base64
import uuid
from timetable.models import TimeRecordLog

#: url safe uuid
def get_a_uuid():
    r_uuid = base64.urlsafe_b64encode(uuid.uuid4().bytes)
    return r_uuid.replace('=', '')
