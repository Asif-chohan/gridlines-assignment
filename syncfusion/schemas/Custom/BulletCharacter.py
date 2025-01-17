from enum import Enum


# This was made up by us
class BulletCharacter(Enum):
    BULLET = chr(183)  # Middle dot (•)
    CHECK = chr(252)  # Check mark (✓)
    CROSS = chr(251)  # Cross mark (✗)
    SQUARE = chr(167)  # Square (■)
    CIRCLE = chr(108)  # Circle (○)
    DASH = chr(8212)  # Em dash (—)
