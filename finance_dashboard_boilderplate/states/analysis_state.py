import reflex as rx
from typing import List, Dict, Any
from datetime import datetime, timedelta

class AnalyticsState(rx.State):
    """State for the analytics page."""
    
    # Analytics data
    revenue_data: List[Dict[str, Any]] = []
    user_activity_data: List[Dict[str, Any]] = []
    top_products: List[Dict[str, Any]] = []
    account_growth: List[Dict[str, Any]] = []
    
    # Date range filter
    start_date: str = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    end_date: str = datetime.now().strftime("%Y-%m-%d")
    
    # Loading states
    is_loading_revenue: bool = False
    is_loading_activity: bool = False
    is_loading_products: bool = False
    is_loading_growth: bool = False
    
    def fetch_analytics_data(self):
        """Fetch all analytics data on page load."""
        return [
            self.fetch_revenue_data(),
            self.fetch_user_activity(),
            self.fetch_top_products(),
            self.fetch_account_growth(),
        ]
    
    async def fetch_revenue_data(self):
        """Fetch revenue data for the selected date range."""
        self.is_loading_revenue = True
        
        try:
            # In a real app, you would fetch from an API with the date range
            import asyncio
            await asyncio.sleep(0.7)  # Simulate API delay
            
            # Generate mock data for the last 30 days
            self.revenue_data = []
            base_date = datetime.now() - timedelta(days=30)
            
            for i in range(31):
                date = base_date + timedelta(days=i)
                self.revenue_data.append({
                    "date": date.strftime("%Y-%m-%d"),
                    "revenue": 1000 + (i * 50) + (100 * (i % 7)),  # Some pattern with weekly cycle
                })
        except Exception as e:
            print(f"Error fetching revenue data: {e}")
        
        self.is_loading_revenue = False
    
    async def fetch_user_activity(self):
        """Fetch user activity data for the selected date range."""
        self.is_loading_activity = True
        
        try:
            # In a real app, you would fetch from an API with the date range
            import asyncio
            await asyncio.sleep(0.6)  # Simulate API delay
            
            # Generate mock data for the last 30 days
            self.user_activity_data = []
            base_date = datetime.now() - timedelta(days=30)
            
            for i in range(31):
                date = base_date + timedelta(days=i)
                self.user_activity_data.append({
                    "date": date.strftime("%Y-%m-%d"),
                    "active_users": 500 + (i * 10) + (50 * (i % 7)),  # Some pattern with weekly cycle
                    "new_users": 50 + (i * 2) + (20 * (i % 7)),  # Some pattern with weekly cycle
                })
        except Exception as e:
            print(f"Error fetching user activity data: {e}")
        
        self.is_loading_activity = False
    
    async def fetch_top_products(self):
        """Fetch top products data."""
        self.is_loading_products = True
        
        try:
            # In a real app, you would fetch from an API
            import asyncio
            await asyncio.sleep(0.5)  # Simulate API delay
            
            self.top_products = [
                {"id": 1, "name": "Premium Plan", "revenue": 45000, "users": 150},
                {"id": 2, "name": "Basic Plan", "revenue": 30000, "users": 300},
                {"id": 3, "name": "Enterprise Plan", "revenue": 25000, "users": 25},
                {"id": 4, "name": "Add-on: Tax Filing", "revenue": 15000, "users": 100},
                {"id": 5, "name": "Add-on: Budgeting", "revenue": 10000, "users": 200},
            ]
        except Exception as e:
            print(f"Error fetching top products: {e}")
        
        self.is_loading_products = False
    
    async def fetch_account_growth(self):
        """Fetch account growth data."""
        self.is_loading_growth = True
        
        try:
            # In a real app, you would fetch from an API
            import asyncio
            await asyncio.sleep(0.8)  # Simulate API delay
            
            # Generate mock data for the last 12 months
            self.account_growth = []
            base_date = datetime.now() - timedelta(days=365)
            
            for i in range(12):
                date = base_date + timedelta(days=i*30)
                self.account_growth.append({
                    "month": date.strftime("%b %Y"),
                    "accounts": 1000 + (i * 200) + (100 * (i % 3)),  # Some pattern with quarterly cycle
                })
        except Exception as e:
            print(f"Error fetching account growth: {e}")
        
        self.is_loading_growth = False
    
    def update_date_range(self, start_date: str, end_date: str):
        """Update the date range and refresh data."""
        self.start_date = start_date
        self.end_date = end_date
        
        # Refresh data with new date range
        return self.fetch_analytics_data()