import reflex as rx



class State(rx.State):
    is_collapsed: bool = False
    width: str ="150px"
    
    
    @rx.event
    async def toggle_collapse(self):
        self.is_collapsed = not self.is_collapsed