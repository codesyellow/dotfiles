#!/usr/bin/env zx
let active = false;
let inactive = false;
let off = false;

const setEqualizer = async () => {
  await $`pamixer --set-volume 30`;
  await $`easy_preset.sh 'LoudnessEqualizer'`;
};

while (true) {
  try {
    const { stdout: cmusStatus } =
      await $`cmus-remote -Q 2>/dev/null | grep status | awk '{print $2}' || echo "0"`;
    //    console.log(cmusStatus);
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
      console.log("Paused or stopped", inactive);
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
  await sleep(2000);
}
