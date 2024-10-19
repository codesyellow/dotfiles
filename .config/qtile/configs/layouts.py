from libqtile import layout
from .variables import bg, fg, al

layouts = [
    layout.MonadWide(
        align=1,
        border_focus=al,
        border_normal=bg,
        border_width=2,
        new_client_position='before_current',
        ratio=.7,
        single_border_width=0,
        single_margin=0,
    ),
    layout.Max(),
] 
