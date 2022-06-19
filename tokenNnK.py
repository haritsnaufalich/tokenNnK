from json import JSONDecoder
import requests

# NKT Function
def getNKT(Query):
  NKT = s.get('https://ninokuni.marblex.io/api/price?tokenType=NKT')
  NKT = JSONDecoder().decode(NKT.text)
  return NKT['currencies']['USD'][Query]
def getExchangeNKT(Query):
  eNKT = s.get('https://ninokuni.marblex.io/api/exchangeRate?tokenType=NKT')
  eNKT = JSONDecoder().decode(eNKT.text)
  Last = len(eNKT['result']) - 1
  return eNKT['result'][Last][Query]

# NKA Function
def getNKA(Query):
  NKA = s.get('https://ninokuni.marblex.io/api/price?tokenType=NKA')
  NKA = JSONDecoder().decode(NKA.text)
  return NKA['currencies']['USD'][Query]
def getExchangeNKA(Query):
  eNKA = s.get('https://ninokuni.marblex.io/api/exchangeRate?tokenType=NKA')
  eNKA = JSONDecoder().decode(eNKA.text)
  Last = len(eNKA['result']) - 1
  return eNKA['result'][Last][Query]

# NKT Print Function
def printNKT():
  print('\n [+] Token Name    : NKT')
  print(' [+] Live Price    : ' + liveNKTPrice + ' USD')
  print(' [+] Last Price    : ' + lastNKTPrice + ' USD' + ' (Previous Close Price)')
  if (liveNKTPrice > lastNKTPrice):
    print(' [+] Changes       : ' + '\033[92m' + str(abs(int(getNKT('percentMajor')))) + '.' + str(getNKT('percentMinor')[0:2]) + '%' + '\033[0m' + ' (+)')
  else:
    print(' [+] Changes       : ' + '\033[91m' + str(abs(int(getNKT('percentMajor')))) + '.' + str(getNKT('percentMinor')[0:2]) + '%' + '\033[0m' + ' (-)')
  if (int(getExchangeNKT('increaseExchangeRate')) > 0):
    print(' [+] Exchange Rate : ' + str(getExchangeNKT('exchangeRate')) + ' (' + '\033[92m' + str(getExchangeNKT('increaseExchangeRate')) + '\033[0m' + ')')
  elif (int(getExchangeNKT('increaseExchangeRate')) == 0):
    print(' [+] Exchange Rate : ' + str(getExchangeNKT('exchangeRate')) + ' (' + '\033[96m' + str(getExchangeNKT('increaseExchangeRate')) + '\033[0m' + ')')
  else:
    print(' [+] Exchange Rate : ' + str(getExchangeNKT('exchangeRate')) + ' (' + '\033[91m' + str(abs(int(getExchangeNKT('increaseExchangeRate')))) + '\033[0m' + ')')

# NKA Print Function
def printNKA():
  print('\n [+] Token Name    : NKA')
  print(' [+] Live Price    : ' + liveNKAPrice + ' USD')
  print(' [+] Last Price    : ' + lastNKAPrice + ' USD' + ' (Previous Close Price)')
  if (liveNKAPrice > lastNKAPrice):
    print(' [+] Changes       : ' + '\033[92m' + str(abs(int(getNKA('percentMajor')))) + '.' + str(getNKA('percentMinor')[0:2]) + '%' + '\033[0m' + ' (+)')
  else:
    print(' [+] Changes       : ' + '\033[91m' + str(abs(int(getNKA('percentMajor')))) + '.' + str(getNKA('percentMinor')[0:2]) + '%' + '\033[0m' + ' (-)')
  if (int(getExchangeNKA('increaseExchangeRate')) > 0):
    print(' [+] Exchange Rate : ' + str(getExchangeNKA('exchangeRate')) + ' (' + '\033[92m' + str(getExchangeNKA('increaseExchangeRate')) + '\033[0m' + ')')
  elif (int(getExchangeNKA('increaseExchangeRate')) == 0):
    print(' [+] Exchange Rate : ' + str(getExchangeNKA('exchangeRate')) + ' (' + '\033[96m' + str(getExchangeNKA('increaseExchangeRate')) + '\033[0m' + ')')
  else:
    print(' [+] Exchange Rate : ' + str(getExchangeNKA('exchangeRate')) + ' (' + '\033[91m' + str(abs(int(getExchangeNKA('increaseExchangeRate')))) + '\033[0m' + ')')

if __name__ == '__main__':
  # Initialize Requests Session
  s = requests.Session()
  
  # NKT
  # posNKTExchangeRate = str(getExchangeNKT('exchangeRate')) + ' (' + '\033[92m' + str(getExchangeNKT('increaseExchangeRate')) + '\033[0m' + ')'
  # netNKTExchangeRate = str(getExchangeNKT('exchangeRate')) + ' (' + '\033[96m' + str(getExchangeNKT('increaseExchangeRate')) + '\033[0m' + ')'
  # negNKTExchangeRate = str(getExchangeNKT('exchangeRate')) + ' (' + '\033[91m' + str(abs(int(getExchangeNKT('increaseExchangeRate')))) + '\033[0m' + ')'
  liveNKTPrice = str(getNKT('priceMajor')) + '.' + str(getNKT('priceMinor')[0:4])
  lastNKTPrice = str(getNKT('previousClosePriceMajor')) + '.' + str(getNKT('previousClosePriceMinor')[0:4])
  # posNKTChanges = '\033[92m' + str(abs(int(getNKT('percentMajor')))) + '.' + str(getNKT('percentMinor')[0:2]) + '%' + '\033[0m' + ' (+)'
  # negNKTChanges = '\033[91m' + str(abs(int(getNKT('percentMajor')))) + '.' + str(getNKT('percentMinor')[0:2]) + '%' + '\033[0m' + ' (-)'

  # NKA
  # posNKAExchangeRate = str(getExchangeNKA('exchangeRate')) + ' (' + '\033[92m' + str(getExchangeNKA('increaseExchangeRate')) + '\033[0m' + ')'
  # netNKAExchangeRate = str(getExchangeNKA('exchangeRate')) + ' (' + '\033[96m' + str(getExchangeNKA('increaseExchangeRate')) + '\033[0m' + ')'
  # negNKAExchangeRate = str(getExchangeNKA('exchangeRate')) + ' (' + '\033[91m' + str(abs(int(getExchangeNKA('increaseExchangeRate')))) + '\033[0m' + ')'
  liveNKAPrice = str(getNKA('priceMajor')) + '.' + str(getNKA('priceMinor')[0:4])
  lastNKAPrice = str(getNKA('previousClosePriceMajor')) + '.' + str(getNKA('previousClosePriceMinor')[0:4])
  # posNKAChanges = '\033[92m' + str(abs(int(getNKA('percentMajor')))) + '.' + str(getNKA('percentMinor')[0:2]) + '%' + '\033[0m' + ' (+)'
  # negNKAChanges = '\033[91m' + str(abs(int(getNKA('percentMajor')))) + '.' + str(getNKA('percentMinor')[0:2]) + '%' + '\033[0m' + ' (-)'

  # Print
  printNKT()
  printNKA()