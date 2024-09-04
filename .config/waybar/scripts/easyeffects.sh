is_easy_active=$(pgrep 'easyeffects')
easy=$(</home/cie/.config/.easy_preset)
if [[ -n $is_easy_active ]]; then
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
