from dataclasses import dataclass
from enum import Enum, auto
from datetime import datetime
from typing import Optional
from telemetry import Building


# Standardised States
class DeviceStatus(Enum):
    OK = auto()
    WARNING = auto()
    ERROR = auto()
    CRITICAL = auto()
    MAINTENANCE = auto()
    CALIBRATING = auto()
    OFFLINE = auto()
    LOW_BATTERY = auto()
    OVERHEATING = auto()
    UNDERHEATING = auto()
    OVERLOAD = auto()
    FAULT = auto()
    UNKNOWN = auto()


class DeviceState:
    is_calibrating: bool = False
    is_in_maintenance: bool = False
    last_maintenance: Optional[datetime] = None


# Capacitive Moisture Sensor
class ThresholdStatus(Enum):
    NORM = auto()
    WARN = auto()
    CRIT = auto()


@dataclass()
class MoistureSensor:
    device_id: str
    timestamp: datetime
    moisture_level: float
    threshold_status: ThresholdStatus
    device_status: DeviceStatus
    device_state: DeviceState
    property: Building
    battery_level: float


# Water Leak Detection Sensor
class LeakSeverity(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


@dataclass()
class LeakSensor:
    device_id: str
    timestamp: datetime
    leak_detected: bool
    leak_severity: Optional[LeakSeverity]
    device_status: DeviceStatus
    device_state: DeviceState
    property: Building
    battery_level: float


# RTD Temperature Sensor
class TemperatureStatus(Enum):
    UNDER = auto()
    NORM = auto()
    OVER = auto()


@dataclass()
class TemperatureSensor:
    device_id: str
    timestamp: datetime
    temperature_celsius: float
    temperature_status: TemperatureStatus
    device_status: DeviceStatus
    device_state: DeviceState
    property: Building
    battery_level: float


# CT Energy Monitoring
class EnergyStatus(Enum):
    NORM = auto()
    OVER = auto()
    FAULT = auto()


@dataclass()
class CurrentTransformer:
    device_id: str
    timestamp: datetime
    cur_amperes: float
    vol_volts: float
    pow_watts: float
    e_wh: float
    energy_status: EnergyStatus
    device_status: DeviceStatus
    device_state: DeviceState
    property: Building
    battery_level: float


# CO2 Sensor
class AirQualIndex(Enum):
    GOOD = auto()
    MODERATE = auto()
    POOR = auto()
    HAZARDOUS = auto()


@dataclass()
class CO2Sensor:
    device_id: str
    timestamp: datetime
    co2_ppm: float
    air_quality_index: AirQualIndex
    device_status: DeviceStatus
    device_state: DeviceState
    property: Building
    battery_level: float
