from dataclasses import dataclass
from enum import Enum, auto
from datetime import datetime
from typing import Optional
from telemetry import Building


# Standardised States
class DeviceStatus(Enum):
    """
    Standardised status values for IoT devices across all systems.
    Attributes:
        OK: Device is operating normally
        WARNING: Device is operating outside normal parameters but not critical
        ERROR: Device has encountered a non-critical error
        CRITICAL: Device has encountered a critical error requiring immediate attention
        MAINTENANCE: Device is under maintenance
        CALIBRATING: Device is performing calibration
        OFFLINE: Device is not responding
        LOW_BATTERY: Device has low battery
        OVERHEATING: Device is overheating
        UNDERHEATING: Device is below optimal operating temperature
        OVERLOAD: Device is experiencing electrical overload
        FAULT: Device has detected a fault condition
        UNKNOWN: Device status is unknown
    """
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
    """
    Standardised operational state of a device
    Attributes:
        is_calibrating: True if device is currently performing calibration
        is_in_maintenance: True if device is currently under maintenance
        last_maintenance: Timestamp of last maintenance activity
    """
    is_calibrating: bool = False
    is_in_maintenance: bool = False
    last_maintenance: Optional[datetime] = None


class BatteryStatus(Enum):
    """
    Standardised battery status levels for IoT devices
    Attributes:
        FULL: Battery is fully charged (100%)
        HIGH: Battery level is high (75-99%)
        MEDIUM: Battery level is medium (50-74%)
        LOW: Battery level is low (25-49%)
        WIRED: Device is powered by a wired connection and does not rely on battery
    """
    FULL = auto()
    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()
    WIRED = auto()


# Capacitive Moisture Sensor
class ThresholdStatus(Enum):
    """
    Attributes:
        NORM: Moisture level is within normal range
        WARN: Moisture level is approaching critical threshold
        CRIT: Moisture level has exceeded critical threshold, indicating potential leak or water damage risk
    """
    NORM = auto()
    WARN = auto()
    CRIT = auto()


@dataclass()
class MoistureSensor:
    """
    Attributes:
        device_id: Unique identifier for the sensor
        timestamp: Time at point of reading (ISO 8601 format)
        moisture_level: Percentage of moisture detected (0-100%)
        threshold_status: Classification of moisture level
        device_status: Current operational status of the device
        device_state: Additional operational state information
        property: Building where sensor is located
        battery_level: Remaining battery percentage (0-100%)
        battery_status: Classification of battery status (FULL, HIGH, MEDIUM, LOW, WIRED)
    """
    device_id: str
    timestamp: datetime
    moisture_level: float
    threshold_status: ThresholdStatus
    device_status: DeviceStatus
    device_state: DeviceState
    property: Building
    battery_level: float
    battery_status: BatteryStatus


# Water Leak Detection Sensor
class LeakSeverity(Enum):
    """
    Attributes:
        LOW: Minor leak detected, no immediate risk of damage
        MEDIUM: Moderate leak detected, potential for damage if not addressed within 24-48 hours
        HIGH: Severe leak detected, immediate risk of significant water damage, requires urgent attention
    """
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


@dataclass()
class LeakSensor:
    """
    Attributes:
        device_id: Unique identifier for the sensor
        timestamp: Time when the reading was taken (ISO 8601 format)
        leak_detected: Boolean indicating if a leak is present
        leak_severity: Severity level of detected leak (if leak_detected=True)
        device_status: Current operational status of the device
        device_state: Additional operational state information
        property: Building where sensor is located
        battery_level: Remaining battery percentage (0-100%)
        battery_status: Classification of battery status (FULL, HIGH, MEDIUM, LOW, WIRED)
    """
    device_id: str
    timestamp: datetime
    leak_detected: bool
    leak_severity: Optional[LeakSeverity]
    device_status: DeviceStatus
    device_state: DeviceState
    property: Building
    battery_level: float
    battery_status: BatteryStatus


# RTD Temperature Sensor
class TemperatureStatus(Enum):
    """
    Attributes:
        UNDER: Temperature is below normal operating range, potential risk of freezing or underperformance
        NORM: Temperature is within normal operating range
        OVER: Temperature is above normal operating range, potential risk of overheating or damage
    """
    UNDER = auto()
    NORM = auto()
    OVER = auto()


@dataclass()
class TemperatureSensor:
    """
    Attributes:
        device_id: Unique identifier for the sensor
        timestamp: Time when the reading was taken (ISO 8601 format)
        temperature_celsius: Measured temperature in degrees Celsius
        temperature_status: Classification of temperature reading
        device_status: Current operational status of the device
        device_state: Additional operational state information
        property: Building where sensor is located
        battery_level: Remaining battery percentage (0-100%)
        battery_status: Classification of battery status (FULL, HIGH, MEDIUM, LOW, WIRED)
    """
    device_id: str
    timestamp: datetime
    temperature_celsius: float
    temperature_status: TemperatureStatus
    device_status: DeviceStatus
    device_state: DeviceState
    property: Building
    battery_level: float
    battery_status: BatteryStatus


# CT Energy Monitoring
class EnergyStatus(Enum):
    """
    Attributes:
        NORM: Energy consumption is within expected range for current conditions
        OVER: Energy consumption is above expected range, potential indication of equipment malfunction or inefficiency
        FAULT: Energy consumption pattern indicates a fault condition, such as a short circuit or overload
    """
    NORM = auto()
    OVER = auto()
    FAULT = auto()


@dataclass()
class CurrentTransformer:
    """
    Attributes:
        device_id: Unique identifier for the sensor
        timestamp: Time when the reading was taken (ISO 8601 format)
        cur_amperes: Measured current in amperes (A)
        vol_volts: Measured voltage in volts (V)
        pow_watts: Active power consumption in watts (W)
        e_wh: Cumulative energy consumption in watt-hours (Wh)
        energy_status: Classification of electrical system condition
        device_status: Current operational status of the device
        device_state: Additional operational state information
        property: Building where sensor is located
        battery_level: Remaining battery percentage (0-100%)
        battery_status: Classification of battery status (FULL, HIGH, MEDIUM, LOW, WIRED)
    """
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
    battery_status: BatteryStatus


# CO2 Sensor
class AirQualIndex(Enum):
    """
    Attributes:
         GOOD: CO2 < 800 ppm, Indicates Acceptable Level
         MODERATE: CO2 800-1200 ppm, Indicates necessary required ventilation
         POOR: CO2 1200-2000 ppm, Indicates range which causes negative health effects.
         HAZARDOUS: CO2 > 2000 ppm, Indicates hazardous air quality
    """
    GOOD = auto()
    MODERATE = auto()
    POOR = auto()
    HAZARDOUS = auto()


@dataclass()
class CO2Sensor:
    """
    Attributes:
        device_id: Unique identifier for the sensor
        timestamp: Time when the reading was taken (ISO 8601 format)
        co2_ppm: CO₂ concentration in parts per million (ppm)
        air_quality_index: Classification of overall air quality
        device_status: Current operational status of the device
        device_state: Additional operational state information
        property: Building where sensor is located
        battery_level: Remaining battery percentage (0-100%)
        battery_status: Classification of battery status (FULL, HIGH, MEDIUM, LOW, WIRED)
    """
    device_id: str
    timestamp: datetime
    co2_ppm: float
    air_quality_index: AirQualIndex
    device_status: DeviceStatus
    device_state: DeviceState
    property: Building
    battery_level: float
    battery_status: BatteryStatus
