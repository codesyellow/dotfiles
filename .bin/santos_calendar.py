#!/usr/bin/env python
from requests_html import HTMLSession
import os
import json
from typing import Dict
from datetime import datetime

HOME = os.path.expanduser("~")
SCHEDULE_PATH = f"{HOME}/.config/sSchedule.json"


class Santos():
    def __init__(self) -> None:
        self.schedule: list = self.get_schedule()
        self.game_info: str = ""

    def scrap_schedule(self) -> list:
        """Scrap the data return it"""
        session = HTMLSession()
        r = session.get(
            'https://www.espn.com.br/futebol/time/calendario/_/id/2674/bra.santos')
        site = r.html.find(".Table__TR.Table__TR--sm.Table__even")
        schedule = []
        for game in site:
            day = int(game.find(".matchTeams")[
                      0].text.split(".")[1].split(" ")[1])
            month = game.find(".matchTeams")[0].text.split(".")[
                1].split(" ")[2]
            hour = int(game.find(".Table__TD .AnchorLink")
                       [5].text.split(":")[0]) + 2
            minutes = game.find(".Table__TD .AnchorLink")[5].text.split(":")[1]
            home_team = game.find(".AnchorLink.Table__Team")[0].text
            away_team = game.find(".AnchorLink.Table__Team")[1].text
            schedule.append({
                "day": day,
                "month": month,
                "hour": f"{hour}:{minutes}",
                "home_team": home_team,
                "away_team": away_team,
            })
        return schedule

    def get_schedule(self) -> list:
        """Try to get the schedule to return it"""
        try:
            with open(SCHEDULE_PATH) as data:
                return json.load(data)
        except FileNotFoundError:
            schedule = self.scrap_schedule()
            with open(SCHEDULE_PATH, "w", encoding="utf-8") as data:
                json.dump(schedule, data, ensure_ascii=False, indent=4)
            return schedule

    def save_schedule(self, schedule: list) -> None:
        """Save schedule to file"""
        with open(SCHEDULE_PATH, "w") as data:
            json.dump(schedule, data, ensure_ascii=False, indent=4)

    def make_copy(self, schedule: list) -> None:
        """Make a copy of the schedule"""
        with open(f"{SCHEDULE_PATH}.bak", "w") as data:
            json.dump(schedule, data, ensure_ascii=False, indent=4)

    def update_schedule(self) -> None:
        """Update the schedule"""
        new_schedule = self.scrap_schedule()
        self.make_copy(self.schedule)
        self.save_schedule(new_schedule)

    def get_next_game(self) -> Dict[str, int]:
        """Get the next game and return it"""
        next_game = self.schedule[0]
        return next_game

    def is_game_today(self) -> bool:
        """Check if the game is today or not and return a boolean"""
        current_day = datetime.now().day
        game_day = self.get_next_game()["day"]

        if current_day == game_day:
            return True
        else:
            return False

    def write(self):
        """Write to the file the next game information"""
        with open("/tmp/santos", "w") as data:
            next_game = self.get_next_game()
            game_day = next_game["day"]
            game_hour = next_game["hour"]
            home_team = next_game["home_team"]
            away_team = next_game["away_team"]
            if self.is_game_today():
                if home_team == "Santos":
                    self.game_info = f"{game_day}:{game_hour}/{away_team}(H)"
                elif away_team == "Santos":
                    self.game_info = f"{game_day}:{game_hour}/{home_team}(A)"
            else:
                if home_team == "Santos":
                    self.game_info = f"{game_day}:{game_hour}(H)"
                elif away_team == "Santos":
                    self.game_info = f"{game_day}:{game_hour}(A)"

            data.write(self.game_info)

    def run(self) -> None:
        self.write()


if __name__ == "__main__":
    santos = Santos()
    santos.run()
