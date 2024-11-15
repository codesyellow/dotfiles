#!/usr/bin/env zx

const { stdout: tmuxList } = await $`tmux ls`;
const icon = "";
const kill = process.argv.slice(3)[0];

const listSize = tmuxList
  .split(os.EOL)
  .filter((e) => !e.includes("attached") && e.length != 0);

if (listSize.length > 1) {
  console.log(
    `<span rise="-22000" foreground="#EF5A6F">${icon}</span>  <span rise="-20000" foreground="#EF5A6F">${listSize.length}</span><span rise="-18000"size="x-large" foreground="#4c566a"> |</span>`
  );
}

if (kill == "kill") {
  listSize.forEach(async (element) => {
    if (!element.includes("attached")) {
      await $`tmux kill-session -t ${element.split(":")[0]}`;
    }
  });
}
