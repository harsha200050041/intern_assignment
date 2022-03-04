from symtable import Symbol
from unicodedata import decimal
from binance import Client
import pandas as pd




api_key ='887c4d60ca13f660f8143df1ddcd5060cc5190b1dfea6938e1c06052f81c016c'
api_secret ='490fa626ec3036aaf89b38db24f16e20665047d86e194e05ab85cc09943c9ac5'

id=1
# quan=0.001
# stop=(99.5/100)*quan
# sell_amount = int(0.99 * (float(quan)))
# quantity = sell_amount
client = Client(api_key,api_secret,testnet=True)
# quan_n=round_down(client,quantity,'BTCUSDT')
# stop_n=round_down(client,stop,'BTCUSDT')
# print(quan_n)
# print(stop_n)
temp=client.futures_get_all_orders(symbol='BTCUSDT',limit=1)
cost=float(temp[0]['cumQuote'])
print(cost)
stop=0.995*cost
stop=round(stop,3)
print(temp)
print(stop)
def order_sell():
    global id
    new_id='ALGOINTERN_SL_OID'+str(id)
    old_id='ALGOINTERN_OID'+str(id)
    order_sell=client.futures_create_order(symbol='BTCUSDT',
                                side='SELL',
                                type='STOP_MARKET',
                                newClientOrderId=new_id,
                                stopPrice=stop,

                                
                      
                                quantity='0.001'
                                )

    
    print(order_sell)
    print("seperation")                            
    id=id+1
    print("ClientOrderID: " + str(order_sell['clientOrderId']))





for i in range(10):
    order_sell()