#!/usr/bin/env node

const os = require('os');

function getCPULoad() {
  const load = os.loadavg();
  // load[0] - Average load over the last 1 minute
  // load[1] - Average load over the last 5 minutes
  // load[2] - Average load over the last 15 minutes
  console.log('CPU Load:', load);
}

setInterval(getCPULoad, 1000); // Check every 1 second
