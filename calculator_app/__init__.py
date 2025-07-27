# calculator_app/__init__.py

"""
Package initialization for the Calculator application.

This file makes Python treat the directory as a package and can be used to:
- Define package-level variables
- Control what gets imported with 'from calculator_app import *'
- Perform package initialization
"""

# Default application configuration (important for Django apps)
default_app_config = 'calculator_app.apps.CalculatorAppConfig'

# Optional: Package version
__version__ = '1.0.0'

# Optional: Top-level imports (uncomment when needed)
# from .models import CalculationHistory  # Example model import
# from . import signals  # Example signals import

# Optional: Control what's available for 'from calculator_app import *'
# __all__ = ['CalculationHistory']  # Example for selective imports