from smarthome.models import AgentAction, SensorEvent


class Rule:
    # TODO: add logic

    name: str = ""

    def matches(self, event: SensorEvent) -> bool:
        # TODO: add logic
        raise NotImplementedError

    def to_action(self, event: SensorEvent) -> AgentAction:
        # TODO: add logic
        raise NotImplementedError