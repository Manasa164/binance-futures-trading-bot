from bot.client import get_client
import logging

logger = logging.getLogger("trading_bot")
client = get_client()

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        order_params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }
        if order_type == "LIMIT":
            order_params["price"] = price
            order_params["timeInForce"] = "GTC"

        logger.info(f"Placing order: {order_params}")
        response = client.futures_create_order(**order_params)
        logger.info(f"Order response: {response}")
        return response
    except Exception as e:
        logger.error(f"Error placing order: {e}")
        return {"error": str(e)}
