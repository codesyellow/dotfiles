#!/usr/bin/env zx
let active = false;
let inactive = false;
while (true) {
  try {
    const { stdout: cmusStatus } =
      await $`cmus-remote -Q | grep status | awk '{print $2}'`;
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
      await $`pamixer --set-volume 30`;
      await $`easy_preset.sh 'LoudnessEqualizer'`;
      if (active) {
        active = false;
      }
    }
  } catch (e) {
    if (!inactive) {
      await $`pamixer --set-volume 30`;
      await $`easy_preset.sh 'LoudnessEqualizer'`;
      inactive = true;
    }
  }
  await sleep(2000);
}
