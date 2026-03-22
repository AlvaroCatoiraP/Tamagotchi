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
    save__update_pet(pet)
    return pet

def save__update_pet(pet:dict) -> bool:
    
    try:
        file = open(f"{pet["name"]}.json", "w")
        json.dump(pet, file, indent=4)
    except:
        print("Un problema surgio al momento de abrir el archivo de datos del Tamagotchi")
    finally:
        file.close()

def load_pet() -> dict:
        try:
            with open(f"{name}.json", "r") as file:
                pet = json.load(file)
                return pet
        except Exception as e:
            print("Un problema surgio al momento de abrir el archivo de datos del Tamagotchi")

def minus_attr(minus :int, name:str, attr : str):

    try:
        with open(f"{name}.json", "r") as file:
            pet = json.load(file)
            if pet[attr] - minus >= 0  :
                pet[attr] = pet[attr] - minus
            
        with open(f"{name}.json", "w") as file:
            json.dump(pet,file,indent=4)

    except Exception as e:
        print("Un problema surgio al momento de abrir el archivo de datos del Tamagotchi")
    except KeyError:
        print("Atributo inexistente en los datos del tamagotchi")


def plus_attr(plus : int, name: str, attr : str):

    try:
        with open(f"{name}.json", "r") as file:
            pet = json.load(file)
            if pet[attr] + plus <= 100:
                pet[attr] = pet[attr] + plus
            
        with open(f"{name}.json", "w") as file:
            json.dump(pet,file,indent=4)

    except Exception as e:
        print("Un problema surgio al momento de abrir el archivo de datos del Tamagotchi")
    except KeyError:
        print("Atributo inexistente en los datos del tamagotchi")


pet = constructor("toto")
