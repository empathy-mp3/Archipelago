from .Options import InscryptionOptions, Goal, EpitaphPiecesRandomization, PaintingChecksBalancing, \
      RandomizeHammer, RandomizeShortcuts, RandomizeVesselUpgrades, Act2RandomizeEntrances
from .Items import act1_items, act2_items, act3_items, act2_3_items, filler_items, base_id, InscryptionItem, ItemDict
from .Locations import act1_locations, act2_locations, act3_locations, regions_to_locations
from .Regions import inscryption_regions_all
from typing import Dict, Any, TextIO
from . import Rules
from BaseClasses import Region, Item, Tutorial, ItemClassification, Entrance, EntranceType
from worlds.AutoWorld import World, WebWorld
from .ER_Rules import disconnect_entrances, shuffle_transitions


class InscrypWeb(WebWorld):
    theme = "dirt"

    guide_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Inscryption Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["DrBibop"]
    )

    guide_fr = Tutorial(
        "Multiworld Setup Guide",
        "Un guide pour configurer Inscryption Archipelago Multiworld",
        "Français",
        "setup_fr.md",
        "setup/fr",
        ["Glowbuzz"]
    )

    tutorials = [guide_en, guide_fr]

    bug_report_page = "https://github.com/DrBibop/Archipelago_Inscryption/issues"


class InscryptionWorld(World):
    """
    Inscryption is an inky black card-based odyssey that blends the deckbuilding roguelike,
    escape-room style puzzles, and psychological horror into a blood-laced smoothie.
    Darker still are the secrets inscrybed upon the cards...
    """
    game = "Inscryption Beta"
    web = InscrypWeb()
    options_dataclass = InscryptionOptions
    options: InscryptionOptions
    all_items = act1_items + act2_items + act3_items + act2_3_items + filler_items
    item_name_to_id = {item["name"]: i + base_id for i, item in enumerate(all_items)}
    all_locations = act1_locations + act2_locations + act3_locations
    location_name_to_id = {location: i + base_id for i, location in enumerate(all_locations)}
    required_epitaph_pieces_count = 9
    required_epitaph_pieces_name = "Epitaph Piece"
    transitions: list[Entrance]

    def generate_early(self) -> None:
        self.all_items = [item.copy() for item in self.all_items]

        if self.options.epitaph_pieces_randomization == EpitaphPiecesRandomization.option_all_pieces:
            self.required_epitaph_pieces_name = "Epitaph Piece"
            self.required_epitaph_pieces_count = 9
        elif self.options.epitaph_pieces_randomization == EpitaphPiecesRandomization.option_in_groups:
            self.required_epitaph_pieces_name = "Epitaph Pieces"
            self.required_epitaph_pieces_count = 3
        else:
            self.required_epitaph_pieces_name = "Epitaph Pieces"
            self.required_epitaph_pieces_count = 1

        if self.options.painting_checks_balancing == PaintingChecksBalancing.option_balanced:
            self.all_items[6]["classification"] = ItemClassification.progression
            self.all_items[11]["classification"] = ItemClassification.progression

        if self.options.painting_checks_balancing == PaintingChecksBalancing.option_force_filler \
                and not self.options.enable_act_2\
                and not self.options.enable_act_3:
            self.all_items[3]["classification"] = ItemClassification.filler

        if self.options.epitaph_pieces_randomization != EpitaphPiecesRandomization.option_all_pieces:
            self.all_items[len(act1_items) + 3]["count"] = self.required_epitaph_pieces_count

        if self.options.randomize_vessel_upgrades != RandomizeVesselUpgrades.option_randomize:
            self.all_items[len(act1_items) + len(act2_items) + 15]["count"] = 2

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)["name"]

    def create_item(self, name: str) -> Item:
        item_id = self.item_name_to_id[name]
        item_data = self.all_items[item_id - base_id]
        return InscryptionItem(name, item_data["classification"], item_id, self.player)

    def create_items(self) -> None:
        nb_items_added = 0
        useful_items = self.all_items.copy()
        included_locations = len(self.all_locations)

        useful_items = [item for item in useful_items
                        if not any(filler_item["name"] == item["name"] for filler_item in filler_items)]
        if self.options.randomize_hammer != RandomizeHammer.option_randomize \
        or not (self.options.enable_act_2 or self.options.enable_act_3):
            useful_items.pop(len(act1_items) + len(act2_items) + len(act3_items))
        if self.options.enable_act_3:
            if self.options.randomize_vessel_upgrades == RandomizeVesselUpgrades.option_vanilla:
                useful_items.pop(len(act1_items) + len(act2_items) + 16)
                useful_items.pop(len(act1_items) + len(act2_items) + 15)
                included_locations -= 4
            if self.options.randomize_shortcuts != RandomizeShortcuts.option_randomize:
                useful_items.pop(len(act1_items) + len(act2_items) + 14)
                useful_items.pop(len(act1_items) + len(act2_items) + 13)
                useful_items.pop(len(act1_items) + len(act2_items) + 12)
                if self.options.randomize_shortcuts == RandomizeShortcuts.option_vanilla:
                    included_locations -= 3
        if self.options.enable_act_2:
            if self.options.epitaph_pieces_randomization == EpitaphPiecesRandomization.option_all_pieces:
                useful_items.pop(len(act1_items) + 3)
            else:
                useful_items.pop(len(act1_items) + 2)
        if not self.options.enable_act_1:
            useful_items = [item for item in useful_items
                            if not any(act1_item["name"] == item["name"] for act1_item in act1_items)]
            included_locations -= len(act1_locations)
        if not self.options.enable_act_2:
            useful_items = [item for item in useful_items
                            if not any(act2_item["name"] == item["name"] for act2_item in act2_items)]
            included_locations -= len(act2_locations)
        if not self.options.enable_act_3:
            useful_items = [item for item in useful_items
                            if not any(act3_item["name"] == item["name"] for act3_item in act3_items)]
            included_locations -= len(act3_locations)

        for item in useful_items:
            for _ in range(item["count"]):
                new_item = self.create_item(item["name"])
                self.multiworld.itempool.append(new_item)
                nb_items_added += 1

        filler_count = included_locations
        filler_count -= nb_items_added

        for i in range(filler_count):
            index = i % len(filler_items)
            filler_item = filler_items[index]
            new_item = self.create_item(filler_item["name"])
            self.multiworld.itempool.append(new_item)

    def create_regions(self) -> None:
        used_regions = inscryption_regions_all

        if not self.options.enable_act_1:
            del used_regions["Act 1"]
            used_regions["Menu"].remove("Act 1")
        if not self.options.enable_act_2:
            del used_regions["Act 2"]
            used_regions["Menu"].remove("Act 2")
        if not self.options.enable_act_3:
            del used_regions["Act 3"]
            used_regions["Menu"].remove("Act 3")
        if self.options.enable_act_3:
            if self.options.randomize_vessel_upgrades == RandomizeVesselUpgrades.option_vanilla:
                regions_to_locations["Act 3"].pop(37)
                regions_to_locations["Act 3"].pop(36)
                regions_to_locations["Act 3"].pop(35)
                regions_to_locations["Act 3"].pop(34)
            if self.options.randomize_shortcuts == RandomizeShortcuts.option_vanilla:
                regions_to_locations["Act 3"].pop(33)
                regions_to_locations["Act 3"].pop(32)
                regions_to_locations["Act 3"].pop(31)
        for region_name in used_regions.keys():
            self.multiworld.regions.append(Region(region_name, self.player, self.multiworld))

        for region_name, region_connections in used_regions.items():
            region = self.get_region(region_name)
            region.add_exits(region_connections)
            region.add_locations({
                location: self.location_name_to_id[location] for location in regions_to_locations[region_name]
            })

    def set_rules(self) -> None:
        Rules.InscryptionRules(self).set_all_rules()

        def connect_entrances(self) -> None:
            if self.options.act2_randomize_entrances != Act2RandomizeEntrances.option_disable:
                disconnect_entrances(self)
                shuffle_transitions(self)

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:

        spoiler = self.multiworld.spoiler

        if self.options.act2_randomize_entrances:
            for transition in self.transitions:
                if (transition.randomization_type == EntranceType.TWO_WAY
                        and (transition.connected_region.name, "both", self.player) in spoiler.entrances):
                    continue
                spoiler.set_entrance(
                    transition.name if "->" not in transition.name else transition.parent_region.name,
                    transition.connected_region.name,
                    "both" if transition.randomization_type == EntranceType.TWO_WAY
                              and self.options.act2_randomize_entrances == ShuffleTransitions.option_coupled else "",
                    self.player
                )

    def extend_hint_information(self, hint_data: dict[int, dict[int, str]]) -> None:
        if not self.options.act2_randomize_entrances:
            return

        hint_data.update({self.player: {}})

        all_state = self.multiworld.get_all_state(True)
        # sometimes some of my regions aren't in path for some reason?
        all_state.update_reachable_regions(self.player)
        paths = all_state.path
        start = self.get_region("Tower HQ")
        start_connections = [entrance.name for entrance in start.exits if entrance not in {"Home", "Shrink Down"}]
        transition_names = [transition.name for transition in self.transitions] + start_connections
        for loc in self.get_locations():
            if (loc.parent_region.name in {"Tower HQ", "The Shop", "Music Box", "The Craftsman's Corner"}
                    or loc.address is None):
                continue
            path_to_loc: list[str] = []
            name, connection = paths.get(loc.parent_region, (None, None))
            while connection != ("Menu", None) and name is not None:
                name, connection = connection
                if name in transition_names:
                    if name in start_connections:
                        name = f"{name} -> {self.get_entrance(name).connected_region.name}"
                    path_to_loc.append(name)

            text = " => ".join(reversed(path_to_loc))
            if not text:
                continue
            hint_data[self.player][loc.address] = text

    def fill_slot_data(self) -> Dict[str, Any]:
        return self.options.as_dict(
            "death_link",
            "act1_death_link_behaviour",
            "enable_act_1",
            "enable_act_2",
            "enable_act_3",
            "goal",
            "randomize_codes",
            "randomize_deck",
            "randomize_sigils",
            "extra_sigils",
            "randomize_hammer",
            "randomize_shortcuts",
            "randomize_vessel_upgrades",
            "optional_death_card",
            "skip_tutorial",
            "skip_epilogue",
            "epitaph_pieces_randomization"
        )
