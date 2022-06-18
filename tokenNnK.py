from datetime import date
from json import JSONDecoder
import requests
import datetime

def getNKT(Query):
  NKT = s.get('https://ninokuni.marblex.io/api/price?tokenType=NKT')
  NKT = JSONDecoder().decode(NKT.text)
  return NKT['currencies']['USD'][Query]

def getNKA(Query):
  NKA = s.get('https://ninokuni.marblex.io/api/price?tokenType=NKA')
  NKA = JSONDecoder().decode(NKA.text)
  return NKA['currencies']['USD'][Query]

def getExchangeNKT(Query):
  eNKT = s.get('https://ninokuni.marblex.io/api/exchangeRate?tokenType=NKT')
  eNKT = JSONDecoder().decode(eNKT.text)
  Last = len(eNKT['result']) - 1
  return eNKT['result'][Last][Query]

def getExchangeNKA(Query):
  eNKA = s.get('https://ninokuni.marblex.io/api/exchangeRate?tokenType=NKA')
  eNKA = JSONDecoder().decode(eNKA.text)
  Last = len(eNKA['result']) - 1
  return eNKA['result'][Last][Query]

def printNKT():
  print('\n [+] Token  : NKT')
  print(' [+] Price  : ' + str(getNKT('priceMajor')) + '.' + str(getNKT('priceMinor')[0:4]) + ' USD')
  if (int(getNKT('percentMajor')) >= 0):
    print(' [+] Change : ' + '\033[92m' + str(getNKT('percentMajor')) + '.' + str(getNKT('percentMinor')[0:2]) + '%' + '\033[0m' + ' (+)')
  else:
    print(' [+] Change : ' + '\033[91m' + str(abs(int(getNKT('percentMajor')))) + '.' + str(getNKT('percentMinor')[0:2]) + '%' + '\033[0m' + ' (-)')
  if (int(getExchangeNKT('increaseExchangeRate')) > 0):
    print(' [+] Rate   : ' + str(getExchangeNKT('exchangeRate')) + ' (' + '\033[92m' + str(getExchangeNKT('increaseExchangeRate')) + '\033[0m' + ')')
  elif (int(getExchangeNKT('increaseExchangeRate')) == 0):
    print(' [+] Rate   : ' + str(getExchangeNKT('exchangeRate')) + ' (' + '\033[96m' + str(getExchangeNKT('increaseExchangeRate')) + '\033[0m' + ')')
  else:
    print(' [+] Rate   : ' + str(getExchangeNKT('exchangeRate')) + ' (' + '\033[91m' + str(abs(int(getExchangeNKT('increaseExchangeRate')))) + '\033[0m' + ')')
  print(' [+] Last Updated on ' + date.fromtimestamp(int(getNKT('lastPriceUpdated')[0:10])).strftime('%B %d %Y'))

def printNKA():
  print('\n [+] Token  : NKA')
  print(' [+] Price  : ' + str(getNKA('priceMajor')) + '.' + str(getNKA('priceMinor')[0:4]) + ' USD')
  if (int(getNKA('percentMajor')) >= 0):
    print(' [+] Change : ' + '\033[92m' + str(getNKA('percentMajor')) + '.' + str(getNKA('percentMinor')[0:2]) + '%' + '\033[0m' + ' (+)')
  else:
    print(' [+] Change : ' + '\033[91m' + str(abs(int(getNKA('percentMajor')))) + '.' + str(getNKA('percentMinor')[0:2]) + '%' + '\033[0m' + ' (-)')
  if (int(getExchangeNKA('increaseExchangeRate')) > 0):
    print(' [+] Rate   : ' + str(getExchangeNKA('exchangeRate')) + ' (' + '\033[92m' + str(getExchangeNKA('increaseExchangeRate')) + '\033[0m' + ')')
  elif (int(getExchangeNKA('increaseExchangeRate')) == 0):
    print(' [+] Rate   : ' + str(getExchangeNKA('exchangeRate')) + ' (' + '\033[96m' + str(getExchangeNKA('increaseExchangeRate')) + '\033[0m' + ')')
  else:
    print(' [+] Rate   : ' + str(getExchangeNKA('exchangeRate')) + ' (' + '\033[91m' + str(abs(int(getExchangeNKA('increaseExchangeRate')))) + '\033[0m' + ')')
  print(' [+] Last Updated on ' + date.fromtimestamp(int(getNKA('lastPriceUpdated')[0:10])).strftime('%B %d %Y'))

if __name__ == '__main__':
  s = requests.Session()
  start = datetime.datetime.now()
  printNKT()
  printNKA()
  end = datetime.datetime.now() - start
  print('\n [+] Execution Time : ' + str(end.seconds) + '.' + str(end.microseconds)[0:2] + ' Seconds')