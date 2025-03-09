import functools
import reflex as rx
from .base_template import base_template

def auth_template(title: str = "Authentication"):
    """Template decorator for authentication pages.
    
    Args:
        title: The page title.
        
    Returns:
        A decorator function that wraps a page component.
    """
    def decorator(page_func):
        @functools.wraps(page_func)
        @base_template(title=title)
        def wrapper(*args, **kwargs):
            # Get the page content
            page_content = page_func(*args, **kwargs)
            
            # Apply the auth template
            return rx.center(
                rx.vstack(
                    rx.heading("Financial Dashboard", size="xl", margin_bottom="6"),
                    rx.box(
                        page_content,
                        width="100%",
                        padding="6",
                        border_radius="lg",
                        border="1px solid var(--border)",
                        background="var(--card)",
                        box_shadow="lg",
                    ),
                    rx.flex(
                        rx.text("© 2025 Financial Dashboard", color="var(--muted-foreground)"),
                        rx.spacer(),
                        rx.hstack(
                            rx.link("Terms", href="#", color="var(--muted-foreground)"),
                            rx.link("Privacy", href="#", color="var(--muted-foreground)"),
                            rx.link("Help", href="#", color="var(--muted-foreground)"),
                            spacing="4",
                        ),
                        width="100%",
                        margin_top="8",
                        padding_x="4",
                    ),
                    max_width="md",
                    width="100%",
                    padding="6",
                    spacing="4",
                ),
                height="100vh",
                width="100%",
                background="var(--background)",
            )
        
        return wrapper
    
    return decorator