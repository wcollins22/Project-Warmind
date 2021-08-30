from dataclasses import dataclass


@dataclass
class Order:
    gb: float
    ff: float
    dr: float


def take_order(order: Order) -> None:
    order.gb = float(input("Good Burgers ($4.5): "))
    order.ff = float(input("French Fries ($1.5): "))
    order.dr = float(input("Drinks       ($1.0): "))


def reciept(order: Order) -> None:
    gb_price = 4.5
    ff_price = 1.5
    dr_price = 1.0
    print("Here is your receipt:")
    print(f"- Good Burgers $4.5 x {int(order.gb)} = ${order.gb * gb_price}")
    print(f"- French Fries $1.5 x {int(order.ff)} = ${order.ff * ff_price}")
    print(f"- Drinks       $1.0 x {int(order.dr)} = ${order.dr * dr_price}")
    total = order.dr * dr_price + order.ff * ff_price + order.gb * gb_price
    print(f"TOTAL = ${float(total)}")


def main() -> None:
    print(
        "Welcome to Good Burger.\nHome of the Good Burger.\nCan I take your order?"
    )
    order = Order(0, 0, 0)
    take_order(order)
    reciept(order)


if __name__ == "__main__":
    main()
