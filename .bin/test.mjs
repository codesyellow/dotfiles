#!/usr/bin/env zx

const original_pregame_hour = await $`cat /tmp/santos_pregame_hour | cut -d: -f1`
const pregame_hour = original_pregame_hour - 2;
const pregame_minute = await $`cat /tmp/santos_pregame_hour | cut -d: -f2`
try {
  await $`test -f /tmp/santos_pregame_hour`;
  while (true) {
    const { stdout: current_hour } = await $`date +%H`
    const { stdout: current_minute } = await $`date +%M`
    if (current_hour >= pregame_hour && current_minute >= pregame_minute) {
      await $`notify-send -u critical -i $HOME/.local/share/icons/football.png "Pregame is about to start!!!"`
      break;
    }; 
    await sleep(10000);
  }
}
catch (e) {
  console.log('Today santos will not play');
}
