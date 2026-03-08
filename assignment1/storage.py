import pickle
from pathlib import Path
from models import AddressBook


BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / "addressbook.pkl"


def save_data(book):
    with open(FILE_PATH, "wb") as f:
        pickle.dump(book, f)


def load_data():
    try:
        with open(FILE_PATH, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()