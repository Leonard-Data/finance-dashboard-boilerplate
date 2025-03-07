import reflex as rx
from ...components.notifications import notifications_dropdown
from ...components.user_dropdown import user_dropdown
from .breadcrumb import breadcrumbs

def navbar() -> rx.Component:
    """Create the top navigation component."""
    return rx.box(
        rx.flex(
            breadcrumbs(),
            rx.spacer(),
            rx.hstack(
                notifications_dropdown(),
                rx.color_mode.button(style={"opacity": "0.8", "scale": "0.95"}),
                user_dropdown(),
                spacing="4",
            ),
            width="100%",
            padding="4",
            border_bottom="1px solid var(--border)",
        ),
        position="sticky",
        top="0",
        background="var(--background)",
        z_index="5",
    )