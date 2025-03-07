import subprocess
import sys

# Install Reflex
subprocess.check_call([sys.executable, "-m", "pip", "install", "reflex"])

# Create a new Reflex project
subprocess.check_call([sys.executable, "-m", "reflex", "init", "financial_dashboard"])

print("Reflex project created successfully!")