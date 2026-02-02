def validate_symbol(symbol):
    if not symbol.isalnum():
        raise ValueError("Symbol must be alphanumeric")
    return symbol.upper()

def validate_side(side):
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side.upper()

def validate_order_type(order_type):
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type.upper()

def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    return quantity

def validate_price(price, order_type):
    if order_type == "LIMIT" and (price is None or price <= 0):
        raise ValueError("Price must be positive for LIMIT orders")
    return price
