# Architecture

The `smarthome` package lives in `src/`. The entry point is `smarthome.__main__:main`.

| Module | Responsibility |
|--------|----------------|
| `smarthome.models` | Domain dataclasses and enums: `SensorEvent`, `AgentAction`, `DoorState`, `MotionState`, `ControllerMode` |
| `smarthome.data` | Reads raw CSV events into domain objects |
| `smarthome.rules` | `Rule` base class, the extension point for every automation rule |
| `smarthome.agent` | `SmartHomeAgent`, holds a rule set and processes events |

Data flow: `data/smart_home_events_raw.csv` → `smarthome.data` → `SensorEvent` list →
`SmartHomeAgent` → `AgentAction` list.

Every module is a stub and raises `NotImplementedError`.