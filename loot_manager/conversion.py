from typing import Tuple, List
import sys
import glob
import shutil
import os
import PIL.Image


class LootComponents:

    weapons = [
        "Warhammer",  # 0
        "Quarterstaff",  # 1
        "Maul",  # 2
        "Mace",  # 3
        "Club",  # 4
        "Katana",  # 5
        "Falchion",  # 6
        "Scimitar",  # 7
        "Long Sword",  # 8
        "Short Sword",  # 9
        "Ghost Wand",  # 10
        "Grave Wand",  # 11
        "Bone Wand",  # 12
        "Wand",  # 13
        "Grimoire",  # 14
        "Chronicle",  # 15
        "Tome",  # 16
        "Book"  # 17
    ]
    weaponsLength = 18

    chestArmor = [
        "Divine Robe",  # 0
        "Silk Robe",  # 1
        "Linen Robe",  # 2
        "Robe",  # 3
        "Shirt",  # 4
        "Demon Husk",  # 5
        "Dragonskin Armor",  # 6
        "Studded Leather Armor",  # 7
        "Hard Leather Armor",  # 8
        "Leather Armor",  # 9
        "Holy Chestplate",  # 10
        "Ornate Chestplate",  # 11
        "Plate Mail",  # 12
        "Chain Mail",  # 13
        "Ring Mail"  # 14
    ]
    chestLength = 15

    headArmor = [
        "Ancient Helm",  # 0
        "Ornate Helm",  # 1
        "Great Helm",  # 2
        "Full Helm",  # 3
        "Helm",  # 4
        "Demon Crown",  # 5
        "Dragon's Crown",  # 6
        "War Cap",  # 7
        "Leather Cap",  # 8
        "Cap",  # 9
        "Crown",  # 10
        "Divine Hood",  # 11
        "Silk Hood",  # 12
        "Linen Hood",  # 13
        "Hood"  # 14
    ]
    headLength = 15

    waistArmor = [
        "Ornate Belt",  # 0
        "War Belt",  # 1
        "Plated Belt",  # 2
        "Mesh Belt",  # 3
        "Heavy Belt",  # 4
        "Demonhide Belt",  # 5
        "Dragonskin Belt",  # 6
        "Studded Leather Belt",  # 7
        "Hard Leather Belt",  # 8
        "Leather Belt",  # 9
        "Brightsilk Sash",  # 10
        "Silk Sash",  # 11
        "Wool Sash",  # 12
        "Linen Sash",  # 13
        "Sash"  # 14
    ]
    waistLength = 15

    footArmor = [
        "Holy Greaves",  # 0
        "Ornate Greaves",  # 1
        "Greaves",  # 2
        "Chain Boots",  # 3
        "Heavy Boots",  # 4
        "Demonhide Boots",  # 5
        "Dragonskin Boots",  # 6
        "Studded Leather Boots",  # 7
        "Hard Leather Boots",  # 8
        "Leather Boots",  # 9
        "Divine Slippers",  # 10
        "Silk Slippers",  # 11
        "Wool Shoes",  # 12
        "Linen Shoes",  # 13
        "Shoes"  # 14
    ]
    footLength = 15

    handArmor = [
        "Holy Gauntlets",  # 0
        "Ornate Gauntlets",  # 1
        "Gauntlets",  # 2
        "Chain Gloves",  # 3
        "Heavy Gloves",  # 4
        "Demon's Hands",  # 5
        "Dragonskin Gloves",  # 6
        "Studded Leather Gloves",  # 7
        "Hard Leather Gloves",  # 8
        "Leather Gloves",  # 9
        "Divine Gloves",  # 10
        "Silk Gloves",  # 11
        "Wool Gloves",  # 12
        "Linen Gloves",  # 13
        "Gloves"  # 14
    ]
    handLength = 15

    necklaces = [
        "Necklace",  # 0
        "Amulet",  # 1
        "Pendant"  # 2
    ]
    necklacesLength = 3

    rings = [
        "Gold Ring",  # 0
        "Silver Ring",  # 1
        "Bronze Ring",  # 2
        "Platinum Ring",  # 3
        "Titanium Ring"  # 4
    ]
    ringsLength = 5

    suffixes = [
        # <no suffix>          # 0
        "of Power",  # 1
        "of Giants",  # 2
        "of Titans",  # 3
        "of Skill",  # 4
        "of Perfection",  # 5
        "of Brilliance",  # 6
        "of Enlightenment",  # 7
        "of Protection",  # 8
        "of Anger",  # 9
        "of Rage",  # 10
        "of Fury",  # 11
        "of Vitriol",  # 12
        "of the Fox",  # 13
        "of Detection",  # 14
        "of Reflection",  # 15
        "of the Twins"  # 16
    ]
    suffixesLength = 16

    namePrefixes = [
        # <no name>            # 0
        "Agony",  # 1
        "Apocalypse",  # 2
        "Armageddon",  # 3
        "Beast",  # 4
        "Behemoth",  # 5
        "Blight",  # 6
        "Blood",  # 7
        "Bramble",  # 8
        "Brimstone",  # 9
        "Brood",  # 10
        "Carrion",  # 11
        "Cataclysm",  # 12
        "Chimeric",  # 13
        "Corpse",  # 14
        "Corruption",  # 15
        "Damnation",  # 16
        "Death",  # 17
        "Demon",  # 18
        "Dire",  # 19
        "Dragon",  # 20
        "Dread",  # 21
        "Doom",  # 22
        "Dusk",  # 23
        "Eagle",  # 24
        "Empyrean",  # 25
        "Fate",  # 26
        "Foe",  # 27
        "Gale",  # 28
        "Ghoul",  # 29
        "Gloom",  # 30
        "Glyph",  # 31
        "Golem",  # 32
        "Grim",  # 33
        "Hate",  # 34
        "Havoc",  # 35
        "Honour",  # 36
        "Horror",  # 37
        "Hypnotic",  # 38
        "Kraken",  # 39
        "Loath",  # 40
        "Maelstrom",  # 41
        "Mind",  # 42
        "Miracle",  # 43
        "Morbid",  # 44
        "Oblivion",  # 45
        "Onslaught",  # 46
        "Pain",  # 47
        "Pandemonium",  # 48
        "Phoenix",  # 49
        "Plague",  # 50
        "Rage",  # 51
        "Rapture",  # 52
        "Rune",  # 53
        "Skull",  # 54
        "Sol",  # 55
        "Soul",  # 56
        "Sorrow",  # 57
        "Spirit",  # 58
        "Storm",  # 59
        "Tempest",  # 60
        "Torment",  # 61
        "Vengeance",  # 62
        "Victory",  # 63
        "Viper",  # 64
        "Vortex",  # 65
        "Woe",  # 66
        "Wrath",  # 67
        "Light's",  # 68
        "Shimmering"  # 69
    ]
    namePrefixesLength = 69

    nameSuffixes = [
        # <no name>            # 0
        "Bane",  # 1
        "Root",  # 2
        "Bite",  # 3
        "Song",  # 4
        "Roar",  # 5
        "Grasp",  # 6
        "Instrument",  # 7
        "Glow",  # 8
        "Bender",  # 9
        "Shadow",  # 10
        "Whisper",  # 11
        "Shout",  # 12
        "Growl",  # 13
        "Tear",  # 14
        "Peak",  # 15
        "Form",  # 16
        "Sun",  # 17
        "Moon"  # 18
    ]
    nameSuffixesLength = 18

    armor_sets = {
        "Weapon": weapons,
        "Chest": chestArmor,
        "Head": headArmor,
        "Waist": waistArmor,
        "Foot": footArmor,
        "Hand": handArmor,
        "Neck": necklaces,
        "Ring": rings,
    }


def get_id_and_class(s: str) -> Tuple[int, str]:
    for k, v in LootComponents.armor_sets.items():
        for i, n in enumerate(v):
            if n in s:
                return i, k


def check_list(s: str, l: List) -> int:
    for i, n in enumerate(l):
        if n in s:
            return (i + 1, n)
    return (0, "")


def name_to_id(s: str, delimiter: str = "", debug=False) -> str:

    if debug:
        print("=========================================================")
        print(s)

    item_id, item_type_name = get_id_and_class(s)
    item_type_id = list(LootComponents.armor_sets).index(item_type_name)

    # get rid of dupes
    s = s.replace(LootComponents.armor_sets[item_type_name][item_id], "")

    suffix_id, suffix = check_list(s, LootComponents.suffixes)
    s = s.replace(suffix, "")

    name_prefix_id, name_prefix = check_list(s, LootComponents.namePrefixes)
    s = s.replace(name_prefix, "")
    name_suffix_id, name_suffix = check_list(s, LootComponents.nameSuffixes)
    s = s.replace(name_suffix, "")
    augmentation = ('1' in s) * 1

    ans = [
        item_type_id, item_id, suffix_id, name_prefix_id, name_suffix_id,
        augmentation
    ]
    ans_to_string = delimiter.join(f"{x:02d}" for x in ans)

    if debug:
        print(item_id, LootComponents.armor_sets[item_type_name][item_id])
        print(item_type_id, item_type_name)
        print(suffix_id, suffix)
        print(name_prefix_id, name_prefix)
        print(name_suffix_id, name_suffix)
        print(augmentation)

    return ans_to_string


def rename_dir(source_dir: str, target_dir: str, delimiter: str = ""):
    source_paths = glob.glob(f"{source_dir}/*.png")
    for p in source_paths:
        print(p.split("/")[-1])
        id = name_to_id(p.split("/")[-1], delimiter=delimiter, debug=True)
        shutil.copy(p, f"{target_dir}/{id}.png")


def overlay_dirs(source_dir_1: str, source_dir_2: str, target_dir: str,
                 alpha: float):
    source_paths = glob.glob(f"{source_dir_1}/*.png")
    for p in source_paths:
        print(".",end="")
        n = p.split("/")[-1]

        image_1 = PIL.Image.open(p)
        image_2 = PIL.Image.open(f"{source_dir_2}/{n}")
        blended = PIL.Image.blend(image_1, image_2, alpha=float(alpha))
        blended.save(f"{target_dir}/{n}")

def id_to_name(s : str, delimiter : str ="") -> str:
    if delimiter == "":
        ids = []
        while len(s) > 0:
            head, s = s[:2], s[2:]
            ids.append(head)
    else:
        ids = s.split(delimiter)

    item_type_name = list(LootComponents.armor_sets)[int(ids[0])]
    item_name = LootComponents.armor_sets[item_type_name][int(ids[1])]

    suffix_id = int(ids[2])
    if suffix_id > 0:
        suffix = LootComponents.suffixes[suffix_id-1]
    else:
        suffix = ""
    
    name_prefix_id = int(ids[3])
    if name_prefix_id > 0:
        name_prefix = '"' + LootComponents.namePrefixes[name_prefix_id-1]
    else:
        name_prefix = ""

    name_suffix_id = int(ids[4])
    if name_suffix_id > 0:
        name_suffix = LootComponents.nameSuffixes[name_suffix_id-1] + '"'
    else:
        name_suffix = ""

    augmentation = "" if int(ids[5]) == 0 else "+1"

    return " ".join([name_prefix, name_suffix, item_name, suffix, augmentation])


if __name__ == "__main__":
    """
    
    Example usage:
    - python conversion.py test
    - python conversion.py rename SOURCE_DIR TARGET_DIR [DELIMITER]
    - python conversion.py overlay SOURCE_DIR_1 SOURCE_DIR_2 TARGET_DIR ALPHA
    
    """
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            print(get_id_and_class("Shoes"))  # 14, Foot
            print(get_id_and_class("Dragonskin Belt"))  #6, Waist

            print(name_to_id("Dragonskin Belt", "_",
                             debug=True))  # '03_06_00_00_00_00'
            print(
                name_to_id('"Vengeance Tear" Divine Slippers of Giants',
                           "_",
                           debug=True))  # '04_10_02_62_14_00'
            print(
                name_to_id('"Vengeance Tear" Divine Slippers of Giants +1',
                           "_",
                           debug=True))  # '04_10_02_62_14_01'

            print(id_to_name('041002621401'))

        if sys.argv[1] == "rename":
            assert len(
                sys.argv
            ) >= 4, "need at least 3 args: rename source_dir target_dir [delimiter]"
            source_dir = sys.argv[2]
            target_dir = sys.argv[3]
            if len(sys.argv) > 4:
                delimiter = sys.argv[4]
            else:
                delimiter = ""

            assert os.path.exists(source_dir)
            if os.path.exists(target_dir):
                shutil.rmtree(target_dir)
            os.makedirs(target_dir)

            rename_dir(source_dir, target_dir, delimiter)

        if sys.argv[1] == "overlay":
            assert len(
                sys.argv
            ) >= 6, "need at least 5 args: rename source_dir_1 source_dir_2 target_dir alpha"
            source_dir_1 = sys.argv[2]
            source_dir_2 = sys.argv[3]
            target_dir = sys.argv[4]
            alpha = sys.argv[5]

            assert os.path.exists(source_dir_1)
            assert os.path.exists(source_dir_2)
            if os.path.exists(target_dir):
                shutil.rmtree(target_dir)
            os.makedirs(target_dir)

            overlay_dirs(source_dir_1, source_dir_2, target_dir, alpha)