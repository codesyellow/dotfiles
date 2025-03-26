#!/usr/bin/env python
MAIN_FONT = "Germania One"
TITLE_FONT = MAIN_FONT
CONTENT_FONT = MAIN_FONT
TITLE_BOLD = "800"
CONTENT_BOLD = "800"
FONT_COLOR = "#4c566a"


def get_pango(title, content):
    """Return the pango string"""
    title_pango = f"<span foreground='{FONT_COLOR}' font_family='{
        TITLE_FONT}'>{title} </span>"
    content_pango = f"<span font_family='{CONTENT_FONT}'>{content}</span>"
    return title_pango + content_pango
