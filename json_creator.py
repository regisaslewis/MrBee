import json

successful_guesses = '{}'

def create_json():
    with open("sg_db.json", "w") as f:
        json.dump(successful_guesses, f)

def check_file():
    try:
        with open("sg_db.json", "r") as f:
            pass
    except FileNotFoundError:
        create_json()

def read_guesses():
    with open("sg_db.json", "r") as f:
        data = json.load(f)
        return data
    
check_file()
python_dict = json.loads(read_guesses())
print(python_dict)