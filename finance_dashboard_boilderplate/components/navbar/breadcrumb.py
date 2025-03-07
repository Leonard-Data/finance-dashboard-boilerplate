import reflex as rx
from ...routes import get_breadcrumbs

def breadcrumbs() -> rx.Component:
    """Create breadcrumbs based on the current route."""
    current_path = rx.State.router.page.path
    breadcrumb_items = get_breadcrumbs(current_path)
    
    return rx.hstack(
        *[
            rx.link(item["title"], href=item["path"])
            for item in breadcrumb_items
        ],
        display=["none", "none", "flex"],
        )