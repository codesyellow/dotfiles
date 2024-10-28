import re
from libqtile.config import Group, ScratchPad, Match
from .variables import icons
from .scratchpads import scratchpads

groups = [
        Group(icons[0], layout='max', matches=[Match(wm_class=re.compile(r"^(Alacritty|st)$"))]),
        Group(icons[1], layout='max', matches=[Match(wm_class=re.compile(r"^(audacious|gimp|kdenlive)$"))]),
        Group(icons[2], layout='max', matches=[Match(wm_class=re.compile(r"^(navigator|firefox|Brave\-browser|qutebrowser|org\.qutebrowser\.qutebrowser|floorp)$"))]),
        Group(icons[3], layout='max', matches=[Match(wm_class=re.compile(r"^(heroic|Steam|amazon\ games\ ui\.exe|bottles|ProtonUp\-Qt|lutris|amazongamessetup\.exe|net\.davidotek\.pupgui2)$")),
                                               Match(title=re.compile(r"^(Steam\ \-\ Self\ Updater|Special\ Offers|Steam\ setup|Steam|Sign\ in\ to\ Steam)$"))]),
        Group(icons[4], layout='max', matches=[Match(wm_class=re.compile(r"^(Youtube\ Music|youtube\ music)$"))]),
        Group(icons[5], layout='max', matches=[Match(wm_class=re.compile(r"^(DL: language lessons|Zathura|mpv|Microsoft\-edge|anki|TelegramDesktop)$"))]),
                                                   ScratchPad('scratchpad', scratchpads),
                                                   ]

