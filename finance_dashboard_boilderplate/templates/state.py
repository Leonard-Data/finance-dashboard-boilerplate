import reflex as rx


class ThemeState(rx.State):
    """The state for the theme of the app."""
    accent_color: str = "custom"
    gray_color: str = "gray"
    radius: str = "large"
    scaling: str = "100%"
