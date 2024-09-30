#!/usr/bin/env zx
let sleepTime = 4000; 
let wasItMoved = false;
let notRunning = false;

const moveIt = async (theGame) => {
  try {
    const { stdout: window_class } = await $`xprop -id $(xdotool getwindowfocus) | grep "WM_CLASS(STRING)" | awk -F '"' '{print $4}' || xprop -id $(xdotool getwindowfocus) | grep "WM_NAME" | awk -F'"' '{print $2}'`;
    
    const window_classes = window_class.trim().split(' ');

    const normalized_window_class = window_class
    .trim()
    .toLowerCase()
    .replace(/[0-9]/g, '')
    .replace(/[^a-zA-Z\s]/g, '')
    .replace(/bin.*/, '');

    const cleanTheGame = theGame.toLowerCase().replace(/[0-9]/g, '').replace(/[^a-zA-Z\s]/g, '');
    const regex = new RegExp(normalized_window_class);  

    for (const element of window_classes) {
      if (cleanTheGame.includes(normalized_window_class) && !wasItMoved) {
        wasItMoved = true;
        console.log('Window class matched, moving it.');
        await $`xdotool windowfocus $(xdotool getwindowfocus)`;
        await $`xdotool key --clearmodifiers Super+Shift+w g`;
        break; 
      }
    }

    if (cleanTheGame.includes(normalized_window_class) && !wasItMoved) {
      wasItMoved = true;
      console.log('Window class matched in fallback, moving it.');
      await $`xdotool windowfocus $(xdotool getwindowfocus)`;
      await $`xdotool key --clearmodifiers Super+Shift+w g`;
    }

  } catch (error) {
    console.error('Error in moveIt function:', error);
  }
};

const isGameRunning = async () => {
  try {
    const { stdout: gameRunning } = await $`pstree | grep reaper || pstree | grep lutris-wrapper || echo "0"`;

    if (gameRunning.trim() !== '0') {
      const { stdout: current_workspace } = await $`xprop -root _NET_CURRENT_DESKTOP | awk '/_NET_CURRENT_DESKTOP/ {print $3}'`;
        if(current_workspace.trim() != '3' && !wasItMoved) {
          await moveIt(gameRunning);
      }
      else {
        if (wasItMoved) {
          wasItMoved = false;
          console.log('No game running')
        }
      }
    }
    else {
      return false;
    }
  } catch (error) {
    console.error('Error for isGameRunning function:', error);
  }
}

while (true) {
  try {
    const state = await isGameRunning(value => value);
    if (!state && !notRunning) {
      wasItMoved = false;
      notRunning = true;
      console.log('No game running')
    }

  } catch (error) {
    console.error('Error executing command:', error);
  }
  await sleep(sleepTime);
}
