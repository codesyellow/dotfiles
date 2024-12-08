#!/usr/bin/env zx
let already_disabled = false;
let already_enabled = false;
while (true) {
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

  const focusedWindowIndex =
    filterArray.findIndex((e) => {
      if (!parsedWindow.floating) {
        return e.address == parsedWindow.address;
      } else {
        return e.address == parsedWorkspace.lastwindow;
      }
    }) + 1;

  const numberOfClients = filterArray[0].grouped.length;
  console.log(numberOfClients);
  if (numberOfClients > 1 && !already_enabled) {
    await $`sed -i '/group:groupbar {/,/}/s/enabled = false/enabled = true/' ~/.config/hypr/configs/tabbed.conf`;
    already_disabled = false;
    already_enabled = true;
  } else if (numberOfClients === 1 && !already_disabled) {
    await $`sed -i '/group:groupbar {/,/}/s/enabled = true/enabled = false/' ~/.config/hypr/configs/tabbed.conf`;
    already_disabled = true;
    already_enabled = false;
  }

  await sleep(1000);
}
