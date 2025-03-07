import reflex as rx

def sidebar_item(icon: str, text: str, href: str, is_active: bool = False) -> rx.Component:
    """Create a sidebar navigation item."""
    return rx.link(
        rx.flex(
            rx.icon(
                icon,
                color="var(--muted-foreground)" if not is_active else "var(--primary)",
                font_size="1.2em",
            ),
            rx.text(text, margin_left="3", display=["none", "none", "block"]),
            align_items="center",
            padding="2",
            border_radius="md",
            background="var(--accent)" if is_active else "transparent",
            color="var(--primary)" if is_active else "var(--muted-foreground)",
            _hover={
                "background": "var(--accent)",
                "color": "var(--primary)",
            },
        ),
        href=href,
        width="100%",
        text_decoration="none",
    )