<?php

date_default_timezone_set('Asia/Jakarta');

# NKT Functions
function getNKT($Query) {
  $NKT = file_get_contents('https://ninokuni.marblex.io/api/price?tokenType=NKT');
  $NKT = json_decode($NKT, true);
  return $NKT['currencies']['USD'][$Query];
}
function getExchangeNKT($Query) {
  $eNKT = file_get_contents('https://ninokuni.marblex.io/api/exchangeRate?tokenType=NKT');
  $eNKT = json_decode($eNKT, true);
  $Last = count($eNKT['result']) - 1;
  return $eNKT['result'][$Last][$Query];
}

# NKA Functions
function getNKA($Query) {
  $NKA = file_get_contents('https://ninokuni.marblex.io/api/price?tokenType=NKA');
  $NKA = json_decode($NKA, true);
  return $NKA['currencies']['USD'][$Query];
}
function getExchangeNKA($Query) {
  $eNKA = file_get_contents('https://ninokuni.marblex.io/api/exchangeRate?tokenType=NKA');
  $eNKA = json_decode($eNKA, true);
  $Last = count($eNKA['result']) - 1;
  return $eNKA['result'][$Last][$Query];
}

# NKT Print
echo PHP_EOL . ' [+] Token Name    : ' . 'NKT' . PHP_EOL;
echo ' [+] Live Price    : ' . getNKT('priceMajor') . '.' . substr(getNKT('priceMinor'), 0, 4) . ' USD' . PHP_EOL;
echo ' [+] Last Price    : ' . getNKT('previousClosePriceMajor') . '.' . substr(getNKT('previousClosePriceMinor'), 0, 4) . ' USD' . ' (Previous Close Price)' . PHP_EOL;
if (getNKT('priceMajor') . '.' . substr(getNKT('priceMinor'), 0, 4) > getNKT('previousClosePriceMajor') . '.' . substr(getNKT('previousClosePriceMinor'), 0, 4)) {
  echo " [+] Changes       : \033[0;32m" . abs(getNKT('percentMajor') . '.' . substr(getNKT('percentMinor'), 0, 2)) . '%' . "\033[0m" . ' (+)' . PHP_EOL;
} else {
  echo " [+] Changes       : \033[0;31m" . abs(getNKT('percentMajor') . '.' . substr(getNKT('percentMinor'), 0, 2)) . '%' . "\033[0m" . ' (-)' . PHP_EOL;
}
if (getExchangeNKT('increaseExchangeRate') > 0) {
  echo ' [+] Exchange Rate : ' . getExchangeNKT('exchangeRate') . ' (' . "\033[0;32m" . abs(getExchangeNKT('increaseExchangeRate')) . "\033[0m" . ')' . PHP_EOL;
} else if (getExchangeNKT('increaseExchangeRate') == 0) {
  echo ' [+] Exchange Rate : ' . getExchangeNKT('exchangeRate') . ' (' . "\033[0;36m" . abs(getExchangeNKT('increaseExchangeRate')) . "\033[0m" . ')' . PHP_EOL;
} else {
  echo ' [+] Exchange Rate : ' . getExchangeNKT('exchangeRate') . ' (' . "\033[0;31m" . abs(getExchangeNKT('increaseExchangeRate')) . "\033[0m" . ')' . PHP_EOL;
}
echo ' [+] Last Updated on ' . date('F j Y, g:i', substr(getNKT('lastPriceUpdated'), 0, 10)) . PHP_EOL;

# NKA Print
echo PHP_EOL . ' [+] Token Name    : ' . 'NKA' . PHP_EOL;
echo ' [+] Live Price    : ' . getNKA('priceMajor') . '.' . substr(getNKA('priceMinor'), 0, 4) . ' USD' . PHP_EOL;
echo ' [+] Last Price    : ' . getNKA('previousClosePriceMajor') . '.' . substr(getNKA('previousClosePriceMinor'), 0, 4) . ' USD' . ' (Previous Close Price)' . PHP_EOL;
if (getNKA('priceMajor') . '.' . substr(getNKA('priceMinor'), 0, 4) > getNKA('previousClosePriceMajor') . '.' . substr(getNKA('previousClosePriceMinor'), 0, 4)) {
  echo " [+] Changes       : \033[0;32m" . abs(getNKA('percentMajor') . '.' . substr(getNKA('percentMinor'), 0, 2)) . '%' . "\033[0m" . ' (+)' . PHP_EOL;
} else {
  echo " [+] Changes       : \033[0;31m" . abs(getNKA('percentMajor') . '.' . substr(getNKA('percentMinor'), 0, 2)) . '%' . "\033[0m" . ' (-)' . PHP_EOL;
}
if (getExchangeNKA('increaseExchangeRate') > 0) {
  echo ' [+] Exchange Rate : ' . getExchangeNKA('exchangeRate') . ' (' . "\033[0;32m" . abs(getExchangeNKA('increaseExchangeRate')) . "\033[0m" . ')' . PHP_EOL;
} else if (getExchangeNKA('increaseExchangeRate') == 0) {
  echo ' [+] Exchange Rate : ' . getExchangeNKA('exchangeRate') . ' (' . "\033[0;36m" . abs(getExchangeNKA('increaseExchangeRate')) . "\033[0m" . ')' . PHP_EOL;
} else {
  echo ' [+] Exchange Rate : ' . getExchangeNKA('exchangeRate') . ' (' . "\033[0;31m" . abs(getExchangeNKA('increaseExchangeRate')) . "\033[0m" . ')' . PHP_EOL;
}
echo ' [+] Last Updated on ' . date('F j Y, g:i', substr(getNKT('lastPriceUpdated'), 0, 10)) . PHP_EOL;

?>
