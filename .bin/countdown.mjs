#!/usr/bin/env zx
const args = process.argv.slice(2)[1];
let minutes;
let seconds;
if (!Number(args)) {
  await $`notify-send.sh "It's not a number!"`;
  process.exit(1);
}

console.log(args.split(".").length);
if (args.split(".").length >= 2) {
  minutes = Number(args.split(".")[0] * 60 * 1000);
  seconds = Number(args.split(".")[1] + "000");
} else {
  minutes = args.split(".")[0];
}
let counter = 0;
while (true) {
  if (!!seconds) {
    seconds = seconds - 1000;
    console.log(seconds);
    await sleep(1000);
    console.log("seconds fineshed");
  } else {
    counter++;
    if (!minutes) {
      break;
    }
    minutes = minutes - 1000;
    console.log(counter, minutes);
    await sleep(1000);
  }
}
