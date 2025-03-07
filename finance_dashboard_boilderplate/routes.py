from typing import Dict, List, Optional, Callable
import reflex as rx

class Route:
    """A class representing a route in the application."""
    
    def __init__(
        self,
        path: str,
        title: str,
        icon: str,
        component: Callable[[], rx.Component],
        requires_auth: bool = True,
        is_sidebar_item: bool = True,
        is_header_item: bool = False,
        children: List["Route"] = None,
        parent: Optional[str] = None,
    ):
        """Initialize a route.
        
        Args:
            path: The URL path for the route.
            title: The display title for the route.
            icon: The icon name for the route.
            component: The component function to render for this route.
            requires_auth: Whether authentication is required to access this route.
            is_sidebar_item: Whether this route should appear in the sidebar.
            is_header_item: Whether this route should appear in the header.
            children: List of child routes.
            parent: The parent route path (if this is a child route).
        """
        self.path = path
        self.title = title
        self.icon = icon
        self.component = component
        self.requires_auth = requires_auth
        self.is_sidebar_item = is_sidebar_item
        self.is_header_item = is_header_item
        self.children = children or []
        self.parent = parent
        
    def is_active(self, current_path: str) -> bool:
        """Check if this route is active based on the current path.
        
        Args:
            current_path: The current URL path.
            
        Returns:
            True if this route is active, False otherwise.
        """
        # Exact match
        if current_path == self.path:
            return True
        
        # Check if any child route is active
        for child in self.children:
            if child.is_active(current_path):
                return True
        
        # Check if this is a parent route and the current path starts with this path
        # but only if this path is not just "/"
        if self.path != "/" and current_path.startswith(self.path + "/"):
            return True
            
        return False
    
    def get_full_path(self) -> str:
        """Get the full path including parent paths.
        
        Returns:
            The full path.
        """
        if self.parent:
            parent_route = next((r for r in routes if r.path == self.parent), None)
            if parent_route:
                return f"{parent_route.get_full_path()}{self.path}"
        return self.path


# Import page components
from .pages import (
    dashboard_page,
    analytics_page,
    settings_page,
    organization_page,
    projects_page,
    transactions_page,
    invoices_page,
    payments_page,
    members_page,
    permissions_page,
    chat_page,
    meetings_page,
    help_page,
    login_page,
    register_page,
    forgot_password_page,
)

# Define all routes
routes: List[Route] = [
    Route(
        path="/",
        title="Dashboard",
        icon="home",
        component=dashboard_page.index,
        requires_auth=True,
    ),
    Route(
        path="/analytics",
        title="Analytics",
        icon="bar-chart-2",
        component=analytics_page.index,
        requires_auth=True,
    ),
    Route(
        path="/organization",
        title="Organization",
        icon="building",
        component=organization_page.index,
        requires_auth=True,
    ),
    Route(
        path="/projects",
        title="Projects",
        icon="folder",
        component=projects_page.index,
        requires_auth=True,
    ),
    Route(
        path="/transactions",
        title="Transactions",
        icon="wallet",
        component=transactions_page.index,
        requires_auth=True,
    ),
    Route(
        path="/invoices",
        title="Invoices",
        icon="receipt",
        component=invoices_page.index,
        requires_auth=True,
    ),
    Route(
        path="/payments",
        title="Payments",
        icon="credit-card",
        component=payments_page.index,
        requires_auth=True,
    ),
    Route(
        path="/members",
        title="Members",
        icon="users",
        component=members_page.index,
        requires_auth=True,
    ),
    Route(
        path="/permissions",
        title="Permissions",
        icon="shield",
        component=permissions_page.index,
        requires_auth=True,
    ),
    Route(
        path="/chat",
        title="Chat",
        icon="message-square",
        component=chat_page.index,
        requires_auth=True,
    ),
    Route(
        path="/meetings",
        title="Meetings",
        icon="video",
        component=meetings_page.index,
        requires_auth=True,
    ),
    Route(
        path="/settings",
        title="Settings",
        icon="settings",
        component=settings_page.index,
        requires_auth=True,
        children=[
            Route(
                path="/account",
                title="Account",
                icon="user",
                component=settings_page.account_settings,
                parent="/settings",
                is_sidebar_item=False,
            ),
            Route(
                path="/security",
                title="Security",
                icon="lock",
                component=settings_page.security_settings,
                parent="/settings",
                is_sidebar_item=False,
            ),
            Route(
                path="/preferences",
                title="Preferences",
                icon="sliders",
                component=settings_page.preferences_settings,
                parent="/settings",
                is_sidebar_item=False,
            ),
            Route(
                path="/notifications",
                title="Notifications",
                icon="bell",
                component=settings_page.notifications_settings,
                parent="/settings",
                is_sidebar_item=False,
            ),
            Route(
                path="/privacy",
                title="Privacy",
                icon="eye",
                component=settings_page.privacy_settings,
                parent="/settings",
                is_sidebar_item=False,
            ),
        ],
    ),
    Route(
        path="/help",
        title="Help",
        icon="help-circle",
        component=help_page.index,
        requires_auth=True,
    ),
    # Authentication routes
    Route(
        path="/login",
        title="Login",
        icon="log-in",
        component=login_page.index,
        requires_auth=False,
        is_sidebar_item=False,
    ),
    Route(
        path="/register",
        title="Register",
        icon="user-plus",
        component=register_page.index,
        requires_auth=False,
        is_sidebar_item=False,
    ),
    Route(
        path="/forgot-password",
        title="Forgot Password",
        icon="key",
        component=forgot_password_page.index,
        requires_auth=False,
        is_sidebar_item=False,
    ),
]

# Helper functions
def get_route_by_path(path: str) -> Optional[Route]:
    """Get a route by its path.
    
    Args:
        path: The path to look for.
        
    Returns:
        The Route object if found, None otherwise.
    """
    # First check for exact matches
    for route in routes:
        if route.path == path:
            return route
    
    # Then check for child routes
    for route in routes:
        for child in route.children:
            if child.path == path or route.path + child.path == path:
                return child
    
    return None

def get_sidebar_routes() -> List[Route]:
    """Get all routes that should appear in the sidebar.
    
    Returns:
        A list of Route objects.
    """
    return [route for route in routes if route.is_sidebar_item]

def get_header_routes() -> List[Route]:
    """Get all routes that should appear in the header.
    
    Returns:
        A list of Route objects.
    """
    return [route for route in routes if route.is_header_item]

def get_auth_required_routes() -> List[Route]:
    """Get all routes that require authentication.
    
    Returns:
        A list of Route objects.
    """
    return [route for route in routes if route.requires_auth]

def get_public_routes() -> List[Route]:
    """Get all routes that don't require authentication.
    
    Returns:
        A list of Route objects.
    """
    return [route for route in routes if not route.requires_auth]

def is_route_active(path: str, current_path: str) -> bool:
    """Check if a route is active based on the current path.
    
    Args:
        path: The route path to check.
        current_path: The current URL path.
        
    Returns:
        True if the route is active, False otherwise.
    """
    route = get_route_by_path(path)
    if route:
        return route.is_active(current_path)
    return False

def get_breadcrumbs(current_path: str) -> List[Dict[str, str]]:
    """Generate breadcrumbs for the current path.
    
    Args:
        current_path: The current URL path.
        
    Returns:
        A list of breadcrumb items with 'title' and 'path' keys.
    """
    breadcrumbs = [{"title": "Home", "path": "/"}]
    
    if current_path == "/":
        return breadcrumbs
    
    # Split the path and build breadcrumbs
    parts = current_path.strip("/").split("/")
    current = ""
    
    for part in parts:
        current += f"/{part}"
        route = get_route_by_path(current)
        
        if route:
            breadcrumbs.append({"title": route.title, "path": current})
        else:
            # If we can't find a route, use the path segment as the title
            breadcrumbs.append({"title": part.capitalize(), "path": current})
    
    return breadcrumbs