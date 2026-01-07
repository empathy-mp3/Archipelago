from dataclasses import dataclass

from Options import Toggle, Choice, DeathLinkMixin, StartInventoryPool, PerGameCommonOptions, DefaultOnToggle, OptionSet


class Act1DeathLinkBehaviour(Choice):
    """If DeathLink is enabled, determines what counts as a death in act 1. This affects deaths sent and received.

    - Sacrificed: Send a death when sacrificed by Leshy. Receiving a death will extinguish all candles.

    - Candle Extinguished: Send a death when a candle is extinguished. Receiving a death will extinguish a candle."""
    display_name = "Act 1 Death Link Behaviour"
    option_sacrificed = 0
    option_candle_extinguished = 1
    default = 0


class EnableAct1(DefaultOnToggle):
    """Play Act 1 in the randomizer."""
    display_name = "Enable Act 1"

class EnableAct2(DefaultOnToggle):
    """Play Act 2 in the randomizer."""
    display_name = "Enable Act 2"

class EnableAct3(DefaultOnToggle):
    """Play Act 3 in the randomizer."""
    display_name = "Enable Act 3"


class Goal(Choice):
    """Defines the goal to accomplish in order to complete the randomizer.

    - Acts In Order: Complete each enabled act in order. You can return to previously completed acts.

    - Acts Any Order: Complete each enabled act in any order. All enabled acts are available from the start."""
    display_name = "Goal"
    option_acts_in_order = 0
    option_acts_any_order = 1
    default = 0


class RandomizeCodes(Toggle):
    """Randomize codes and passwords in the game (clocks, safes, etc.)"""
    display_name = "Randomize Codes"


class RandomizeDeck(Choice):
    """Randomize cards in your deck into new cards.
    Disable: Disable the feature.

    - Every Encounter Within Same Type: Randomize cards within the same type every encounter (keep rarity/scrybe type).

    - Every Encounter Any Type: Randomize cards into any possible card every encounter.

    - Starting Only: Only randomize cards given at the beginning of runs and acts."""
    display_name = "Randomize Deck"
    option_disable = 0
    option_every_encounter_within_same_type = 1
    option_every_encounter_any_type = 2
    option_starting_only = 3
    default = 0


class RandomizeSigils(Choice):
    """Randomize sigils printed on the cards into new sigils.

    - Disable: Disable the feature.

    - Randomize Addons: Every encounter, randomize sigils added from sacrifices or other means.

    - Randomize All: Every encounter, randomize all sigils.
    
    - Randomize Once: When a new card is obtained, randomize its sigils. In Act 2, every copy of the same card will have the same randomized sigils."""
    display_name = "Randomize Abilities"
    option_disable = 0
    option_randomize_addons = 1
    option_randomize_all = 2
    option_randomize_once = 3
    default = 0


class ExtraSigils(Toggle):
    """Allow extra sigils to show up in Act 1 and 3.
    These include sigils from other acts, Kaycee's Mod, or just new ones from the same act.
    Some very strong sigils will not show up.
    There may be an unusual lack of information given by these sigils."""
    display_name = "Extra Sigils"


class RandomizeHammer(Choice):
    """Instead of starting with the hammer in Act 2 and 3, it's an item that needs to be found first.

    - Vanilla: Start with the hammer, as normal.

    - Randomize: The hammer needs to be found in the randomizer.

    - Remove: Remove the hammer entirely."""
    display_name = "Randomize Hammer"
    option_vanilla = 0
    option_randomize = 1
    option_remove = 2
    default = 0


class RandomizeShortcuts(Choice):
    """The 3 shortcuts opened by NPCs in Botopia can be randomized, and have locations.

    - Vanilla: You open them normally by talking to the NPCs

    - Randomize: There's items that open the shortcuts, and locations for talking to the NPCs.

    - Open: They start open, and there's still locations for them. For a faster Act 3 experience."""
    display_name = "Randomize Shortcuts"
    option_vanilla = 0
    option_randomize = 1
    option_open = 2
    default = 0


class RandomizeVesselUpgrades(Choice):
    """The 3 Vessel Upgrades from Uberbots and the Conduit Upgrade can be randomized, and have locations.
    These will give your vessels a random beneficial (but not broken) sigil, including those not in the normal options.

    - Vanilla: You gain them normally, by picking them up from bosses.

    - Randomize: Your vessels are upgraded instantly upon receiving a Vessel Upgrade, and there's locations for them.

    - Remove One: Same as randomize, but there's one less upgrade in the pool."""
    display_name = "Randomize Vessel Upgrades"
    option_vanilla = 0
    option_randomize = 1
    option_remove_one = 2
    default = 0


class OptionalDeathCard(Choice):
    """Add a moment after death in act 1 where you can decide to create a death card or not.

    - Disable: Disable the feature.

    - Always On: The choice is always offered after losing all candles.

    - DeathLink Only: The choice is only offered after receiving a DeathLink event."""
    display_name = "Optional Death Card"
    option_disable = 0
    option_always_on = 1
    option_deathlink_only = 2
    default = 2


class SkipTutorial(DefaultOnToggle):
    """Skips the first few tutorial runs of act 1. Bones are available from the start."""
    display_name = "Skip Tutorial"


class SkipEpilogue(Toggle):
    """Completes the goal as soon as the required acts are completed without the need of completing the epilogue."""
    display_name = "Skip Epilogue"


class EpitaphPiecesRandomization(Choice):
    """Determines how epitaph pieces in act 2 are randomized. This can affect your chances of getting stuck.

    - All Pieces: Randomizes all nine pieces as their own item.

    - In Groups: Randomizes pieces in groups of three.

    - As One Item: Group all nine pieces as a single item."""
    display_name = "Epitaph Pieces Randomization"
    option_all_pieces = 0
    option_in_groups = 1
    option_as_one_item = 2
    default = 0


class PaintingChecksBalancing(Choice):
    """Generation options for the second and third painting checks in act 1.

    - None: Adds no progression logic to these painting checks. They will all count as sphere 1 (early game checks).

    - Balanced: Adds rules to these painting checks. Early game items are less likely to appear into these paintings.

    - Force Filler: For when you dislike doing these last two paintings. Their checks will only contain filler items."""
    display_name = "Painting Checks Balancing"
    option_none = 0
    option_balanced = 1
    option_force_filler = 2
    default = 1


@dataclass
class InscryptionOptions(DeathLinkMixin, PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    act1_death_link_behaviour: Act1DeathLinkBehaviour
    enable_act_1: EnableAct1
    enable_act_2: EnableAct2
    enable_act_3: EnableAct3
    goal: Goal
    randomize_codes: RandomizeCodes
    randomize_deck: RandomizeDeck
    randomize_sigils: RandomizeSigils
    extra_sigils: ExtraSigils
    randomize_hammer: RandomizeHammer
    randomize_shortcuts: RandomizeShortcuts
    randomize_vessel_upgrades: RandomizeVesselUpgrades
    optional_death_card: OptionalDeathCard
    skip_tutorial: SkipTutorial
    skip_epilogue: SkipEpilogue
    epitaph_pieces_randomization: EpitaphPiecesRandomization
    painting_checks_balancing: PaintingChecksBalancing
