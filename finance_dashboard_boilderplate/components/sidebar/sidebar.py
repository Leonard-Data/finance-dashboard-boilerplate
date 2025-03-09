import reflex as rx
from .state import State
from ...routes import get_sidebar_routes, is_route_active
from .sidebar_item import sidebar_item

def sidebar() -> rx.Component:
    """Create the sidebar component."""
    # Get sidebar routes
    sidebar_routes = get_sidebar_routes()
    
    # Split routes into main and footer sections
    main_routes = [route for route in sidebar_routes if route.icon not in ["settings", "help-circle"]]
    footer_routes = [route for route in sidebar_routes if route.icon in ["settings", "help-circle"]]
    
    return rx.box(
        rx.vstack(
            rx.flex(
                rx.heading("Flowers&Saints", size="md", display=["none", "none", "block"] if not SidebarState.is_collapsed else "none"),
                rx.spacer(),
                rx.button(
                    rx.icon("chevron-left", transform=f"rotate({90 if State.is_collapsed else 0}deg)"),
                    on_click=State.toggle_collapse,
                    variant="ghost",
                    size="sm",
                ),
                width="100%",
                padding="4",
                border_bottom="1px solid var(--border)",
            ),
            rx.vstack(
                *[sidebar_item(route) for route in main_routes],
                width="100%",
                spacing="1",
                align_items="flex-start",
                padding="2",
                overflow_y="auto",
                flex="1",
            ),
            rx.vstack(
                *[sidebar_item(route) for route in footer_routes],
                width="100%",
                spacing="1",
                align_items="flex-start",
                padding="2",
                border_top="1px solid var(--border)",
            ),
            height="100%",
            width=["0px", "0px", "72px", State.width],
            border_right="1px solid var(--border)",
            background="var(--background)",
            transition="width 0.2s ease-in-out",
            overflow="hidden",
        ),
        position=["fixed", "fixed", "relative"],
        height="100vh",
        z_index="10",
    )