from django.apps import AppConfig

class CalculatorAppConfig(AppConfig):
    """
    Configuration class for the calculator application.
    
    Provides proper Django app configuration with:
    - Default auto field
    - App name
    - Verbose name
    - Ready handler for signals
    """
    
    # Default auto field for model primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Python path to the application
    name = 'calculator_app'
    
    # Human-readable name for admin interface
    verbose_name = "Calculator Application"
    
    def ready(self):
        """
        Override this method to perform initialization tasks when Django starts.
        Uncomment the imports and code when needed.
        """
        # Import signal handlers (uncomment when needed)
        # from . import signals
        
        # For async tasks (uncomment when needed)
        # import calculator_app.tasks
        
        # For translation (uncomment when needed)
        # from django.utils.translation import gettext_noop
        # _ = gettext_noop
        
        # Initialize calculator constants (example)
        # self.initialize_constants()
    
    # Example initialization method
    def initialize_constants(self):
        """
        Create default calculator constants if they don't exist
        """
        from .models import CalculatorConstant
        constants = [
            ('pi', 3.1415926535, "The ratio of a circle's circumference to its diameter"),
            ('e', 2.7182818284, "Euler's number"),
        ]

        for name, value, desc in constants:
            CalculatorConstant.objects.get_or_create(
                name=name,
                defaults={'value': value, 'description': desc}
            )