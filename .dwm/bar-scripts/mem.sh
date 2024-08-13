while true; do
  freemen_per=$(free -m | awk 'NR==2{print $3*100/$2 }')
  freemen_per_int=$(printf "%.0f\n" "$freemen_per")
  echo "$freemen_per_int" >/tmp/ram

  sleep 2
done
