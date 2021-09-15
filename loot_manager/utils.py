import json
from pathlib import Path
import glob

# supposed to be called one level higher than the repo!
RESOURCES = Path("loot_manager/resources/")
CACHE_PATH = RESOURCES / "prompts_cache.json"

def get_prompts(item_class=None):
    suffix = "_" + item_class if item_class != None else ""
    with open(RESOURCES / f"prompts{suffix}.json", "r") as file:
        prompts = json.load(file)
    return prompts

def get_templates():
    raw_paths = glob.glob("loot_manager/resources/templates/*")
    templates = {x.split("/")[-1][:-4].replace("_"," ") : x for x in raw_paths}
    return templates

def prompt_to_class_and_template(prompt):
    templates = get_templates()
    candidate = ''
    for t in templates:
        if t.lower() in prompt.lower():
            if len(t) > len(candidate):
                candidate = t
    return candidate, templates[candidate]

def get_item_classes():
    with open("loot_manager/resources/classes.json", "r") as file:
        item_classes = json.load(file)
    return item_classes
