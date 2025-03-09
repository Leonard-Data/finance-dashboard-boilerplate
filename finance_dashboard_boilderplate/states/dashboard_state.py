import reflex as rx
from typing import List, Dict, Any

class DashboardState(rx.State):
    """State for the dashboard page."""
    
    # Dashboard data
    accounts: List[Dict[str, Any]] = []
    transactions: List[Dict[str, Any]] = []
    budget_categories: List[Dict[str, Any]] = []
    savings_goals: List[Dict[str, Any]] = []
    
    # Loading states
    is_loading_accounts: bool = False
    is_loading_transactions: bool = False
    is_loading_budget: bool = False
    is_loading_goals: bool = False
    
    def fetch_dashboard_data(self):
        """Fetch all dashboard data on page load."""
        return [
            self.fetch_accounts(),
            self.fetch_transactions(),
            self.fetch_budget_categories(),
            self.fetch_savings_goals(),
        ]
    
    async def fetch_accounts(self):
        """Fetch user accounts."""
        self.is_loading_accounts = True
        
        try:
            # In a real app, you would fetch from an API
            # For demo purposes, we'll use mock data
            import asyncio
            await asyncio.sleep(0.5)  # Simulate API delay
            
            self.accounts = [
                {"id": 1, "name": "Checking", "balance": 2543.21, "type": "checking"},
                {"id": 2, "name": "Savings", "balance": 12750.83, "type": "savings"},
                {"id": 3, "name": "Investment", "balance": 34892.45, "type": "investment"},
            ]
        except Exception as e:
            print(f"Error fetching accounts: {e}")
        
        self.is_loading_accounts = False
    
    async def fetch_transactions(self):
        """Fetch recent transactions."""
        self.is_loading_transactions = True
        
        try:
            # In a real app, you would fetch from an API
            import asyncio
            await asyncio.sleep(0.7)  # Simulate API delay
            
            self.transactions = [
                {"id": 1, "description": "Grocery Store", "amount": -82.45, "date": "2025-03-05", "category": "Food"},
                {"id": 2, "description": "Salary Deposit", "amount": 3200.00, "date": "2025-03-01", "category": "Income"},
                {"id": 3, "description": "Electric Bill", "amount": -145.30, "date": "2025-02-28", "category": "Utilities"},
                {"id": 4, "description": "Restaurant", "amount": -64.20, "date": "2025-02-25", "category": "Dining"},
                {"id": 5, "description": "Gas Station", "amount": -48.75, "date": "2025-02-23", "category": "Transportation"},
            ]
        except Exception as e:
            print(f"Error fetching transactions: {e}")
        
        self.is_loading_transactions = False
    
    async def fetch_budget_categories(self):
        """Fetch budget categories."""
        self.is_loading_budget = True
        
        try:
            # In a real app, you would fetch from an API
            import asyncio
            await asyncio.sleep(0.6)  # Simulate API delay
            
            self.budget_categories = [
                {"id": 1, "name": "Housing", "budget": 1200, "spent": 1150, "color": "blue"},
                {"id": 2, "name": "Food", "budget": 500, "spent": 420, "color": "green"},
                {"id": 3, "name": "Transportation", "budget": 300, "spent": 275, "color": "purple"},
                {"id": 4, "name": "Entertainment", "budget": 200, "spent": 180, "color": "orange"},
                {"id": 5, "name": "Utilities", "budget": 250, "spent": 230, "color": "red"},
            ]
        except Exception as e:
            print(f"Error fetching budget categories: {e}")
        
        self.is_loading_budget = False
    
    async def fetch_savings_goals(self):
        """Fetch savings goals."""
        self.is_loading_goals = True
        
        try:
            # In a real app, you would fetch from an API
            import asyncio
            await asyncio.sleep(0.8)  # Simulate API delay
            
            self.savings_goals = [
                {"id": 1, "name": "Emergency Fund", "target": 10000, "current": 6500, "color": "blue"},
                {"id": 2, "name": "Vacation", "target": 3000, "current": 1200, "color": "green"},
                {"id": 3, "name": "New Car", "target": 20000, "current": 5000, "color": "purple"},
            ]
        except Exception as e:
            print(f"Error fetching savings goals: {e}")
        
        self.is_loading_goals = False