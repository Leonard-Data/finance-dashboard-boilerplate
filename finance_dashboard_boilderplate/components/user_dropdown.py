import reflex as rx

def user_dropdown() -> rx.Component:
    """Create a user dropdown."""
    return rx.menu.root(
        rx.menu.trigger(
            rx.flex(
                rx.avatar(
                    # name=UserState.full_name,
                    # src=UserState.avatar,
                    size="sm",
                ),
                rx.icon("chevron-down", font_size="xs", margin_left="2"),
                align_items="center",
            ),
        ),
        rx.menu.root(
            rx.menu.item(
                rx.text("Profile"),
                rx.icon("user"),
                on_click=rx.redirect("/settings/account"),
            ),
            rx.menu.item(
                rx.text("Settings"),
                rx.icon("settings"),
                on_click=rx.redirect("/settings"),
            ),
            rx.menu.separator(),
            rx.menu.item(
                rx.text("Logout"),
                rx.icon("log-out"),
                # on_click=AuthState.logout,
            ),
        ),
    )