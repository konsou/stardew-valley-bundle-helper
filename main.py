from typing import Set
import json

ITEMS_FILE = "./items.json"
BUNDLES_FILE = "./bundles.json"


def save_items(items: Set[str]):
    try:
        with open(ITEMS_FILE, 'w') as f:
            json.dump(list(items), f)
            print(f"Items saved")
    except OSError as e:
        print(f"ERROR SAVING ITEMS: {e}")


def save_bundles(bundles: Set[str]):
    try:
        with open(BUNDLES_FILE, 'w') as f:
            json.dump(list(bundles), f)
            print(f"Bundles saved")
    except OSError as e:
        print(f"ERROR SAVING ITEMS: {e}")


def main():
    items: Set[str] = set()
    bundles: Set[str] = set()

    try:
        with open(ITEMS_FILE) as f:
            items = set(json.load(f))
    except OSError as e:
        print(e)

    try:
        with open(BUNDLES_FILE) as f:
            bundles = set(json.load(f))
    except OSError as e:
        print(e)

    while True:
        print(f"Items:")
        print(items)

        print(f"(a)dd items, a(d)d bundle, (q)uit: ")
        user_input = input(": ").lower().strip()

        if user_input == "a":
            while True:
                item_to_add = input("Item to add (q to return): ").lower().strip()
                if item_to_add == "q":
                    break
                print(f"Adding item: {item_to_add}")
                items.add(item_to_add)
                save_items(items)

        elif user_input == "q":
            break


if __name__ == '__main__':
    main()
