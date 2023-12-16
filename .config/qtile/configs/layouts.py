from libqtile import layout
from .variables import colors, bg

layouts = [
        layout.MonadWide(
            align=1,
            border_focus=colors[18],
            border_normal=colors[1],
            border_width=2,
            new_client_position='before_current',
            ratio=.7,
            single_border_width=0,
            single_margin=0,
            ),
        layout.Max(),
        layout.TreeTab(
            active_bg=colors[12],
            active_fg=colors[0],
            border_width=0,
            bg_color=bg,
            inactive_bg=colors[0],
            place_right=True,
            previous_on_rm=True,
            sections=[''],
            section_fg=colors[0],
            vspace=0,
            ),
        ] 
