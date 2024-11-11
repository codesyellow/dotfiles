#!/usr/bin/env zx

const { stdout: clients } = await $`hyprctl clients -j`;
const { stdout: workspace } = await $`hyprctl activeworkspace -j`;
const { stdout: window } = await $`hyprctl activewindow -j`;
const clientsParsed = JSON.parse(clients);
const parsedWorkspace = JSON.parse(workspace);
const parsedWindow = JSON.parse(window);

const filterArray = clientsParsed.filter((e) => {
  if (e.workspace.id == parsedWorkspace.id) {
    return e;
  }
});

// get activeworkspace lastwindow inside the else to check the right number to return
const focusedWindowIndex =
  filterArray.findIndex((e) => {
    console.log(parsedWindow.floating);
    if (!parsedWindow.floating) {
      return e.address == parsedWindow.address;
    } else {
      return e.address == parsedWorkspace.lastwindow;
    }
  }) + 1;

console.log(focusedWindowIndex);
const numberOfClients = filterArray[0].grouped.length;
//console.log(parsedWindow);

if (numberOfClients > 1) {
  const output = ` ${focusedWindowIndex}/${numberOfClients}<span size='15000' foreground='#4c566a'> | </span>`;
  console.log(
    `{\"text\": \"${output}\", \"tooltip\": \"tablayout\", \"class\": \"warning\"}`
  );
}
