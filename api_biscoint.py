import json
import requests
from biscoint_api_python import Biscoint
from time import sleep

api_data = {
    'api_key': '4ac3580d4975d9465add3a469442c6ba54c5ace105efb97cc5f07fee5cd3904b',
    'api_secret': 'acc9a10439cbbac4969407c72cc7d5412b6b18fa72006a35d80748e0504b8661',}

bsc = Biscoint(api_data['api_key'], api_data['api_secret'])

try:
    #Consulta saldo em BTC e BRL
    balance = bsc.get_balance()
    #print(json.dumps(balance, indent=4))
    saldo_btc = balance['BTC']
    saldo_brl = balance['BRL']
    print(f'Saldo Bitcoin {saldo_btc}')
    print(f'Saldo BRL R$ {saldo_brl}')

except requests.exceptions.HTTPError as error:
    print(error)
    print(json.dumps(error.response.json(), indent=4))

else:
    if float(saldo_btc) == 0:
        print('Comprar bitcoin')
        while True:
            ticker = bsc.get_ticker() # verifica valor do bitcoin atual
            valor_btc = ticker['bid']
            print(f'Valor Bitcoin :{valor_btc}')
            if float(valor_btc) <= 189000.74:
                offer = bsc.get_offer('buy', f'{saldo_brl}', True) # Faz a oferta
                print(json.dumps(offer, indent=4))
                sleep(2)

                offerConfirmation = bsc.confirm_offer(offer['offerId']) #Confirma a oferta
                print(json.dumps(offerConfirmation, indent=4))
                sleep(2)
                break
            else:
                print('Ainda não chegou no objetivo, aguardar...')
                sleep(1800)
    else:
        print('Vender Bitcoin')
        while True:
            ticker = bsc.get_ticker() # verifica valor do bitcoin atual
            valor_btc = ticker['bid']
            print(f'Valor Bitcoin :{valor_btc}')
            if float(valor_btc) >= 270660.74:
                offer = bsc.get_offer('sell', f'{saldo_btc}', False) # Faz a oferta
                print(json.dumps(offer, indent=4))
                sleep(2)

                offerConfirmation = bsc.confirm_offer(offer['offerId']) #Confirma a oferta
                print(json.dumps(offerConfirmation, indent=4))
                sleep(2)
                break
            else:
                print('Ainda não chegou no objetivo, aguardar...')
                sleep(30)
