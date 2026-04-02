#!/usr/bin/env python
import subprocess
import re
import sys
import json
from time import sleep

SLEEP_TIME=5

class Caffeine:
    """Prevents the systemd from going to sleep while focused window is fullscrened or an audio is being played."""

    def __init__(self): 
        self.args=sys.argv[1:]
        self.alt_filter_list=[]

    def is_fullscreen(self): 
        return self.monitor_size() == self.window_size()

    def check_playerctl(self, apps):
        for app in apps:
            try:
                status = subprocess.run(['playerctl', '-p', app, 'status'], 
                                        capture_output=True, text=True).stdout.strip()
                if status == "Playing":
                    if not self.is_caffeine_on():
                        print("Using playerctl")
                    return True
            except:
                continue
        return False
    def get_audio_data(self):
        try:
            lines = subprocess.run(['pactl', 'list', 'sink-inputs'], capture_output=True, text=True).stdout.split('\n')
        except Exception:
            pass
        else:
            filtered = [l for l in lines if re.search(r'application\.name|Corked', l)]
            return '\n'.join(filtered)

    def parse_audio_data(self, text):
            result = []
            current_block = None
            
            for line in text.strip().split('\n'):
                line = line.strip()
                
                corked_match = re.match(r'Corked:\s*(yes|no)', line)
                if corked_match:
                    if current_block is not None:
                        result.append(current_block)
                    current_block = {
                        'Corked': corked_match.group(1),
                        'properties': {}
                    }
                elif current_block is not None and '=' in line:
                    key, _, value = line.partition('=')
                    key = key.strip()
                    value = value.strip().strip('"')
                    current_block['properties'][key] = value
            
            if current_block is not None:
                result.append(current_block)
            
            return result

    def filter_audio_data(self, items, terms):
        filtered = []
        alt_filter = []
        for item in items:
            app_name = item['properties']['application.name'].lower()
            
            if all(term.lower() not in app_name for term in terms):
                filtered.append(item)
            else:
                alt_filter.append(item)

   #     print(alt_filter)
        self.alt_filter_list = alt_filter
        return filtered

    def is_audio_playing(self):
        data = self.get_audio_data()
        blocks = self.parse_audio_data(data)
        playing=[audio for audio in self.filter_audio_data(blocks, self.args) if audio["Corked"] == "no"]
        if len(playing) >= 1:
            if not self.is_caffeine_on():
                print("Using alternative method")
            return True
        else:
            return self.check_playerctl(self.args) 
                
                
    def set_caffeine_status(self, status):
        try:
            subprocess.run(['systemctl', '--user', f'{status}', 'caffeine.service'], check=True)
            print(f"{status} the service")
        except subprocess.CalledProcessError as e:
            print(f"Unable to {status} the service: {e.stderr}")

    def is_caffeine_on(self):
        """Checks the ActiveState of a systemd service."""
        try:
            status=subprocess.run(["systemctl", "--user", "show", "caffeine", "-p", "ActiveState", "--value"], capture_output=True, text=True, check=True).stdout.strip()
        except Exception: 
            pass
        else:
            return status == "active"
        
    def window_size(self):
        try:
            win_size=self.nirimsg("focused-window")["layout"]["window_size"]
        except TypeError:
            pass
        else:
            return f"{win_size[0]}x{win_size[1]}"

    def is_window_floating(self):
        try:
            floating=self.nirimsg("focused-window")["is_floating"]
        except Exception:
            pass
        else:
            return floating

    def monitor_size(self):
        try:
            info=self.nirimsg("focused-output")
        except Exception:
            pass
        except TypeError:
            pass
        else:
            width=info["logical"]["width"]
            height=info["logical"]["height"]
            return f"{width}x{height}"

    def nirimsg(self, command):
        try:
            return json.loads(subprocess.run(["niri", "msg", "--json", f"{command}"], capture_output=True, text=True, check=True).stdout)
        except Exception:
            print("Is niri running?")

    def run(self):
        while True:
            if not self.is_audio_playing():
                if self.is_fullscreen() and not self.is_caffeine_on():
                    self.set_caffeine_status("start")
                elif not self.is_fullscreen() and self.is_caffeine_on() and not self.is_window_floating():
                    self.set_caffeine_status("stop")
            else:
                if not self.is_caffeine_on() and not self.is_window_floating():
                    self.set_caffeine_status("start")
            sleep(SLEEP_TIME)

caf = Caffeine()

caf.run()
