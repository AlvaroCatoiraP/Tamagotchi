from pathlib import Path
import json
def constructor(name : str) -> dict:
    """
        cunstruct the peth with attr 
        Args :
            name : str 
            the name of the pet 
        returns
            pet : dic
            a dictionary with the pet attr
    """
    pet = {
        "name": name,
        "life": 100, # 0 = death - 100 = full life 
        "hungry": 100, # 0 = no hungry - 100 = very hungry
        "happynes" : 100 # 0 sad - 100 happy
    }
    return pet

def save__update_Pet(pet:dict) -> bool:
    
    try:
        file = open(f"{pet["name"]}.data", "w")
        dump = json.dump(pet)
        json.load(file,dump)
    except:
        print("Un problema surgio al momento de abrir el archivo de datos del Tamagotchi")
