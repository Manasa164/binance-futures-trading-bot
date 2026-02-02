from bot.orders import place_order

def main():
    print("=== Trading Bot CLI ===")

    symbol = input("Symbol: ").strip().upper()
    side = input("Side (BUY / SELL): ").strip().upper()
    order_type = input("Order type (MARKET / LIMIT): ").strip().upper()
    quantity = float(input("Quantity: ").strip())

    price = None
    if order_type == "LIMIT":
        price = float(input("Price (for LIMIT only): ").strip())

    print("\nOrder Summary:")
    print(f"Symbol: {symbol}")
    print(f"Side: {side}")
    print(f"Type: {order_type}")
    print(f"Quantity: {quantity}")
    if price:
        print(f"Price: {price}")

    try:
        response = place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )
        print("\nOrder Response:")
        print(response)

    except Exception as e:
        print("\nError:")
        print(e)


if __name__ == "__main__":
    main()
