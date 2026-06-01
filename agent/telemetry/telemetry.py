import datetime
import random
import string
from typing import Literal

# Complaint descriptions mapping for random selection
COMPLAINT_DESCRIPTIONS = {
    "Leaking pipe": [
        "There's a steady drip coming from the pipe under the kitchen sink — water pooling in the cabinet and staining the wood. Happening since last night.",
        "Cold water pipe in the laundry room started leaking during the evening. I put a bucket under it but it keeps overflowing.",
        "Ceiling below the bathroom upstairs is wet and bubbling — I can see water stains spreading. Smells a bit musty now.",
        "Small leak at the joint behind the toilet tank. It gets worse whenever someone flushes.",
        "Copper pipe near the hot water heater has a hairline crack and sprays when the washing machine runs — urgent.",
        "I noticed brown water dripping from the ceiling light in the hallway. Appears to be coming from a pipe above.",
        "Slow steady leak from the external hose bib. Water saturates the soil next to the foundation.",
        "Pipe under sink bursts occasionally when dishwasher runs, causing water to come out onto kitchen floor.",
        "Shower drain area is wet even when not in use — there’s water coming from the pipe behind the tiles.",
        "Kitchen faucet base leaks and water is pooling on the countertop, damaging the laminate.",
        "Basement sump pump pipe has a leak joint — water is running down the wall and causing efflorescence.",
        "I found mold starting in the cabinet from a long-term leak under the sink. Concerned about health risks.",
        "During heavy rain the pipe in the ceiling drips and the water trickles down the wall — needs sealing.",
        "Radiator supply pipe is leaking slightly at the valve; radiator gets hot but the area is wet.",
        "Hot water line near the boiler is dripping and creating a puddle on the floor; noticed a drop in hot water pressure."
    ],
    "HVAC failure": [
        "The apartment hasn't been cooling since this morning — thermostat shows 72°F but the vents blow warm air.",
        "Furnace is not turning on at all; it's cold inside and the pilot light looks out.",
        "AC cycles on and off every few minutes and the apartment never reaches the set temperature.",
        "Very loud banging and clanking coming from the HVAC unit whenever it starts. Woke us up several times last night.",
        "Strange burning smell from the vents when the system runs — worried about safety.",
        "Heat works intermittently; sometimes the temperature drops drastically in the evening.",
        "Vents only blowing in one room; the rest of the apartment gets no airflow.",
        "Thermostat display is flashing and refuses to accept settings; HVAC is stuck in emergency mode.",
        "System is making a high-pitched squeal and then shuts down after a few minutes of running.",
        "Cold air is blowing but humidity is very high — unit seems to not dehumidify or remove moisture.",
        "There is a leak around the outdoor condenser unit and puddles form under the compressor.",
        "Supply vent in the bedroom is blowing dust and sometimes black particles — concern for indoor air quality.",
        "Heater flame is flickering and the unit frequently trips the circuit breaker.",
        "AC smells like mildew every time it runs; vents feel damp and there’s a visible film on the registers.",
        "The blower fan seems weak; airflow is very low even at the highest setting."
    ],
    "Boiler pressure drop": [
        "Hot water pressure has been very low for the last two days; radiators don't heat up fully.",
        "Boiler gauge shows pressure dropping below normal each morning and I have to top it up.",
        "Heater makes a gurgling noise and the radiators are cold at the far end of the system.",
        "I noticed water around the base of the boiler and the pressure gauge reads much lower than usual.",
        "Hot water takes a long time to arrive and sometimes goes cold after a minute — seems like pressure issues.",
        "The boiler keeps shutting down with a 'low pressure' fault message on the display.",
        "Radiators are hot at the bottom but cold at the top — suspected airlock related to pressure loss.",
        "An audible hissing from the boiler area and then the pressure drops within hours.",
        "Following the repair last month the pressure keeps falling; unsure where the leak is.",
        "No hot water in the upstairs bathrooms; pressure gauge reads zero intermittently.",
        "The expansion tank might be failing — frequent pressure fluctuations and cold spots on radiators.",
        "Pilot stays lit but system trips out due to low pressure; pressure relief valve may be leaking.",
        "Boiler cycles frequently and pressure drops after each cycle; heating is inconsistent.",
        "Water puddle near the radiator valve and boiler pressure readout slowly decreases over a day.",
        "We lose heat overnight and have to manually repressurize the system in the morning."
    ],
    "Water meter anomaly": [
        "My water meter reading jumped dramatically overnight even though we weren't home and all fixtures were off.",
        "Meter shows continuous flow while everything is turned off — suspect hidden leak or faulty meter.",
        "Usage increased by several hundred liters this month with no change in our routine. Please inspect.",
        "Reading seems to be fluctuating wildly each time I check; may be the meter is stuck or misreporting.",
        "We've been billed for unusually high water consumption; I monitored the meter and it keeps creeping up.",
        "Meter spins slowly even with no taps open — I'm certain nothing is drawing water.",
        "After fixing a visible leak the meter still reports high usage — maybe the meter itself is defective.",
        "Meter pulses several times per minute even when nobody in the unit is using water.",
        "Neighbor had a leak and our meter still shows abnormal usage after their repair; please verify installation.",
        "I compared last month's and this month's usage and there is a sudden unexplained spike.",
        "Outdoor meter reading seems stuck and then jumps by a large amount; might be a mechanical fault.",
        "Meter display shows odd symbols and the digital readout resets intermittently.",
        "Water consumption appears to increase when the irrigation system is off; possibly cross-connection or meter error.",
        "We found damp soil near an underground service pipe and the meter shows continuous flow — suspect underground leak.",
        "Meter increments when the washing machine and dishwasher are not running — a technician visit is required."
    ],
}

def get_random_description(title:Literal["Leaking pipe", "HVAC failure", "Boiler pressure drop", "Water meter anomaly"]) -> str:
    options = COMPLAINT_DESCRIPTIONS.get(title)
    if options:
        return random.choice(options)
    for key in COMPLAINT_DESCRIPTIONS:
        if key.lower() in title.lower() or title.lower() in key.lower():
            return random.choice(COMPLAINT_DESCRIPTIONS[key])
    return f"Resident submitted a complaint titled '{title}' but no prepared description is available."


def generate_random(length: int) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class Device:
    def __init__(self, _device_type, *telemetry_data_fields:str):
        self.name = "Device_" + generate_random(8)
        self.type = _device_type
        self.data = {}
        for field in telemetry_data_fields:
            self.data[field] = None

class Complaint:
    def __init__(self, creation_date_time:datetime.datetime, _title:str, _description:str):
        self.date_time = creation_date_time
        self.title = _title
        self.description = _description
        self.category = None
        self.isActive = True

class Building:
    def __init__(self):
        self.name = "Building_" + generate_random(5)
        self.devices = []
        self.active_complaints = []
        self.complaint_history = []

class TelemetryData:
    RAN_LEN = 8
    def __init__(self):
        self.buildingStore = set([])
        for i in range(5000):
            building = Building()
            for j in range(random.randint(4, 40)):
                device_type = random.choice(["HVAC", "Boiler", "WaterMeter", "PressureSensor"])
                if device_type == "HVAC":
                    device = Device(device_type, "temperature", "status")
                    device.data["temperature"] = random.uniform(15.0, 30.0)
                    device.data["status"] = random.choice(["operational", "maintenance_required", "failure"])
                elif device_type == "Boiler":
                    device = Device(device_type, "pressure", "status")
                    device.data["pressure"] = random.uniform(1.0, 5.0)
                    device.data["status"] = random.choice(["operational", "maintenance_required", "failure"])
                elif device_type == "WaterMeter":
                    device = Device(device_type, "water_usage", "leak_status")
                    device.data["water_usage"] = random.uniform(0.0, 100.0)
                    device.data["leak_status"] = random.choice(["no_leak", "leak_detected"])
                else:
                    device = Device(device_type, "pressure", "anomaly_status")
                    device.data["pressure"] = random.uniform(1.0, 5.0)
                    device.data["anomaly_status"] = random.choice(["normal", "anomaly_detected"])
                building.devices.append(device)
            for k in range(random.randint(0, 5)):
                creation_time = datetime.datetime.now() - datetime.timedelta(days=random.randint(60, 365))
                title = random.choice(["Leaking pipe", "HVAC failure", "Boiler pressure drop", "Water meter anomaly"])
                _description = get_random_description(title)
                complaint = Complaint(creation_time, title, _description)
                complaint.category = random.choice(["Plumbing", "HVAC", "Electrical", "General Maintenance"])
                complaint.isActive = False
                building.complaint_history.append(complaint)
            self.buildingStore.add(building)

# tel = TelemetryData()
# for b in tel.buildingStore:
#     print(f"\n\n----Building: {b.name}----")
#     print(f"\n--Overview--\nDevices: {len(b.devices)}\nActive Complaints: {len(b.active_complaints)}\nComplaint History: {len(b.complaint_history)}")
#     print(f"\n--Devices--")
#     for d in b.devices:
#         print(f"Device Name: {d.name}\nType: {d.type}\nData: {d.data}")
#     print(f"\n--Complaint History--")
#     for c in b.complaint_history:
#         print(f"Date: {c.date_time}\nTitle: {c.title}\nDescription: {c.description}\nCategory: {c.category}\nActive: {c.isActive}")


