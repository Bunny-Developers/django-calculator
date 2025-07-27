from django.db import models
from django.contrib.auth.models import User

class CalculationHistory(models.Model):
    """
    Model to store calculation history for users (optional feature).
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    expression = models.CharField(max_length=255)
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Calculation History'
        verbose_name_plural = 'Calculation Histories'
    
    def __str__(self):
        return f"{self.expression} = {self.result}"