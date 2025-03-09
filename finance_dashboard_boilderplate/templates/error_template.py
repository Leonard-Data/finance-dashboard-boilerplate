import functools
import reflex as rx
from .base_template import base_template

def error_template(title: str = "Error"):
    """Template decorator for error pages.
    
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
            
            # Apply the error template
            return rx.center(
                rx.vstack(
                    page_content,
                    spacing="4",
                    padding="8",
                    align_items="center",
                    max_width="md",
                    width="100%",
                ),
                height="100vh",
                width="100%",
                background="var(--background)",
            )
        
        return wrapper
    
    return decorator