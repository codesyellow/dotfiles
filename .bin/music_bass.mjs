#!/usr/bin/env zx
let active = false;
let inactive = false;

const setEqualizer = async () => {
  await $`pamixer --set-volume 30`;
  await $`easy_preset.sh 'LoudnessEqualizer'`;
};

while (true) {
  try {
    const { stdout: cmusStatus } =
      await $`cmus-remote -Q 2>/dev/null | grep status | awk '{print $2}' || echo "0"`;
    if (cmusStatus.trim() === "playing" && !active) {
      active = true;
      if (inactive) {
        inactive = false;
      }
      console.log("Playing");
      await $`easy_preset.sh 'HeavyBass'`;
    } else if (
      cmusStatus.trim() === "paused" ||
      (cmusStatus.trim() === "stopped" && !inactive)
    ) {
      inactive = true;
      console.log("Paused or stopped");
      setEqualizer();
      if (active) {
        active = false;
      }
    } else if (cmusStatus.trim() === "0") {
      if (!inactive) {
        setEqualizer();
        inactive = true;
      }
    }
  } catch (e) {
    if (!inactive) {
      setEqualizer();
      inactive = true;
    }
  }
  await sleep(2000);
}
