from dataclasses import dataclass


@dataclass(frozen=True)
class LCSDirections:
    TOP_LEFT: str = 'top-left'
    LEFT: str = 'left'
    TOP: str = 'top'
