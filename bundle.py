from typing import Dict
import json


class Bundle:
    def __init__(self, name: str, slots_required: int):
        print(f"Add bundle {name} with {slots_required} slots required")
        self.name: str = name
        self.slots_required: int = slots_required
        self.items: Dict[str, int] = dict()

    def __str__(self) -> str:
        return f"{self.name} - {self.slots_required} slots required - {self.items}"

    def __repr__(self) -> str:
        return f"<Bundle {self.name} - {self.slots_required} slots required - {len(self.items)} items>"

    def add_item(self, item: str, quantity: int = 1):
        #  print(f"Add {item} ({quantity}) to bundle {self.name}")
        self.items[item] = quantity

    def to_json_string(self) -> str:
        return json.dumps(self.__dict__)

    @classmethod
    def from_json_string(cls, json_string: str) -> 'Bundle':
        return cls.from_json(json.loads(json_string))

    @classmethod
    def from_json(cls, json_data: Dict):
        new_bundle = Bundle(name=json_data['name'], slots_required=json_data['slots_required'])

        for item, quantity in json_data['items'].items():
            new_bundle.add_item(item=item, quantity=quantity)

        return new_bundle


if __name__ == '__main__':
    test_bundle = Bundle(name="test", slots_required=3)
    test_bundle.add_item("wood", 99)
    test_bundle.add_item("mudskipper")

    print(test_bundle.to_json_string())
    b2 = Bundle.from_json_string(test_bundle.to_json_string())
    print(b2.to_json_string())

    print(b2)
