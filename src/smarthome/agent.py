from smarthome.models import AgentAction, SensorEvent
from smarthome.rules import Rule


class SmartHomeAgent:
    # TODO: add logic

    def __init__(self, rules: list[Rule] | None = None) -> None:
        # TODO: add logic
        raise NotImplementedError

    def add_rule(self, rule: Rule) -> None:
        # TODO: add logic
        raise NotImplementedError

    def process(self, event: SensorEvent) -> list[AgentAction]:
        # TODO: add logic
        raise NotImplementedError

    def run(self, events: list[SensorEvent]) -> list[AgentAction]:
        # TODO: add logic
        raise NotImplementedError