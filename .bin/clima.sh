#!/usr/bin/env bash
climate=$(curl -s "http://api.openweathermap.org/data/2.5/weather?lat=-23.963&lon=-46.3918&appid=2d6602a071d92529af1939b0152f5aba&units=metric" | jq '.main.temp | round')

if [[ -n $climate ]]; then
  echo $climate >"/tmp/climate"
else
  echo "climate not found"
fi
