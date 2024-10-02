#!/usr/bin/env zx

const data = await fs.readFile(
  "/home/cie/.config/santosfc/santos.json",
  "utf-8"
);
const jsonSantosCalendar = JSON.parse(data);
const { stdout: current_day } = await $`date +%d`;
const { stdout: current_month } = await $`date +%m`;
let sleepTime;

const printMatchInfo = (match, hour) => {
  match.split("x").forEach((team) => {
    if (!team.trim().toLowerCase().includes("san")) {
      fs.writeFileSync("/tmp/santosmatch", `${hour}[${team.trim()}]`);
    }
  });
};

const santosMatch = async (hour, match) => {
  const hourArray = hour.split(":");
  const gameHour = hourArray[0];
  const gameMinutes = hourArray[1];
  let notifyDone = false;
  let didMatchDisplayed = false;

  while (true) {
    const { stdout: current_hour } = await $`date +%H`;
    const { stdout: current_minute } = await $`date +%M`;
    const timeLeft = gameHour - current_hour;

    if (timeLeft <= 0) {
      console.log("Leaving because condition was met");
      await $`rm /tmp/santosmatch`;
      break;
    }

    if (!didMatchDisplayed) {
      printMatchInfo(match, hour);
      didMatchDisplayed = true;
    }

    if (timeLeft <= 2 && gameMinutes <= current_minute && !notifyDone) {
      await $`notify-send -u critical -i $HOME/.local/share/icons/football.png "Pregame is about to start!!!"`;
      notifyDone = true;
    }

    if (timeLeft > 4) {
      sleepTime = 3600000;
    } else {
      sleepTime = 60000;
    }

    await sleep(sleepTime);
  }
};

const isMatchToday = () => {
  const matchs = jsonSantosCalendar.matchs;

  for (const gameKey in matchs) {
    if (matchs.hasOwnProperty(gameKey)) {
      const game = matchs[gameKey];
      if (
        Number(game.day) === Number(current_day) &&
        Number(game.month) === Number(current_month)
      ) {
        console.log(
          `Santos will play at: ${game.hour} and its match is: ${game.match}`
        );
        santosMatch(game.hour, game.match);
      }
    }
  }
};

isMatchToday();
