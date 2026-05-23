import flet as ft


CURRENT_THEME = "light"

_LIGHT = {
    "bg": ft.Colors.BLUE_GREY_50,
    "surface": ft.Colors.WHITE,
    "divider": ft.Colors.BLUE_GREY_100,
    "text_primary": ft.Colors.BLUE_GREY_900,
    "text_secondary": ft.Colors.BLUE_GREY_500,
    "border": ft.Colors.BLUE_GREY_200,
    "accent": ft.Colors.BLUE_600,
    "accent_bg": ft.Colors.BLUE_50,
    "primary": ft.Colors.BLUE_600,
    "on_primary": ft.Colors.WHITE,
    "navbar_inactive": ft.Colors.BLUE_GREY_700,
    "navbar_brand": ft.Colors.BLUE_700,
    "topbar_title": ft.Colors.BLUE_GREY_900,
    "topbar_date": ft.Colors.BLUE_GREY_500,
    "notification_text": ft.Colors.BLUE_GREY_600,
    "notification_icon": ft.Colors.CYAN_500,
    "table_heading": ft.Colors.BLUE_GREY_50,
}

_DARK = {
    "bg": ft.Colors.BLUE_GREY_900,
    "surface": ft.Colors.BLUE_GREY_800,
    "divider": ft.Colors.BLUE_GREY_700,
    "text_primary": ft.Colors.BLUE_GREY_100,
    "text_secondary": ft.Colors.BLUE_GREY_400,
    "border": ft.Colors.BLUE_GREY_700,
    "accent": ft.Colors.BLUE_400,
    "accent_bg": ft.Colors.BLUE_900,
    "primary": ft.Colors.BLUE_500,
    "on_primary": ft.Colors.WHITE,
    "navbar_inactive": ft.Colors.BLUE_GREY_400,
    "navbar_brand": ft.Colors.BLUE_400,
    "topbar_title": ft.Colors.BLUE_GREY_100,
    "topbar_date": ft.Colors.BLUE_GREY_400,
    "notification_text": ft.Colors.BLUE_GREY_400,
    "notification_icon": ft.Colors.CYAN_300,
    "table_heading": ft.Colors.BLUE_GREY_800,
}


def get(key):
    return (_DARK if CURRENT_THEME == "dark" else _LIGHT)[key]


def toggle():
    global CURRENT_THEME
    CURRENT_THEME = "dark" if CURRENT_THEME == "light" else "light"


def is_dark():
    return CURRENT_THEME == "dark"
