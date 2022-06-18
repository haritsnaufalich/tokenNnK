<?php

date_default_timezone_set('Asia/Jakarta');

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

// NKT Section
echo PHP_EOL . ' [+] Token   : ' . 'NKT' . PHP_EOL;
echo ' [+] Price   : ' . getNKT('priceMajor') . '.' . substr(getNKT('priceMinor'), 0, 4) . ' (USD)' . PHP_EOL;
if (getNKT('percentMajor') >= 0) {
  echo " [+] Change  : \033[0;32m" . getNKT('percentMajor') . '.' . substr(getNKT('percentMinor'), 0, 2) . '%' . "\033[0m" . ' (+)' . PHP_EOL;
} else {
  echo " [+] Change  : \033[0;31m" . abs(getNKT('percentMajor') . '.' . substr(getNKT('percentMinor'), 0, 2)) . '%' . "\033[0m" . ' (-)' . PHP_EOL;
}
if (getExchangeNKT('increaseExchangeRate') > 0) {
  echo ' [+] Rate    : ' . getExchangeNKT('exchangeRate') . ' (' . "\033[0;32m" . getExchangeNKT('increaseExchangeRate') . "\033[0m" . ')' . PHP_EOL;
} else if (getExchangeNKT('increaseExchangeRate') == 0) {
  echo ' [+] Rate    : ' . getExchangeNKT('exchangeRate') . ' (' . "\033[0;36m" . abs(getExchangeNKT('increaseExchangeRate')) . "\033[0m" . ')' . PHP_EOL;
} else {
  echo ' [+] Rate    : ' . getExchangeNKT('exchangeRate') . ' (' . "\033[0;31m" . abs(getExchangeNKT('increaseExchangeRate')) . "\033[0m" . ')' . PHP_EOL;
}
echo ' [+] Last Updated on ' . date('F j Y, g:i', substr(getNKT('lastPriceUpdated'), 0, 10)) . PHP_EOL;
// echo '[+] Last Updated on ' . date('F j Y, g:i', getNKT('lastPriceUpdated')) . PHP_EOL;

// NKA Section
echo PHP_EOL . ' [+] Token   : ' . 'NKA' . PHP_EOL;
echo ' [+] Price   : ' . getNKA('priceMajor') . '.' . substr(getNKA('priceMinor'), 0, 4) . ' (USD)' . PHP_EOL;
if (getNKA('percentMajor') >= 0) {
  echo " [+] Change  : \033[0;32m" . getNKA('percentMajor') . '.' . substr(getNKA('percentMinor'), 0, 2) . '%' . "\033[0m" . ' (+)' . PHP_EOL;
} else {
  echo " [+] Change  : \033[0;31m" . abs(getNKA('percentMajor') . '.' . substr(getNKA('percentMinor'), 0, 2)) . '%' . "\033[0m" . ' (-)' . PHP_EOL;
}
if (getExchangeNKA('increaseExchangeRate') > 0) {
  echo ' [+] Rate    : ' . getExchangeNKA('exchangeRate') . ' (' . "\033[0;32m" . getExchangeNKA('increaseExchangeRate') . "\033[0m" . ')' . PHP_EOL;
} else if (getExchangeNKA('increaseExchangeRate') == 0) {
  echo ' [+] Rate    : ' . getExchangeNKA('exchangeRate') . ' (' . "\033[0;36m" . abs(getExchangeNKA('increaseExchangeRate')) . "\033[0m" . ')' . PHP_EOL;
} else {
  echo ' [+] Rate    : ' . getExchangeNKA('exchangeRate') . ' (' . "\033[0;31m" . abs(getExchangeNKA('increaseExchangeRate')) . "\033[0m" . ')' . PHP_EOL;
}
echo ' [+] Last Updated on ' . date('F j Y, g:i', substr(getNKA('lastPriceUpdated'), 0, 10)) . PHP_EOL;
// echo '[+] Last Updated on ' . date('F j Y, g:i', getNKA('lastPriceUpdated')) . PHP_EOL;

?>
