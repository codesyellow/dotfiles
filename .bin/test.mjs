#!/usr/bin/env zx
const { stdout: current_day } = await $`date +%d`
const { stdout: current_month } = await $`date +%m`

const parsedJson = async (jsonPath) => {
  const data = await fs.readFile('/home/cie/.config/santosfc/santos.json', 'utf-8');
  return data
}

class Santos {
  matchup;
  hour;

  constructor(matchup, hour) {
    this.matchup = matchup,
    this.hour = hour
  }
}

const santos = new Santos('Ponte', '12');

console.log(santos);
parsedJson('/home/cie/.config/santosfc/santos.json').then(jsonData => {
  const matchs = JSON.parse(jsonData).matchs
  //console.log(matchs)
  Object.keys(matchs).forEach(key => {
    if (matchs[key].month.trim() === current_month.trim() && matchs[key].day.trim() === current_day.trim()) {
      console.log(matchs[key].hour, matchs[key].match)
    }
  });
});
