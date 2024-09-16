#!/bin/bash

climate_num=$(curl -s "http://api.openweathermap.org/data/2.5/weather?lat=-23.963&lon=-46.3918&appid=2d6602a071d92529af1939b0152f5aba&units=metric" | jq '.main.temp | round')

if [[ "$climate_num" -ge 30 ]]; then
  output=" |  $climate_num"
elif [[ "$climate_num" -le 20 ]]; then
  output=" |  $climate_num"
else
  output=" |  $climate_num"
fi

echo "{\"text\": \"$output\", \"tooltip\": \"Climate\" }"
