import reflex as rx
from typing import Dict, Optional

class NotificationSettings:
    """Notification settings for a user."""
    
    def __init__(
        self,
        account_activity: bool = True,
        new_features: bool = True,
        marketing: bool = False,
    ):
        self.account_activity = account_activity
        self.new_features = new_features
        self.marketing = marketing

class PrivacySettings:
    """Privacy settings for a user."""
    
    def __init__(
        self,
        share_usage_data: bool = True,
        allow_recommendations: bool = True,
        profile_visible: bool = True,
        show_activity: bool = True,
    ):
        self.share_usage_data = share_usage_data
        self.allow_recommendations = allow_recommendations
        self.profile_visible = profile_visible
        self.show_activity = show_activity

class UserState(rx.State):
    """User state for the application."""
    
    # User profile
    full_name: str = "John Doe"
    email: str = "john.doe@example.com"
    phone: str = "+1 (555) 123-4567"
    avatar: str = "/placeholder.svg?height=40&width=40"
    
    # User preferences
    language: str = "English"
    currency: str = "USD ($)"
    two_factor_enabled: bool = False
    
    # Notification settings
    email_notifications: NotificationSettings = NotificationSettings()
    push_notifications: NotificationSettings = NotificationSettings()
    
    # Privacy settings
    privacy: PrivacySettings = PrivacySettings()
    
    # UI state
    is_delete_account_modal_open: bool = False
    
    def save_profile(self):
        """Save user profile changes."""
        # In a real app, you would send this to an API
        # For demo purposes, we'll just show a notification
        return rx.window_alert("Profile saved successfully!")
    
    def toggle_two_factor(self, value: bool):
        """Toggle two-factor authentication."""
        self.two_factor_enabled = value
    
    def set_language(self, value: str):
        """Set user language preference."""
        self.language = value
    
    def set_currency(self, value: str):
        """Set user currency preference."""
        self.currency = value
    
    # Email notification toggles
    def toggle_email_account_activity(self, value: bool):
        """Toggle email notifications for account activity."""
        self.email_notifications.account_activity = value
    
    def toggle_email_new_features(self, value: bool):
        """Toggle email notifications for new features."""
        self.email_notifications.new_features = value
    
    def toggle_email_marketing(self, value: bool):
        """Toggle email notifications for marketing."""
        self.email_notifications.marketing = value
    
    # Push notification toggles
    def toggle_push_account_activity(self, value: bool):
        """Toggle push notifications for account activity."""
        self.push_notifications.account_activity = value
    
    def toggle_push_new_features(self, value: bool):
        """Toggle push notifications for new features."""
        self.push_notifications.new_features = value
    
    def toggle_push_marketing(self, value: bool):
        """Toggle push notifications for marketing."""
        self.push_notifications.marketing = value
    
    # Privacy toggles
    def toggle_share_usage_data(self, value: bool):
        """Toggle sharing usage data."""
        self.privacy.share_usage_data = value
    
    def toggle_allow_recommendations(self, value: bool):
        """Toggle allowing personalized recommendations."""
        self.privacy.allow_recommendations = value
    
    def toggle_profile_visible(self, value: bool):
        """Toggle profile visibility."""
        self.privacy.profile_visible = value
    
    def toggle_show_activity(self, value: bool):
        """Toggle showing activity status."""
        self.privacy.show_activity = value
    
    def download_data(self):
        """Download user data."""
        # In a real app, you would generate and download a file
        # For demo purposes, we'll just show a notification
        return rx.window_alert("Your data is being prepared for download. You will receive an email when it's ready.")
    
    def show_delete_account_modal(self):
        """Show the delete account confirmation modal."""
        self.is_delete_account_modal_open = True
    
    def hide_delete_account_modal(self):
        """Hide the delete account confirmation modal."""
        self.is_delete_account_modal_open = False
    
    def delete_account(self):
        """Delete the user account."""
        # In a real app, you would send this to an API
        # For demo purposes, we'll just show a notification and redirect
        self.hide_delete_account_modal()
        return [
            rx.window_alert("Your account has been scheduled for deletion. You will be logged out now."),
            rx.redirect("/login"),
        ]