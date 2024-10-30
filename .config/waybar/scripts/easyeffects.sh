is_easy_active=$(pgrep 'easyeffects')
if [[ -n $is_easy_active ]]; then
  easy=$(</home/digo/.config/.easy_preset)
  if [[ $easy = "LoudnessEqualizer" ]]; then
    state="normal"
    output=""
  else
    state="warning"
    output=""
  fi
else
  state="critical"
  output="!"
fi

echo "{\"text\": \"$output\", \"tooltip\": \"Pomodoro Timer\", \"class\": \"$state\"}"
