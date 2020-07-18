from threading import Thread
import requests, time

threads = [None] * 1000

def gogo(idx, ll):
    url = 'https://api.hanbitco.com/history?symbol=ETH_BTC&resolution=1&from=1574938994&to=1594964733'
    # url = 'https://www.hanbitco.com/exchange/eth_btc'
    data = requests.get(url)
    print('finished thread {}'.format(idx), data)

for i in range(len(threads)):
    print('thread {} started'.format(i))
    threads[i] = Thread(target=gogo, args=(i, 1))
    threads[i].start()


time.sleep(100)

