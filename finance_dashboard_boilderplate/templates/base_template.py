"""Common templates used between pages in the app."""

from __future__ import annotations

from typing import Callable

import reflex as rx

from .. import styles
from .state import ThemeState
# Meta tags for the app.
default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1",
    },
]

def base_template(
    route: str | None = None,
    title: str | None = None,
    description: str | None = None,
    meta: str | None = None,
    script_tags: list[rx.Component] | None = None,
    on_load: rx.EventHandler | list[rx.EventHandler] | None = None,
) -> Callable[[Callable[[], rx.Component]], rx.Component]:
    """The template for each page of the app.

    Args:
        route: The route to reach the page.
        title: The title of the page.
        description: The description of the page.
        meta: Additional meta to add to the page.
        on_load: The event handler(s) called when the page load.
        script_tags: Scripts to attach to the page.

    Returns:
        The template with the page content.

    """

    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        """The template for each page of the app.

        Args:
            page_content: The content of the page.

        Returns:
            The template with the page content.

        """
        # Get the meta tags for the page.
        all_meta = [*default_meta, *(meta or [])]

        def templated_page():
            return rx.box(
                        page_content(),
                        min_height="100vh",
                        width="100%",
                    )

        @rx.page(
            route=route,
            title=title,
            description=description,
            meta=all_meta,
            script_tags=script_tags,
            on_load=on_load,
        )
        def theme_wrap():
            return rx.theme(
                templated_page(),
                has_background=True,
                accent_color=ThemeState.accent_color,
                gray_color=ThemeState.gray_color,
                radius=ThemeState.radius,
                scaling=ThemeState.scaling,
            )

        return theme_wrap

    return decorator

import functools
import reflex as rx

def base_template(title: str = "Financial Dashboard"):
    """Base template decorator for all pages.
    
    Args:
        title: The page title.
        
    Returns:
        A decorator function that wraps a page component.
    """
    def decorator(page_func):
        @functools.wraps(page_func)
        def wrapper(*args, **kwargs):
            # Get the page content
            page_content = page_func(*args, **kwargs)
            
            # Apply the base template
            return rx.theme(
                rx.box(
                    page_content,
                    min_height="100vh",
                    width="100%",
                ),
                has_background=True,
                accent_color=ThemeState.accent_color,
                gray_color=ThemeState.gray_color,
                radius=ThemeState.radius,
                scaling=ThemeState.scaling,
            )
        
        return wrapper
    
    return decorator