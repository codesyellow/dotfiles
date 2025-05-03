#!/usr/bin/env zx
let sleepTime = 4000;
let wasItMoved = false;
let notRunning = false;

const isGameRunning = async () => {
  try {
    const { stdout: gameRunning } = await $`
            pstree | grep reaper || 
            pstree | grep lutris-wrapper ||
            ps -ef | grep 'Games' | grep "-epicusername" | grep -v 'grep' ||
            echo "0"`;
    if (gameRunning.trim() !== "0") {
      //const { stdout: picomRunning } = await $`pidof picom || echo 0`;
      //if (picomRunning != 0) {
      //    await $`killall picom`;
      //}
      if (!fs.existsSync("/tmp/gameon")) {
        await $`touch /tmp/gameon`;
        await $`pkill -RTMIN+15 waybar`
      }
    } else {
      if (fs.existsSync("/tmp/gameon")) {
        await $`rm /tmp/gameon`;
        await $`pkill -RTMIN+15 waybar`
      }
      //const { stdout: picomRunning } = await $`pidof picom || echo 0`;
      //if (picomRunning == 0) {
      //    await $`nohup picom > /dev/null 2>&1 &`;
      //}
      wasItMoved = false;
    }
  } catch (error) {
    console.error("Error for isGameRunning function:", error);
  }
};

while (true) {
  try {
    await isGameRunning((value) => value);
  } catch (error) {
    console.error("Error executing command:", error);
  }
  await sleep(sleepTime);
}
