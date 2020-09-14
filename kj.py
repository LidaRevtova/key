import os
import tempfile
import json
import argparse



parser = argparse.ArgumentParser()
parser.add_argument("--key", help="key name")
parser.add_argument("--value", help="val value")
args = parser.parse_args()
if args.key is None:
    print("None")



def open_file():
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'w') as f:
            readJson = {"keys": [], "values": {}}
            json.dump(readJson, f)


def read_storage(file_name):
    with open(file_name) as f:
        storage = json.load(f)
    return storage


def save_storage(storage, file_name):
    with open(file_name, 'w') as f:
        json.dump(storage, f)
    #return storage

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-key", "-k", type=str, help="parameters - key. type - str")
    parser.add_argument("-value", "-v", type=str, help="parameters - value. type - str")

    args = parser.parse_args()
    if args.key is None:
        print("Error. -key is not defined")
        return
    _key = str(args.key)
    _value = args.value
    Actions(_key, _value)