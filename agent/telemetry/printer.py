from telemetry import Building
from telemetry import Device
from telemetry import Warn
from telemetry import TelemetryData
from telemetry import Complaint

string_items = ["temperature anomaly", "status failure", "pressure anomaly", "status failure", "water_usage anomaly", "leak_status detected", "pressure anomaly", "anomaly_status detected"]

def print_building(_building: Building):
    f.write(f"b = Building(\"{_building.name}\")\n")
    for device in _building.devices:
        print_device(device)
    for complaint in _building.active_complaints:
        print_complaint(complaint)
        f.write("b.active_complaints.append(c)\n")
    for complaint in _building.complaint_history:
        print_complaint(complaint)
        f.write("b.complaint_history.append(c)\n")

def print_device(_device:Device):
    f.write(f"d = Device(\"{_device.name}\",\"{_device.type}\")\n")
    temp = []
    for key, value in _device.data.items():
        if isinstance(value, str) or value in string_items:
            temp.append(f"\"{key}\":\"{value}\"")
        else:
            temp.append(f"\"{key}\":{value}")

    f.write(f"d.data = {{{", ".join(temp)}}}\n")
    for warn in _device.log:
        print_warn(warn)
    f.write("b.devices.append(d)\n")

def print_warn(_warn:Warn):
    f.write(f"w = Warn(d, datetime.datetime.fromisoformat(\"{_warn.date_time}\"), \"{_warn.title}\")\n")
    temp = []
    for key, value in _warn.device["snapshot"].items():
        if isinstance(value, str) or value in string_items:
            temp.append(f"\"{key}\":\"{value}\"")
        else:
            temp.append(f"\"{key}\":{value}")
    f.write(f"w.device[\"snapshot\"] = {{{", ".join(temp)}}}\n")
    f.write("d.log.append(w)\n")

def print_complaint(_complaint:Complaint):
    f.write(f"c = Complaint(datetime.datetime.fromisoformat(\"{_complaint.date_time}\"), \"{_complaint.title}\", \"{_complaint.description})\", \"{_complaint.category}\", {_complaint.is_active})\n")


tel = TelemetryData()
tel.gen(num_buildings=10, min_devices=1, max_devices=3, min_complaints=0, max_complaints=3, min_warns=1, max_warns=3)

with open("generated.py", "w+", encoding="utf-8") as f:
    f.write("""
from telem2 import Building
from telem2 import Device
from telem2 import Warn
from telemetry import TelemetryData
from telem2 import Complaint
import time
import random
import datetime
""")
    f.write("tel = TelemetryData()\n")
    f.write("b:Building = None\n")
    f.write("d:Device = None\n")
    f.write("w:Warn = None\n")
    f.write("c:Complaint = None\n")

    for building in tel.building_store:
        print_building(building)
        f.write("tel.building_store.add(b)\n")
        f.write("b = None\n")
        f.write("d = None\n")
        f.write("w = None\n")
        f.write("c = None\n")

    f.write("""
while True:
    time.sleep(random.randint(1, 5)/100)
    num = random.randint(0, 100)
    if num == 10:
        c, b = tel.generate_complaint()
        print(f"New Complaint: {c.title} at {c.date_time} in {b.name}")
    elif num == 9:
        w, b = tel.generate_warn()
        print(f"New Warn: {w.title} at {w.date_time} in {b.name} for device {w.device['name']}")
""")
