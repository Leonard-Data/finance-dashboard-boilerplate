import functools
import reflex as rx
from .dashboard_template import dashboard_template
from ..routes import get_route_by_path

def settings_template(title: str = "Settings"):
    """Template decorator for settings pages.
    
    Args:
        title: The page title.
        
    Returns:
        A decorator function that wraps a page component.
    """
    def decorator(page_func):
        @functools.wraps(page_func)
        @dashboard_template(title=title)
        def wrapper(*args, **kwargs):
            # Get the page content
            page_content = page_func(*args, **kwargs)
            
            # Get settings routes
            settings_route = get_route_by_path("/settings")
            settings_tabs = []
            
            if settings_route and settings_route.children:
                for child in settings_route.children:
                    settings_tabs.append(
                        rx.link(
                            rx.flex(
                                rx.icon(child.icon, margin_right="2"),
                                rx.text(child.title),
                                align_items="center",
                                padding="2",
                                border_radius="md",
                                background="var(--accent)" 
                                    if rx.State.router.page.path == f"/settings{child.path}" 
                                    else "transparent",
                                color="var(--primary)" 
                                    if rx.State.router.page.path == f"/settings{child.path}" 
                                    else "var(--muted-foreground)",
                                _hover={
                                    "background": "var(--accent)",
                                    "color": "var(--primary)",
                                },
                            ),
                            href=f"/settings{child.path}",
                            width="100%",
                            text_decoration="none",
                        )
                    )
            
            # Apply the settings template
            return rx.flex(
                rx.box(
                    rx.vstack(
                        rx.heading("Settings", size="lg", margin_bottom="4"),
                        *settings_tabs,
                        width="100%",
                        spacing="1",
                        align_items="flex-start",
                    ),
                    width="250px",
                    padding="4",
                    border_right="1px solid var(--border)",
                ),
                rx.box(
                    page_content,
                    flex="1",
                    padding="4",
                ),
                width="100%",
                border_radius="lg",
                border="1px solid var(--border)",
                background="var(--card)",
                overflow="hidden",
            )
        
        return wrapper
    
    return decorator