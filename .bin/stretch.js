#!/usr/bin/env node

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const { Command } = require('commander');

const program = new Command();
const stretchPath = '/tmp/stretch';
const stretchStartPath = '/tmp/stretch_start';

program
  .option('-t, --times <number>', 'How many times you want to stretch', parseInt)
  .option('-s, --seconds <number>', 'How many seconds you want for each stretch', parseInt)
  .option('-w, --wait <number>', 'How many seconds you want to stop between each stretch', parseInt)
  .parse(process.argv);

const options = program.opts();

if (Object.keys(options).length === 0) {
  program.help();
}

let times = options.times || 0;
const seconds = options.seconds || 0;
const wait = options.wait || 0;

if (fs.existsSync(stretchPath)) {
  console.log('It\'s already running!');
  execSync('notify-send "Already running!"');
  process.exit(1);
}

const realtime = times;

while (times >= 0) {
  if (times === realtime) {
    execSync('paplay ~/.audios/stretch_start.wav');
    fs.writeFileSync(stretchStartPath, '');
    console.log('Get ready!');
    execSync('sleep 3');
  }

  if (fs.existsSync(stretchStartPath)) {
    fs.unlinkSync(stretchStartPath);
  }

  if (!fs.existsSync(stretchPath)) {
    fs.writeFileSync(stretchPath, '');
  }

  if (times === 0) {
    execSync('paplay ~/.audios/stretch_ended.wav');
    fs.unlinkSync(stretchPath);
    execSync('notify-send -u critical "Stretch ended!"');
    break;
  } else {
    execSync('paplay ~/.audios/stretch_work.mp3');
    execSync(`sleep ${seconds}`);
    if (wait && times !== 1) {
      fs.writeFileSync('/tmp/stop', '');
      console.log('Stop!!');
      execSync('paplay ~/.audios/stretch_breaks.mp3');
      execSync(`sleep ${wait}`);
      fs.unlinkSync('/tmp/stop');
    }
  }

  times--;
}
