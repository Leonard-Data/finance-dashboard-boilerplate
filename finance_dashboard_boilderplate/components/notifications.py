import reflex as rx

def notifications_dropdown() -> rx.Component:
    """Create a notifications dropdown."""
    return rx.menu.root(
        rx.menu.trigger(
            rx.button(
                rx.icon("bell"),
                variant="ghost",
                size="sm",
                radius="small"
            ),
        ),
        rx.menu.content(
            rx.menu.item("New Feature: Budget Tracking"),
            rx.menu.item("Account Alert: Unusual Activity"),
            rx.menu.item("Payment Due: Credit Card"),
            rx.menu.item("Investment Update: +5% Growth"),
            rx.menu.item("New Offer: Higher Interest Savings"),
            width="300px",
        ),
    )