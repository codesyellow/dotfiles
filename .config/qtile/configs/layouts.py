from libqtile import layout
from libqtile.config import Match
from .variables import COLORS

layouts = [
    #    layout.MonadWide(
    #        align=1,
    #        border_focus=al,
    #        border_normal=bg,
    #        border_width=2,
    #        new_client_position="before_current",
    #        ratio=0.7,
    #        single_border_width=0,
    #        single_margin=0,
    #    ),
    layout.Max(),
]

floating_layout = layout.Floating(
    border_focus=COLORS["alt"],
    border_normal=COLORS["bg"],
    border_width=2,
    margin=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="Tk"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="blueman-manager"),
        Match(wm_class="org.kde.polkit-kde-authentication-agent-1"),
        Match(wm_class="CachyOSHello"),
        Match(wm_class="org.cachyos.cachyos-kernel-manager"),
        Match(title="anki-vim"),
        Match(title="maps"),
    ],
)
