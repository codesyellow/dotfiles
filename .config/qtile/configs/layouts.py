from libqtile import layout
from .variables import colors
from .functions import has_class

layouts = [
        layout.MonadWide(
            align=1,
            border_focus=colors[12],
            border_normal=colors[15],
            border_width=2,
            new_client_position='before_current',
            ratio=.6,
            single_border_width=0,
            single_margin=0,
            ),
        layout.Max(),
        layout.TreeTab(
            active_bg=colors[12],
            active_fg=colors[0],
            border_width=0,
            bg_color=colors[1],
            inactive_bg=colors[0],
            place_right=True,
            previous_on_rm=True,
            sections=[''],
            section_fg=colors[0],
            vspace=0,
            ),
        ] 

floating_layout = layout.Floating(
    border_focus = colors[4],
    border_normal = '#98971a',
    border_width = 2,
    margin = 2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        has_class("pavucontrol"),
        has_class("com.github.wwmm.easyeffects"),
        has_class("net.davidotek.pupgui2"),
        has_class('moderndeck'),
        has_class('ProtonUp-Qt'),
        has_class('monophony'),
        has_class('Whatsapp-for-linux'),
        ]
        )
