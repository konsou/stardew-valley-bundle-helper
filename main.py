from typing import Set
import json

from bundle import Bundle

ITEMS_FILE = "./items.json"
BUNDLES_FILE = "./bundles.json"


def save_items(items: Set[str]):
    try:
        with open(ITEMS_FILE, 'w') as f:
            json.dump(sorted(items), f, indent=4)
            print(f"Items saved")
    except OSError as e:
        print(f"ERROR SAVING ITEMS: {e}")


def save_bundles(bundles: Set[Bundle]):
    json_string = "["

    for bundle in bundles:
        json_string = f"{json_string}\n{bundle.to_json_string()},"

    json_string = json_string[:-1]  # remove last comma
    json_string = f"{json_string}\n]"

    try:
        with open(BUNDLES_FILE, 'w') as f:
            f.write(json_string)
            print(f"Bundles saved")
    except OSError as e:
        print(f"ERROR SAVING ITEMS: {e}")


def main():
    items: Set[str] = set()
    bundles: Set[Bundle] = set()

    try:
        with open(ITEMS_FILE) as f:
            items = set(json.load(f))
    except OSError as e:
        print(e)

    try:
        with open(BUNDLES_FILE) as f:
            loaded_bundles = json.load(f)
            print(loaded_bundles)
            for bundle in loaded_bundles:
                print(bundle)
                bundles.add(Bundle.from_json(bundle))
    except OSError as e:
        print(e)

    while True:
        print(f"Bundles:")
        for i, bundle in enumerate(bundles):
            print(f"{i}: {bundle}")

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

        elif user_input == "d":
            while True:
                bundle_name = input("Bundle name (q to return): ").lower().strip()
                if bundle_name == "q":
                    break
                slots_required = int(input("Slots required: "))

                new_bundle = Bundle(name=bundle_name, slots_required=slots_required)

                while True:
                    item_to_add = input("Item to add (q to return): ").lower().strip()
                    if item_to_add == "q":
                        break
                    quantity = input("How many needed? (default 1): ")
                    try:
                        quantity = int(quantity)
                    except ValueError:
                        quantity = 1

                    new_bundle.add_required_item(item=item_to_add, quantity=quantity)

                bundles.add(new_bundle)
                save_bundles(bundles)

        elif user_input == "q":
            break


if __name__ == '__main__':
    main()
