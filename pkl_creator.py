import pickle

successful_guesses = {}

def create_pkl():
    with open("successful_guesses.pkl", "wb") as f:
        pickle.dump(successful_guesses, f)

def check_file():
    try:
        with open("successful_guesses.pkl", "rb") as f:
            pass
    except FileNotFoundError:
        create_pkl()

def read_guesses():
    with open("successful_guesses.pkl", "rb") as f:
        while True:
            try:
                data = pickle.load(f)
            except EOFError:
                break
        return data
    
check_file()