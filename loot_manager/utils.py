import json
from pathlib import Path
import os.path
import glob

RESOURCES = Path("resources/")
CACHE_PATH = RESOURCES / "prompts_cache.json"


def get_prompts(item_class=None):
    """FLASK"""
    suffix = "_" + item_class if item_class != None else ""
    with open(RESOURCES / "prompts" / f"prompts{suffix}.json", "r") as file:
        prompts = json.load(file)
    return prompts

def pop_prompt(item_class=None):
    """FLASK"""
    if os.path.isfile(CACHE_PATH):
        with open(CACHE_PATH, "r") as file:
            prompts_stack = json.load(file)
    else:
        prompts_stack = get_prompts(item_class)

    n_prompts = len(prompts_stack)
    print(f"{n_prompts} remaining in prompts cache!")
    if n_prompts == 0:
        return None

    popped_prompt = None
    if item_class == None:
        popped_prompt = prompts_stack.pop(0)
        n_prompts -= 1
    else:
        for i in range(n_prompts):
            if prompts_stack[i][1] == item_class:
                popped_prompt = prompts_stack.pop(i)
                n_prompts -= 1
                break
    # if item_class is given and nothing is found, it will return None

    with open(CACHE_PATH, "w") as file:
        json.dump(prompts_stack, file)

    return popped_prompt, n_prompts

def clear_cache():
    """FLASK"""
    os.remove(CACHE_PATH)

# general utils

def get_templates():
    raw_paths = glob.glob("resources/templates/*")
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