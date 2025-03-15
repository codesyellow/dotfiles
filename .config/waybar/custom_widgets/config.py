#!/usr/bin/env python

TITLE_FONT = "IBM Plex Sans"
TITLE_BOLD = "100"
CONTENT_FONT = "IBM Plex Sans"
CONTENT_BOLD = "600"


def get_pango(title, content):
    """Return the pango string"""
    title_pango = f"<span font_family='{
        TITLE_FONT}' font_weight='{TITLE_BOLD}'>{title} </span>"
    content_pango = f"<span font_family='{
        CONTENT_FONT}' font_weight='{CONTENT_BOLD}'>{content}</span>"
    return title_pango + content_pango
