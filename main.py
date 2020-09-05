from typing import Set
import json

from bundle import Bundle, save_base_bundles, load_base_bundles, save_user_bundles, load_user_bundles


def main():

    bundles: Set[Bundle]

    try:
        bundles = load_user_bundles()
        print(f"User bundle state loaded.")
    except OSError:
        bundles = load_base_bundles()
        print(f"No user data - base bundle data loaded.")

    while True:
        print(f"Bundles:")
        for i, bundle in enumerate(bundles):
            print(f"{i}: {bundle}")

        print(f"(a)dd items, a(d)d bundle, (q)uit: ")
        user_input = input(": ").lower().strip()

        if user_input == "q":
            break


if __name__ == '__main__':
    main()
