from typing import Set

from tabulate import tabulate

from bundle import Bundle, save_base_bundles, load_base_bundles, save_user_bundles, load_user_bundles, needed_items, find_by_name


def main():
    try:
        bundles: Set[Bundle] = load_user_bundles()
        print(f"User bundle state loaded.")
    except OSError:
        bundles: Set[Bundle] = load_base_bundles()
        print(f"No user data - base bundle data loaded.")

    while True:
        print(f"Needed items:")
        needed_items_ = needed_items(bundles)

        print(tabulate(needed_items_, showindex=True))
        # for i, needed in enumerate(needed_items(bundles)):
        #     print(f"{i}: {needed[0]} ({needed[1]}) - {needed[2]}")

        print(f"(a)dd items, a(d)d bundle, (q)uit: ")
        user_input = input(": ").lower().strip()

        try:
            user_input = int(user_input)

            selected_item = needed_items_[user_input]
            print(selected_item)

            in_bundle = find_by_name(selected_item[2], bundles)
            print(f"In bundle {in_bundle}")

            result = in_bundle.item_done(item=selected_item[0], quantity=selected_item[1])

            if result:
                print(f"Marked as done!")
            else:
                print(f"ERROR! Wrong item and/or quantity!")

            save_user_bundles(bundles)

            input(f"Press ENTER to continue...")

        except ValueError:
            pass

        if user_input == "q":
            break


if __name__ == '__main__':
    main()
