import datetime
import random
import string
from typing import List

used_strings = set()

def generate_random(length: int) -> str:
    rand = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    if rand in used_strings:
        return generate_random(length)
    return rand

class Warn:
    def __init__(self, device:Device, t, warn_type:str):
        self.date_time = t
        self.title = warn_type
        self.device = {
            "snapshot": None,
            "name": device.name,
            "type": device.type
        }

class Device:
    def __init__(self, _name:str, _device_type:str):
        self.name = _name
        self.type = _device_type
        self.data = {}
        self.log:List[Warn] = []


class Complaint:
    def __init__(self, creation_date_time:datetime.datetime, _title:str, _description:str, category:str, is_active:bool):
        self.date_time = creation_date_time
        self.title = _title
        self.description = _description
        self.category = category
        self.is_active = is_active

class Building:
    def __init__(self, n:str):
        self.name = n
        self.devices:List[Device] = []
        self.active_complaints:List[Complaint] = []
        self.complaint_history:List[Complaint] = []





