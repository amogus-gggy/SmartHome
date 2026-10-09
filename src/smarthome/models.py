from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
RAW_EVENTS_FILE = DATA_DIR / "smart_home_events_raw.csv"


class DoorState(StrEnum):
    OPEN = "open"
    CLOSED = "closed"


class MotionState(StrEnum):
    DETECTED = "detected"
    NONE = "none"


class ControllerMode(StrEnum):
    HOME = "home"
    AWAY = "away"
    NIGHT = "night"


@dataclass(frozen=True, slots=True)
class SensorEvent:
    # TODO: add logic
    timestamp: str
    room: str
    temperature_c: float
    illuminance_lux: float
    motion: MotionState
    door_state: DoorState
    controller_mode: ControllerMode


@dataclass(frozen=True, slots=True)
class AgentAction:
    # TODO: add logic
    timestamp: str
    room: str
    device: str
    command: str
    reason: str