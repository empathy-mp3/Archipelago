from . import InscryptionTestBase
from ..Items import trap_items


TRAP_NAMES = {item["name"] for item in trap_items}


class OptionTestBase(InscryptionTestBase):
    def location_names(self):
        return [location.name for location in self.multiworld.get_unfilled_locations(self.player)]

    def pool_names(self):
        return [item.name for item in self.multiworld.itempool]

    def precollected_names(self):
        return [item.name for item in self.multiworld.precollected_items[self.player]]

    def assert_only_acts(self, *expected_acts: str) -> None:
        prefixes = {name.split(" - ")[0] for name in self.location_names()}
        self.assertEqual(prefixes, set(expected_acts))

    def assert_pool_matches_locations(self) -> None:
        self.assertEqual(len(self.pool_names()), len(self.location_names()))


class TestActOneOnly(OptionTestBase):
    options = {"enable_act_2": 0, "enable_act_3": 0}

    def test_only_act_1_is_generated(self) -> None:
        self.assert_only_acts("Act 1")
        self.assert_pool_matches_locations()


class TestActTwoOnly(OptionTestBase):
    options = {"enable_act_1": 0, "enable_act_3": 0}

    def test_only_act_2_is_generated(self) -> None:
        self.assert_only_acts("Act 2")
        self.assert_pool_matches_locations()


class TestActThreeOnly(OptionTestBase):
    options = {"enable_act_1": 0, "enable_act_2": 0}

    def test_only_act_3_is_generated(self) -> None:
        self.assert_only_acts("Act 3")
        self.assert_pool_matches_locations()


class TestTwoActsEnabled(OptionTestBase):
    options = {"enable_act_3": 0}

    def test_only_enabled_acts_are_generated(self) -> None:
        self.assert_only_acts("Act 1", "Act 2")
        self.assert_pool_matches_locations()


class TestActUnlocksOpen(OptionTestBase):
    options = {"act_unlocks": 1}

    def test_no_act_items_exist(self) -> None:
        self.assertEqual([n for n in self.pool_names() if n in ("Act 1", "Act 2", "Act 3")], [])
        self.assertEqual(self.precollected_names(), [])


class TestActUnlocksItemsStartingActOne(OptionTestBase):
    options = {"act_unlocks": 2, "starting_act": 0}

    def test_starting_act_is_precollected_and_others_are_in_pool(self) -> None:
        self.assertIn("Act 1", self.precollected_names())
        pool = self.pool_names()
        self.assertNotIn("Act 1", pool)
        self.assertIn("Act 2", pool)
        self.assertIn("Act 3", pool)


class TestActUnlocksItemsStartingActTwo(OptionTestBase):
    options = {"act_unlocks": 2, "starting_act": 1}

    def test_starting_act_is_precollected_and_others_are_in_pool(self) -> None:
        self.assertIn("Act 2", self.precollected_names())
        pool = self.pool_names()
        self.assertNotIn("Act 2", pool)
        self.assertIn("Act 1", pool)
        self.assertIn("Act 3", pool)


class TestActUnlocksItemsStartingActDisabled(OptionTestBase):
    options = {"act_unlocks": 2, "starting_act": 0, "enable_act_1": 0}

    def test_starting_act_falls_back_to_an_enabled_act(self) -> None:
        precollected = self.precollected_names()
        self.assertEqual(len(precollected), 1)
        self.assertIn(precollected[0], ("Act 2", "Act 3"))
        self.assertNotIn("Act 1", self.pool_names())


class TestHammerVanilla(OptionTestBase):
    options = {"randomize_hammer": 0}

    def test_hammer_is_not_an_item(self) -> None:
        self.assertNotIn("Hammer", self.pool_names())


class TestHammerRandomized(OptionTestBase):
    options = {"randomize_hammer": 1}

    def test_hammer_is_an_item(self) -> None:
        self.assertIn("Hammer", self.pool_names())


class TestHammerRemoved(OptionTestBase):
    options = {"randomize_hammer": 2}

    def test_hammer_is_not_an_item(self) -> None:
        self.assertNotIn("Hammer", self.pool_names())


class TestRandomizeNodes(OptionTestBase):
    options = {"randomize_nodes": 1}

    def test_adds_locations_and_pool_still_fits(self) -> None:
        self.assert_pool_matches_locations()
        self.assertGreater(len(self.location_names()), 100)


class TestRandomizeChallenges(OptionTestBase):
    options = {"randomize_challenges": 2}

    def test_adds_locations_and_pool_still_fits(self) -> None:
        self.assert_pool_matches_locations()
        self.assertGreater(len(self.location_names()), 100)


class TestRandomizeChallengesNoGrizzlies(OptionTestBase):
    options = {"randomize_challenges": 1}

    def test_pool_still_fits(self) -> None:
        self.assert_pool_matches_locations()


class TestRandomizeShortcuts(OptionTestBase):
    options = {"randomize_shortcuts": 1}

    def test_adds_locations_and_pool_still_fits(self) -> None:
        self.assert_pool_matches_locations()
        self.assertGreater(len(self.location_names()), 100)


class TestRandomizeVesselUpgrades(OptionTestBase):
    options = {"randomize_vessel_upgrades": 1}

    def test_adds_locations_and_pool_still_fits(self) -> None:
        self.assert_pool_matches_locations()
        self.assertGreater(len(self.location_names()), 100)


class TestAct3Overhaul(OptionTestBase):
    options = {"act3_overhaul": 1}

    def test_adds_a_location_and_pool_still_fits(self) -> None:
        self.assert_pool_matches_locations()
        self.assertGreater(len(self.location_names()), 100)


class TestAct2RandomizeBridge(OptionTestBase):
    options = {"act2_randomize_bridge": 1}

    def test_pool_still_fits(self) -> None:
        self.assert_pool_matches_locations()


class TestExtraSigils(OptionTestBase):
    options = {"extra_sigils": 1}

    def test_pool_still_fits(self) -> None:
        self.assert_pool_matches_locations()


class TestAllRandomizationEnabled(OptionTestBase):
    options = {
        "randomize_nodes": 1,
        "randomize_challenges": 2,
        "randomize_shortcuts": 1,
        "randomize_vessel_upgrades": 1,
        "randomize_hammer": 1,
        "act2_randomize_bridge": 1,
        "act3_overhaul": 1,
        "extra_sigils": 1,
    }

    def test_every_location_is_generated(self) -> None:
        self.assert_pool_matches_locations()
        self.assertEqual(len(self.location_names()), len(self.multiworld.worlds[self.player].all_locations))


class TestNoTraps(OptionTestBase):
    options = {"trap_chance": 0}

    def test_no_traps_are_generated(self) -> None:
        self.assertEqual([n for n in self.pool_names() if n in TRAP_NAMES], [])


class TestAllTraps(OptionTestBase):
    options = {"trap_chance": 100}

    def test_traps_replace_filler(self) -> None:
        self.assertGreater(len([n for n in self.pool_names() if n in TRAP_NAMES]), 0)
        self.assert_pool_matches_locations()


class TestSingleTrapType(OptionTestBase):
    options = {
        "trap_chance": 100,
        "trap_type_weights": {"Bleach Trap": 1, "Trash Trap": 0,
                              "Deck Size Trap": 0, "Reinforcements Trap": 0},
    }

    def test_only_the_weighted_trap_is_generated(self) -> None:
        traps = {n for n in self.pool_names() if n in TRAP_NAMES}
        self.assertEqual(traps, {"Bleach Trap"})
