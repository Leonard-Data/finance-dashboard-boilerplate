import reflex as rx
from .state import State
from ...routes import get_sidebar_routes, is_route_active

def sidebar_item(route) -> rx.Component:
    """Create a sidebar navigation item."""
    return rx.link(
        rx.flex(
            rx.icon(
                route.icon,
                color="var(--muted-foreground)" if not is_route_active(route.path, rx.State.router.page.path) else "var(--primary)",
                font_size="1.2em",
            ),
            rx.text(
                route.title, 
                margin_left="3", 
                display=["none", "none", "block"] if not State.is_collapsed else "none"
            ),
            align_items="center",
            padding="2",
            border_radius="md",
            background="var(--accent)" if is_route_active(route.path, rx.State.router.page.path) else "transparent",
            color="var(--primary)" if is_route_active(route.path, rx.State.router.page.path) else "var(--muted-foreground)",
            _hover={
                "background": "var(--accent)",
                "color": "var(--primary)",
            },
        ),
        href=route.path,
        width="100%",
        text_decoration="none",
    )

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