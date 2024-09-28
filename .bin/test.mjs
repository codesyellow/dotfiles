#!/usr/bin/env zx
let sleepTime;
while (true) {
  try {
    const { stdout: reaperRunning } = await $`pstree -p | grep reaper || echo "0"`;
    
    if (reaperRunning.trim() !== '0' ) {
      const numbers = reaperRunning.match(/\((\d+)\)/g).map(num => num.replace(/[()]/g, ''));

      // Loop through the array and print the numbers
      numbers.forEach(number => {
        console.log(number);
      });
      const { stdout: current_workspace } = await $`xprop -root _NET_CURRENT_DESKTOP | awk '/_NET_CURRENT_DESKTOP/ {print $3}'`;
      if(current_workspace.trim() != '3') {
        const { stdout: window_class } = await $`xprop -id $(xdotool getwindowfocus) | grep "WM_CLASS(STRING)" | awk -F '"' '{print $4}' || xprop -id $(xdotool getwindowfocus) | grep "_NET_WM_NAME" | awk -F'"' '{print $2}'
`;
        console.log(window_class, current_workspace);
        sleepTime = 3000;
      }
    }
    else {
      console.log('no game running or is running in the proper workspace')
      sleepTime = 10000;
    }
  } catch (error) {
    console.error('Error executing command:', error);
  }
  await sleep(sleepTime);
}
