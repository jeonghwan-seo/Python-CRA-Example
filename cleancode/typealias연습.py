def print_user_cart(user_id: int, items: list[tuple[str, int]]) -> None:
    print(f"User {user_id} 의 Shopping Cart:")
    total = 0.0
    for name, price in items:
        print(f" - {name}: {price}원")
        total += price
    print(f"Total: {total}원")


cart = [
    ("Keyboard", 49000),
    ("Mouse", 25000),
    ("Monitor", 199000),
]

print_user_cart(1001, cart)
