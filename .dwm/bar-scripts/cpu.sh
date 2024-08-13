cputemp=$(cat /sys/class/thermal/thermal_zone2/temp | cut -c 1-2)
cpu=$(awk '{u=$2+$4; t=$2+$4+$5; if (NR==1){u1=u; t1=t;} else print ($2+$4-u1) * 100 / (t-t1) "%"; }' \
  <(grep 'cpu ' /proc/stat) <(
    sleep 1
    grep 'cpu ' /proc/stat
  ))
cpu=$(echo "$cpu" | tr -d '%') # Remove the '%' sign if present
cpu_per_int=$(printf "%.0f\n" "$cpu")

if [[ $1 == 'cpu' ]]; then
  printf "$cpu_per_int"
else
  printf "$cputemp"
fi
