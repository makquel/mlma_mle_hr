from components import Item
from utils import generate_item
from structs import Buffer


def main():
    data_structure = Buffer("FIFO")

    print("<<Generating random items>>")
    items = [Item(*generate_item()) for _ in range(5)]
    print(items)

    print("<<Adding items to our buffer>>")
    for item in items:
        data_structure.insert(item)

    print("<<Remove according to policy>>")
    removed_item = data_structure.extract()
    # print(removed_item)
    # print("----")
    # print(items[-1])
    assert removed_item == items[-1]


if __name__ == "__main__":
    main()
