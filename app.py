import argparse
from bot.logger import setup_logger
from bot.service import (
    validate_order_input,
    print_order_summary,
    print_order_response,
)
from bot.exceptions import ValidationError, APIClientError, NetworkError

# later you will use:
# from bot.client import BinanceFuturesClient


def parse_args():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair symbol, e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, dest="order_type", help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price for LIMIT orders only")

    return parser.parse_args()


def main():
    logger = setup_logger()
    args = parse_args()

    symbol = args.symbol.upper()
    side = args.side.upper()
    order_type = args.order_type.upper()
    quantity = args.quantity
    price = args.price

    try:
        validate_order_input(symbol, side, order_type, quantity, price)
        print_order_summary(symbol, side, order_type, quantity, price)

        logger.info(
            "Order request received | symbol=%s side=%s type=%s quantity=%s price=%s",
            symbol, side, order_type, quantity, price
        )

        # later replace this with real Binance call
        # client = BinanceFuturesClient(logger)
        # response = client.place_order(symbol, side, order_type, quantity, price)

        response = {
            "orderId": "TEMP12345",
            "status": "NEW",
            "executedQty": "0",
            "avgPrice": "0.0"
        }

        logger.info("Order response received | %s", response)
        print_order_response(response)
        print("\nSUCCESS: Order processed successfully.")

    except ValidationError as e:
        logger.error("Validation error: %s", e)
        print(f"\nFAILED: {e}")

    except APIClientError as e:
        logger.error("API error: %s", e)
        print(f"\nFAILED: Binance API error - {e}")

    except NetworkError as e:
        logger.error("Network error: %s", e)
        print(f"\nFAILED: Network error - {e}")

    except Exception as e:
        logger.exception("Unexpected error")
        print(f"\nFAILED: Unexpected error - {e}")


if __name__ == "__main__":
    main()
