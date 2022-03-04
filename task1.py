from symtable import Symbol
from binance import Client
import pandas as pd

api_key ='887c4d60ca13f660f8143df1ddcd5060cc5190b1dfea6938e1c06052f81c016c'
api_secret ='490fa626ec3036aaf89b38db24f16e20665047d86e194e05ab85cc09943c9ac5'

a=1
client = Client(api_key, api_secret,testnet=True)
 #res=client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='BUY',quantity='0.001')
 #res=client.futures_order_book(symbol='BTCUSDT')
    # res = client.futures_symbol_ticker(symbol='BTCUSDT')
    # res2=client.create_test_order(symbol='BTCUSDT',type='MARKET',side='BUY',quantity=0.001)
    # client.futures_change_leverage(symbol='BTCUSDT',leverage='1')
    # client.futures_create_order(symbol='BTCUSDT',timeInForce='GTC',price='30000',side='BUY',quantity='0.001')
    # df=pd.DataFrame(client.futures_order_book(symbol='BTCUSDT'))
def order_buy():
    global a
    temp='ALGOINTERN_OID'+str(a)
    order_buy=client.futures_create_order(
                                    symbol='BTCUSDT',
                                    side='BUY',
                                    type='MARKET',
                                    newClientOrderId=temp,
                                   
                                
                                    quantity='0.001',
                                )
    
    

    a=a+1
   
    
for i in range(10):
    order_buy()
temp=client.futures_get_all_orders(symbol='BTCUSDT',limit=10)






#  type='LIMIT',
#     timeInForce='GTC',  # Can be changed - see link to API doc below
#     price=30000,  # The price at which you wish to buy/sell, float
#     side='BUY',  # Direction ('BUY' / 'SELL'), string
#     quantity=0.001      