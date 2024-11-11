#!/usr/bin/env zx
let active = false;
let inactive = false;
let off = false;
const defaultVolume = 25;

const setEqualizer = async () => {
  await $`pamixer --set-volume ${defaultVolume}`;
  await $`easy_preset.sh 'LoudnessEqualizer'`;
};

const cmusRunning = async () => {
  try {
    const { stdout: cmusStatus } =
      await $`cmus-remote -Q 2>/dev/null | grep status | awk '{print $2}' || echo "0"`;
    if (cmusStatus.trim() === "playing" && !active) {
      active = true;
      off = false;
      if (inactive) {
        inactive = false;
      }
      console.log("Playing");
      await $`easy_preset.sh 'HeavyBass'`;
    } else if (
      (cmusStatus.trim() === "paused" && !inactive) ||
      (cmusStatus.trim() === "stopped" && !inactive)
    ) {
      off = false;
      inactive = true;
      console.log("Paused or stopped");
      setEqualizer();
      if (active) {
        active = false;
      }
    } else if (cmusStatus.trim() === "0") {
      if (!off) {
        setEqualizer();
        console.log("not running!");
        off = true;
      }
    }
  } catch (e) {
    if (!off) {
      setEqualizer();
      off = true;
    }
  }
};

while (true) {
  cmusRunning();
  await sleep(2000);
}
