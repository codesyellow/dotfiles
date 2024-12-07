# type: ignore
from .variables import home

wks1class_rules = "Alacritty|st"
wks2class_rules = "audacious|gimp|kdenlive"
wks3class_rules = (
    "navigator|firefox|Brave\-browser|qutebrowser|org\.qutebrowser\.qutebrowser|floorp"
)
wks4class_rules = "heroic|Steam|amazon\ games\ ui\.exe|bottles|ProtonUp\-Qt|lutris|amazongamessetup\.exe|net\.davidotek\.pupgui2"
wks5class_rules = "Youtube\ Music|youtube\ music"
wks6class_rules = (
    "DL: language lessons|Zathura|mpv|Microsoft\-edge|anki|TelegramDesktop"
)

# title
wks2title_rules = "Media viewer"
wks4title_rules = (
    "Steam\ \-\ Self\ Updater|Special\ Offers|Steam\ setup|Steam|Sign\ in\ to\ Steam"
)

game_rules = ""

games_classes_file = (
    open(f"{home}/.config/qtile/configs/game_classes", "r").read().splitlines()
)
counter = 0

for class_name in games_classes_file:
    if counter == 0:
        game_rules += f"{class_name.strip()}"
        counter += 1
    else:
        game_rules += f"|{class_name.strip()}"

wks7class_rules = game_rules
