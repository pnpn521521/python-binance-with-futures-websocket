from binance.client import Client
from binance.websockets import BinanceFuturesSocketManager
from binance.enums import *


def process_message(msg):
    # Do Something
    print(msg)


api_key = ""
api_secret = ""
client = Client(api_key, api_secret)

bfm = BinanceFuturesSocketManager(client)

# Aggregate Trade Streams
# bfm.start_futures_aggtrade_socket('BTCUSDT',process_message)

# Mark Price Stream
# bfm.start_futures_symbol_markprice_socket('BTCUSDT',process_message)
# bfm.start_futures_symbol_markprice_socket('BTCUSDT',process_message,update_time=1)

# Mark Price Stream for All market
# bfm.start_futures_markprice_socket(process_message)
# bfm.start_futures_markprice_socket(process_message,update_time=1)

# Kline/Candlestick Streams
# bfm.start_futures_kline_socket('BTCUSDT',process_message,interval=KLINE_INTERVAL_1MINUTE)

# Individual Symbol Mini Ticker Stream
# bfm.start_futures_symbol_miniticker_socket('BTCUSDT',process_message)

# All Market Mini Tickers Stream
# bfm.start_futures_miniticker_socket(process_message)

# Individual Symbol Ticker Streams
# bfm.start_futures_symbol_ticker_socket('BTCUSDT',process_message)

# All Market Tickers Streams
# bfm.start_futures_ticker_socket(process_message)

# Individual Symbol Book Ticker Streams
# bfm.start_futures_symbol_book_ticker_socket('BTCUSDT',process_message)

# All Book Tickers Stream
# bfm.startt_futures_book_ticker_socket(process_message)

# Liquidation Order Streams
# Not tested
# bfm.start_futures_symbol_force_order_socket('BTCUSDT',process_message)

# All Market Liquidation Order Streams
# Not tested
# bfm.start_futures_force_order_socket(process_message)

# Partial Book Depth Streams
# bfm.start_futures_depth_socket('BTCUSDT',process_message,depth=5)
# bfm.start_futures_depth_socket('BTCUSDT',process_message,depth=5,update_time=500)

# Diff. Book Depth Streams
# bfm.start_futures_depth_socket('BTCUSDT',process_message)
# bfm.start_futures_depth_socket('BTCUSDT',process_message,update_time=0)

# Multiplex Socket
# bfm.start_futures_multiplex_socket(['btcusdt@aggTrade', 'bnbusdt@ticker'],process_message)

# User Data Streams
# bfm.start_futures_socket(process_message)

bfm.start()
