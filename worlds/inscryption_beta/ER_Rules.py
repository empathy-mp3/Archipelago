from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region
from entrance_rando import EntranceType, randomize_entrances
from .ER_Data import randomized_connections, transitions
from .Options import Act2RandomizeEntrances

if TYPE_CHECKING:
    from . import InscryptionWorld


def disconnect_entrances(world: "InscryptionWorld") -> None:
    def disconnect_entrance() -> None:
        child = entrance.connected_region.name
        child_region = entrance.connected_region
        child_region.entrances.remove(entrance)
        entrance.connected_region = None

        er_type = EntranceType.ONE_WAY if child == "Glacial Peak - Left" else \
            EntranceType.TWO_WAY if child in randomized_connections else EntranceType.ONE_WAY
        if er_type == EntranceType.TWO_WAY:
            mock_entrance = entrance.parent_region.create_er_target(entrance.name)
        else:
            mock_entrance = child_region.create_er_target(child)

        entrance.randomization_type = er_type
        mock_entrance.randomization_type = er_type


    for parent, child in randomized_connections.items():
        if child == "Corrupted Future":
            entrance = world.get_entrance("Artificer's Portal")
        elif child == "Tower of Time - Left":
            entrance = world.get_entrance("Artificer's Challenge")
        else:
            entrance = world.get_entrance(f"{parent} -> {child}")
        disconnect_entrance()

def shuffle_transitions(world: "InscryptionWorld") -> None:

    result = randomize_entrances(world, coupled, {0: [0]})

    world.transitions = sorted(result.placements, key=lambda entrance: TRANSITIONS.index(entrance.parent_region.name))

    for transition in world.transitions:
        if "->" not in transition.name:
            continue
        transition.parent_region.exits.remove(transition)
        transition.name = f"{transition.parent_region.name} -> {transition.connected_region.name}"
        transition.parent_region.exits.append(transition)
