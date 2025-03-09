import reflex as rx
from typing import Optional, Dict, Any

class AuthState(rx.State):
    """Authentication state for the application."""
    
    # User authentication state
    is_authenticated: bool = False
    user_id: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    
    # Login form state
    login_email: str = ""
    login_password: str = ""
    login_error: Optional[str] = None
    login_processing: bool = False
    
    # Registration form state
    register_name: str = ""
    register_email: str = ""
    register_password: str = ""
    register_confirm_password: str = ""
    register_error: Optional[str] = None
    register_processing: bool = False
    
    # Password reset state
    reset_email: str = ""
    reset_error: Optional[str] = None
    reset_processing: bool = False
    reset_success: bool = False
    
    def login(self):
        """Handle user login."""
        self.login_processing = True
        self.login_error = None
        
        # In a real app, you would validate credentials against a backend
        # For this example, we'll just simulate a successful login
        if self.login_email and self.login_password:
            # Simulate API call delay
            import asyncio
            yield asyncio.sleep(1)
            
            # For demo purposes, accept any non-empty credentials
            self.is_authenticated = True
            self.username = self.login_email.split("@")[0]
            self.email = self.login_email
            self.user_id = "user123"
            self.access_token = "demo_access_token"
            self.refresh_token = "demo_refresh_token"
            
            # Save auth tokens to localStorage
            token_data = {
                "access_token": self.access_token,
                "refresh_token": self.refresh_token,
                "user_id": self.user_id,
                "username": self.username,
                "email": self.email,
            }
            rx.set_local_storage("auth_tokens", token_data)
            
            # Redirect to dashboard
            return rx.redirect("/")
        else:
            self.login_error = "Please enter both email and password."
        
        self.login_processing = False
    
    def register(self):
        """Handle user registration."""
        self.register_processing = True
        self.register_error = None
        
        # Validate form inputs
        if not self.register_name:
            self.register_error = "Please enter your name."
        elif not self.register_email:
            self.register_error = "Please enter your email."
        elif not self.register_password:
            self.register_error = "Please enter a password."
        elif self.register_password != self.register_confirm_password:
            self.register_error = "Passwords do not match."
        else:
            # Simulate API call delay
            import asyncio
            yield asyncio.sleep(1)
            
            # For demo purposes, registration always succeeds
            # Redirect to login page
            self.register_processing = False
            return rx.redirect("/login")
        
        self.register_processing = False
    
    def reset_password(self):
        """Handle password reset request."""
        self.reset_processing = True
        self.reset_error = None
        
        if not self.reset_email:
            self.reset_error = "Please enter your email."
        else:
            # Simulate API call delay
            import asyncio
            yield asyncio.sleep(1)
            
            # For demo purposes, reset always succeeds
            self.reset_success = True
        
        self.reset_processing = False
    
    def logout(self):
        """Handle user logout."""
        # Clear authentication state
        self.is_authenticated = False
        self.user_id = None
        self.username = None
        self.email = None
        self.access_token = None
        self.refresh_token = None
        
        # Clear localStorage
        rx.clear_local_storage("auth_tokens")
        
        # Redirect to login page
        return rx.redirect("/login")
    
    async def check_auth_on_load(self):
        """Check authentication status when the app loads."""
        # Try to get auth tokens from localStorage
        tokens = await rx.get_local_storage("auth_tokens")
        
        if tokens:
            # Restore authentication state
            self.is_authenticated = True
            self.user_id = tokens.get("user_id")
            self.username = tokens.get("username")
            self.email = tokens.get("email")
            self.access_token = tokens.get("access_token")
            self.refresh_token = tokens.get("refresh_token")
            
            # In a real app, you would validate the token with your backend
            # If invalid, you would clear the state and redirect to login