from entrance_rando import EntranceType

connections: dict[str, dict[str, EntranceType]] = {
    "Starting Island": {
        "Starting Island Exit": EntranceType.TWO_WAY
    },
    "World Map Right": {
        "World Map Starting Island": EntranceType.TWO_WAY,
        "World Map Docks": EntranceType.TWO_WAY,
        "World Map Mycologists' Hut": EntranceType.TWO_WAY,
        "World Map Crypt": EntranceType.TWO_WAY
    },
    "World Map Left": {
        "World Map Factory": EntranceType.TWO_WAY,
        "World Map Tower": EntranceType.TWO_WAY
    },
    "Docks": {
        "Docks Exit": EntranceType.TWO_WAY
    },
    "Mycologists' Hut": {
        "Mycologists' Hut Exit": EntranceType.TWO_WAY
    },
    "Forest": {
        "Forest Exit": EntranceType.TWO_WAY,
        "Forest Past Prospector": EntranceType.ONE_WAY,
        "Forest Past Angler": EntranceType.TWO_WAY,
        "Forest Cabin Entrance": EntranceType.TWO_WAY
    },
    "Pond": {
        "Pond Exit": EntranceType.TWO_WAY,
        "Pond Hidden Path": EntranceType.TWO_WAY
    },
    "Pond OLD_DATA Room": {
        "Pond OLD_DATA Room Exit": EntranceType.TWO_WAY
    },
    "Meadow": {
        "Meadow Exit": EntranceType.TWO_WAY,
        "Meadow Hidden Path": EntranceType.TWO_WAY
    },
    "Woodcarver Room": {
        "Woodcarver Room Exit": EntranceType.TWO_WAY
    },
    "Cabin": {
        "Cabin Exit": EntranceType.TWO_WAY,
        "Cabin Shop Entrance": EntranceType.TWO_WAY
    },
    "Cabin Shop": {
        "Cabin Shop Exit": EntranceType.TWO_WAY
    },
    "Crypt": {
        "Crypt Exit": EntranceType.TWO_WAY,
        "Crypt Shop Entrance": EntranceType.TWO_WAY,
        "Crypt Mirror Room Entrance": EntranceType.TWO_WAY,
        "Crypt Basement Entrance": EntranceType.TWO_WAY
    },
    "Crypt Shop": {
        "Crypt Shop Exit": EntranceType.TWO_WAY
    },
    "Crypt Mirror Room": {
        "Crypt Mirror Room Exit": EntranceType.TWO_WAY
    },
    "Crypt Basement": {
        "Crypt Basement Exit": EntranceType.TWO_WAY,
        "Crypt Basement Bone Lord Stairs": EntranceType.ONE_WAY
    },
    "Bone Lord Stairs": {
        "Bone Lord Stairs Down": EntranceType.TWO_WAY,
        "Bone Lord Stairs Up": EntranceType.TWO_WAY
    },
    "Lower Bone Lord Room": {
        "Lower Bone Lord Room Exit Stairs": EntranceType.TWO_WAY,
        "Lower Bone Lord Room to Upper": EntranceType.TWO_WAY,
    },
    "Upper Bone Lord Room": {
        "Upper Bone Lord Room to Lower": EntranceType.TWO_WAY
    },
    "Factory": {
        "Factory Exit": EntranceType.TWO_WAY,
        "Factory Shop Entrance": EntranceType.TWO_WAY,
        "Factory to Inspection Room": EntranceType.TWO_WAY,
    },
    "Factory Shop": {
        "Factory Shop Exit": EntranceType.TWO_WAY
    },
    "Inspection Room": {
        "Inspection Room Exit": EntranceType.TWO_WAY,
        "Inspection Room to Smelting Room": EntranceType.TWO_WAY
    },
    "Smelting Room": {
        "Smelting Room Exit": EntranceType.TWO_WAY,
        "Smelting Room Elevator Down": EntranceType.TWO_WAY,
    },
    "Dredging Room": {
        "Dredging Room Elevator Up": EntranceType.TWO_WAY
    },
    "Tower 1st Floor": {
        "Tower 1st Floor Exit": EntranceType.TWO_WAY,
        "Tower 1st Floor Shop Entrance": EntranceType.TWO_WAY,
        "Tower 1st Floor Back Room Left Entrance": EntranceType.TWO_WAY,
        "Tower 1st Floor Green Gem": EntranceType.TWO_WAY,
        "Tower 1st Floor Stairs Up": EntranceType.ONE_WAY
    },
    "Tower 1st Floor Behind Books": {
        "Tower 1st Floor Back Room Right Entrance": EntranceType.TWO_WAY
    },
    "Tower Shop": {
        "Tower Shop Exit": EntranceType.TWO_WAY
    },
    "Tower OLD_DATA Room": {
        "Tower OLD_DATA Room Left Exit": EntranceType.TWO_WAY,
        "Tower OLD_DATA Room Right Exit": EntranceType.TWO_WAY
    },
    "Goobert's Plane": {
        "Goobert's Plane Exit": EntranceType.TWO_WAY
    },
    "Tower 2nd Floor": {
        "Tower 2nd Floor Stairs Down": EntranceType.TWO_WAY,
        "Tower 2nd Floor Drop Down": EntranceType.TWO_WAY,
        "Tower 2nd Floor Orange Gem": EntranceType.TWO_WAY,
        "Tower 2nd Floor Stairs Up": EntranceType.ONE_WAY
    },
    "Pike Mage's Plane": {
        "Pike Mage's Plane Exit": EntranceType.TWO_WAY
    },
    "Tower 3rd Floor": {
        "Tower 3rd Floor Stairs Down": EntranceType.TWO_WAY,
        "Tower 3rd Floor Drop Down": EntranceType.TWO_WAY,
        "Tower 3rd Floor Back Room Left Entrance": EntranceType.TWO_WAY,
        "Tower 3rd Floor Back Room Right Entrance": EntranceType.TWO_WAY,
        "Tower 3rd Floor Blue Gem": EntranceType.TWO_WAY,
        "Tower 3rd Floor Stairs Up": EntranceType.ONE_WAY
    },
    "Tower Dark Room": {
        "Tower 3rd Floor Back Room Left Entrance": EntranceType.TWO_WAY,
        "Tower 3rd Floor Back Room Right Entrance": EntranceType.TWO_WAY
    },
    "Lonely Wizard's Plane": {
        "Lonely Wizard's Plane Exit": EntranceType.TWO_WAY
    },
    "Tower 4th Floor": {
        "Tower 4th Floor Stairs Down": EntranceType.TWO_WAY,
        "Tower 4th Floor Bathroom Entrance": EntranceType.TWO_WAY
    },
    "Tower Bathroom": {
        "Tower Bathroom Exit": EntranceType.TWO_WAY
    }
}

randomized_connections: dict[str, str] = {
    "Starting Island Exit":                     "World Map Starting Island",
    "World Map Docks":                          "Docks Exit",
    "World Map Mycologists' Hut":               "Mycologists' Hut Exit",
    "World Map Forest":                         "Forest Exit",
    "Forest Past Prospector":                   "Pond Exit",
    "Pond Hidden Path":                         "Pond OLD_DATA Room Exit",
    "Forest Past Angler":                       "Meadow Exit",
    "Meadow Hidden Path":                       "Woodcarver Room Exit",
    "Forest Cabin Entrance":                    "Cabin Exit",
    "Cabin Shop Entrance":                      "Cabin Shop Exit",
    "World Map Crypt":                          "Crypt Exit",
    "Crypt Shop Entrance":                      "Crypt Shop Exit",
    "Crypt Mirror Room Entrance":               "Crypt Mirror Room Exit",
    "Crypt Basement Entrance":                  "Crypt Basement Exit",
    "Crypt Basement Bone Lord Stairs":          "Bone Lord Stairs Down",
    "Bone Lord Stairs Up":                      "Lower Bone Lord Room Exit Stairs",
    "Lower Bone Lord Room to Upper":            "Upper Bone Lord Room to Lower",
    "World Map Factory":                        "Factory Exit",
    "Factory Shop Entrance":                    "Factory Shop Exit",
    "Factory to Inspection Room":               "Inspection Room Exit",
    "Inspection Room to Smelting Room":         "Smelting Room Exit",
    "Smelting Room Elevator Down":              "Dredging Room Elevator Up",
    "World Map Tower":                          "Tower 1st Floor Exit",
    "Tower 1st Floor Shop Entrance":            "Tower Shop Exit",
    "Tower 1st Floor Back Room Left Entrance":  "Tower OLD_DATA Room Left Exit",
    "Tower 1st Floor Back Room Right Entrance": "Tower OLD_DATA Room Right Exit",
    "Tower 1st Floor Green Gem":                "Goobert's Plane Exit",
    "Tower 1st Floor Stairs Up":                "Tower 2nd Floor Stairs Down",
    "Tower 2nd Floor Drop Down":                "Tower 2nd Floor Orange Gem",
    "Pike Mage's Plane Exit":                   "Tower 2nd Floor Stairs Up",
    "Tower 3rd Floor Stairs Down":              "Tower 3rd Floor Drop Down",
    "Tower 3rd Floor Back Room Left Entrance":  "Tower Dark Room Left Exit",
    "Tower 3rd Floor Back Room Right Entrance": "Tower Dark Room Right Exit",
    "Tower 3rd Floor Blue Gem":                 "Lonely Wizard's Plane Exit",
    "Tower 3rd Floor Stairs Up":                "Tower 4th Floor Stairs Down",
    "Tower 4th Floor Bathroom Entrance":        "Tower Bathroom Exit",
}

transitions: list[str] = [
        "Starting Island Exit",
        "World Map Starting Island",
        "World Map Docks",
        "Docks Exit",
        "World Map Mycologists' Hut",
        "Mycologists' Hut Exit",
        "World Map Forest",
        "Forest Exit",
        "Forest Past Prospector",
        "Pond Exit",
        "Pond Hidden Path",
        "Pond OLD_DATA Room Exit",
        "Forest Past Angler",
        "Meadow Exit",
        "Meadow Hidden Path",
        "Woodcarver Room Exit",
        "Forest Cabin Entrance",
        "Cabin Exit",
        "Cabin Shop Entrance",
        "Cabin Shop Exit",
        "World Map Crypt",
        "Crypt Exit",
        "Crypt Shop Entrance",
        "Crypt Shop Exit",
        "Crypt Mirror Room Entrance",
        "Crypt Mirror Room Exit",
        "Crypt Basement Entrance",
        "Crypt Basement Exit",
        "Crypt Basement Bone Lord Stairs",
        "Bone Lord Stairs Down",
        "Bone Lord Stairs Up",
        "Lower Bone Lord Room Exit Stairs",
        "Lower Bone Lord Room to Upper",
        "Upper Bone Lord Room to Lower",
        "World Map Factory",
        "Factory Exit",
        "Factory Shop Entrance",
        "Factory Shop Exit",
        "Factory to Inspection Room",
        "Inspection Room Exit",
        "Inspection Room to Smelting Room",
        "Smelting Room Exit",
        "Smelting Room Elevator Down",
        "Dredging Room Elevator Up",
        "World Map Tower",
        "Tower 1st Floor Exit",
        "Tower 1st Floor Shop Entrance",
        "Tower Shop Exit",
        "Tower 1st Floor Back Room Left Entrance",
        "Tower OLD_DATA Room Left Exit",
        "Tower 1st Floor Back Room Right Entrance",
        "Tower OLD_DATA Room Right Exit",
        "Tower 1st Floor Green Gem",
        "Goobert's Plane Exit",
        "Tower 1st Floor Stairs Up",
        "Tower 2nd Floor Stairs Down",
        "Tower 2nd Floor Drop Down",
        "Tower 2nd Floor Orange Gem",
        "Pike Mage's Plane Exit",
        "Tower 2nd Floor Stairs Up",
        "Tower 3rd Floor Stairs Down",
        "Tower 3rd Floor Drop Down",
        "Tower 3rd Floor Back Room Left Entrance",
        "Tower Dark Room Left Exit",
        "Tower 3rd Floor Back Room Right Entrance",
        "Tower Dark Room Right Exit",
        "Tower 3rd Floor Blue Gem",
        "Lonely Wizard's Plane Exit",
        "Tower 3rd Floor Stairs Up",
        "Tower 4th Floor Stairs Down",
        "Tower 4th Floor Bathroom Entrance",
        "Tower Bathroom Exit",
]
