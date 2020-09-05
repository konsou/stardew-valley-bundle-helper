from typing import Dict, Set
import json
import pickle


BASE_BUNDLES_FILE = "./bundles_base.json"
USER_BUNDLES_FILE = "./bundles_user.pkl"


def load_user_bundles() -> Set['Bundle']:
    with open(USER_BUNDLES_FILE, 'rb') as f:
        return pickle.load(f)


def save_user_bundles(bundles: Set['Bundle']):
    with open(USER_BUNDLES_FILE, 'wb') as f:
        pickle.dump(bundles, f)


def save_base_bundles(bundles: Set['Bundle']):
    json_string = "["

    for bundle in bundles:
        json_string = f"{json_string}\n{bundle.to_json_string()},"

    json_string = json_string[:-1]  # remove last comma
    json_string = f"{json_string}\n]"

    try:
        with open(BASE_BUNDLES_FILE, 'w') as f:
            f.write(json_string)
            print(f"Bundles saved")
    except OSError as e:
        print(f"ERROR SAVING ITEMS: {e}")


def load_base_bundles() -> Set['Bundle']:
    bundles = set()

    with open(BASE_BUNDLES_FILE) as f:
        loaded_bundles = json.load(f)
        for bundle in loaded_bundles:
            bundles.add(Bundle.from_json(bundle))

    return bundles


class Bundle:
    def __init__(self, name: str, slots_required: int):
        #  print(f"Add bundle {name} with {slots_required} slots required")
        self.name: str = name
        self.slots_required: int = slots_required
        self.slots_filled: int = 0
        self.items: Dict[str, int] = dict()
        self.items_remaining: Dict[str, int] = dict()

    def __str__(self) -> str:
        return f"{self.name} - {self.slots_filled}/{self.slots_required} slots - {self.items_remaining}"

    def __repr__(self) -> str:
        return f"<Bundle {self.name} - {self.slots_required} slots required - {len(self.items)} items>"

    def add_required_item(self, item: str, quantity: int = 1):
        #  print(f"Add {item} ({quantity}) to bundle {self.name}")
        self.items[item] = quantity
        self.items_remaining[item] = quantity

    def item_done(self, item: str, quantity: int = 1) -> bool:
        try:
            if self.items[item] <= quantity and self.items_remaining[item] <= quantity:
                del self.items_remaining[item]
                self.slots_filled += 1
                return True
        except KeyError:
            return False
        return False

    def is_finished(self) -> bool:
        if self.slots_filled >= self.slots_required:
            return True
        else:
            return False

    def to_json_string(self) -> str:
        return json.dumps(self.__dict__)

    @classmethod
    def from_json_string(cls, json_string: str) -> 'Bundle':
        return cls.from_json(json.loads(json_string))

    @classmethod
    def from_json(cls, json_data: Dict):
        new_bundle = Bundle(name=json_data['name'], slots_required=json_data['slots_required'])

        for item, quantity in json_data['items'].items():
            new_bundle.add_required_item(item=item, quantity=quantity)

        return new_bundle


if __name__ == '__main__':
    test_bundle = Bundle(name="test", slots_required=3)
    test_bundle.add_required_item("wood", 99)
    test_bundle.add_required_item("mudskipper")

    print(test_bundle.to_json_string())
    b2 = Bundle.from_json_string(test_bundle.to_json_string())
    print(b2.to_json_string())

    print(str(b2))
    b2.item_done("wood", 99)
    print(str(b2))
