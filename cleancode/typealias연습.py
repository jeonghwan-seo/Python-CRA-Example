def print_user_cart(user_id: int, items: list[tuple[str, float]]) -> None:
    print(f"User {user_id} 의 Shopping Cart:")
    total = 0.0
    for name, price in items:
        print(f" - {name}: {price:.2f}원")
        total += price
    print(f"Total: {total:.2f}원")


cart = [
    ("Keyboard", 49.10),
    ("Mouse", 25.50),
    ("Monitor", 199.10),
]

print_user_cart(1001, cart)
