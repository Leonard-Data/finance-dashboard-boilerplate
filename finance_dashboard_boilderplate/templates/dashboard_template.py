import functools
import reflex as rx
from .base_template import base_template
from ..components.navbar import  navbar
from ..components.sidebar import sidebar

from ..states import AuthState

def dashboard_template(title: str = "Dashboard", require_auth: bool = True, on_load=None):
    """Template decorator for dashboard pages.
    
    Args:
        title: The page title.
        require_auth: Whether authentication is required.
        on_load: Function(s) to execute when the page loads.
        
    Returns:
        A decorator function that wraps a page component.
    """
    def decorator(page_func):
        @functools.wraps(page_func)
        @base_template(title=title)
        def wrapper(*args, **kwargs):
            # Check authentication if required
            if require_auth and not AuthState.is_authenticated:
                return rx.redirect("/login")
            
            # Get the page content
            page_content = page_func(*args, **kwargs)
            
            # Combine template on_load with page on_load
            template_on_load = AuthState.check_auth_on_load
            
            # Determine the final on_load
            final_on_load = None
            if on_load and template_on_load:
                if isinstance(on_load, list):
                    final_on_load = [template_on_load] + on_load
                else:
                    final_on_load = [template_on_load, on_load]
            elif on_load:
                final_on_load = on_load
            elif template_on_load:
                final_on_load = template_on_load
            
            # Apply the dashboard template
            return rx.flex(
                sidebar.sidebar(),
                rx.box(
                    navbar.navbar(),
                    rx.box(
                        page_content,
                        padding="6",
                        max_width="7xl",
                        margin="0 auto",
                    ),
                    flex="1",
                    overflow="auto",
                ),
                on_load=final_on_load,
                height="100vh",
                width="100%",
            )
        
        return wrapper
    
    return decorator