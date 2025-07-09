#!/usr/bin/env python3
import subprocess
import json
import argparse
import time

# Tamanhos em percentual (largura, altura)
PADDING = (20, 20)
SMALL = (40, 40)
SMALLA = (40, 80)
SMALLF = (90, 40)
MEDIUM = (50, 50)
MEDIUMA = (50, 50)
BIG = (90, 90)

parser = argparse.ArgumentParser(description="Sway scratchpad controller")
parser.add_argument("-p", "--position")
parser.add_argument("-s", "--sizes")
parser.add_argument("-c", "--command")
parser.add_argument("-n", "--name", default="")
parser.add_argument("-cn", "--class", default="")

class Swaypad():
    def __init__(self) -> None:
        self.scratch_size = 600
        self.size = self.set_size()
        self.focused_monitor = self.get_focused_monitor()
        self.position = self.set_position()

    def set_position(self):
        """Calcula a posição com base no monitor atual"""
        monitor_width = self.focused_monitor["rect"]["width"]
        monitor_height = self.focused_monitor["rect"]["height"]
        args = parser.parse_args()
        config = vars(args)
        width = int(monitor_width * (self.size[0] / 100))
        height = int(monitor_height * (self.size[1] / 100))  # Corrigido aqui

        match config["position"]:
            case "top":
                return (monitor_width // 2 - width // 2, PADDING[1])
            case "bottom":
                return (monitor_width // 2 - width // 2, monitor_height - height - 50)
            case "top-left":
                return PADDING
            case "top-right":
                return (monitor_width - width - PADDING[0], PADDING[1])
            case "bottom-left":
                return (PADDING[0], monitor_height - height - 50)
            case "bottom-right":
                return (monitor_width - width - PADDING[0], monitor_height - height - 50)
            case _:
                return (monitor_width // 2 - width // 2, monitor_height // 2 - height // 2)

    def set_size(self):
        args = parser.parse_args()
        config = vars(args)
        match config["sizes"]:
            case "sm":
                return SMALL
            case "sma":
                return SMALLA
            case "smf":
                return SMALLF
            case "med":
                return MEDIUM
            case "meda":
                return MEDIUMA
            case "big":
                return BIG
            case _:
                return MEDIUM

    def get_focused_monitor(self):
        monitors = json.loads(subprocess.check_output([
            "swaymsg", "-t", "get_outputs", "-r"
        ]).decode("utf-8"))
        for monitor in monitors:
            if monitor["focused"]:
                return monitor

    def wait_for_window(self, app_name, timeout=3):
        """Espera até a janela com nome/classe aparecer no get_tree"""
        for _ in range(timeout * 10):
            tree = subprocess.check_output(["swaymsg", "-t", "get_tree"])
            if app_name in tree.decode():
                return True
            time.sleep(0.1)
        return False

    def open_app(self):
        args = parser.parse_args()
        config = vars(args)
        command = config["command"]
        subprocess.Popen(command.split(), start_new_session=True)

    def open_scratch(self):
        args = parser.parse_args()
        config = vars(args)
        name = config["name"]
        class_name = config["class"]

        if class_name:
            app_match = f"[class='{class_name}']"
        else:
            app_match = f"[app_id='{name}']"

        width = self.focused_monitor["rect"]["width"]
        height = self.focused_monitor["rect"]["height"]
        scratch_width = int(width * (self.size[0] / 100))
        scratch_height = int(height * (self.size[1] / 100))

        resize = f"resize set {scratch_width} {scratch_height}"
        position = f"move position {self.position[0]} {self.position[1]}"

        # Primeira tentativa de redimensionar (caso a janela já exista)
        subprocess.run(f'swaymsg {app_match} {resize}', shell=True)
        # Tentar mostrar
        app = subprocess.run(f'swaymsg {app_match} scratchpad show', shell=True)

        # Esperar aparecer
        if not self.wait_for_window(name or class_name):
            print("Janela não encontrada após mostrar a scratchpad.")
            self.open_app()
            return

        time.sleep(0.2)
        # Garantir que o tamanho/posição foi aplicado corretamente
        subprocess.run(f'swaymsg {app_match} floating enable', shell=True)
        subprocess.run(f'swaymsg {app_match} {resize}', shell=True)
        subprocess.run(f'swaymsg {app_match} {position}', shell=True)
        time.sleep(0.1)

        # Focar na janela
        try:
            window_id = subprocess.check_output(
                "swaymsg -t get_tree | jq -r '.. | select(.focused?) | .id'", shell=True
            ).strip().decode()
            if window_id:
                subprocess.run(f'swaymsg [con_id={window_id}] focus', shell=True)
        except Exception:
            pass

    def run(self):
        self.open_scratch()


if __name__ == "__main__":
    swaypad = Swaypad()
    swaypad.run()
