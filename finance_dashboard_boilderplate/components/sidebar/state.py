import reflex as rx



class State(rx.State):
    """State for the sidebar component."""
    
    # Sidebar state
    is_collapsed: bool = False
    width: str = "240px"
    
    def toggle_collapse(self):
        """Toggle sidebar collapse state."""
        self.is_collapsed = not self.is_collapsed
        self.width = "72px" if self.is_collapsed else "240px"