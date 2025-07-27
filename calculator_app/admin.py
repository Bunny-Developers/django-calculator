from django.contrib import admin
from .models import CalculationHistory, CalculatorConstant

@admin.register(CalculationHistory)
class CalculationHistoryAdmin(admin.ModelAdmin):
    list_display = ('expression', 'result', 'created_at', 'user')
    search_fields = ('expression', 'result')
    list_filter = ('created_at',)

@admin.register(CalculatorConstant)
class CalculatorConstantAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'scientific_value')
    search_fields = ('name', 'description')