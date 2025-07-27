from django.test import TestCase, Client
from django.urls import reverse
import json

class CalculatorViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.calculator_url = reverse('calculator')
        self.calculate_url = reverse('calculate')

    def test_calculator_view_GET(self):
        """Test that the calculator page renders properly"""
        response = self.client.get(self.calculator_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'calculator_app/calculator.html')
        self.assertContains(response, 'Modern Django Calculator')

    def test_calculate_endpoint_valid_expression(self):
        """Test the calculate endpoint with valid expressions"""
        test_cases = [
            ('2+2', 4),
            ('10-5', 5),
            ('3*4', 12),
            ('20/5', 4),
            ('(5+3)*2', 16),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                response = self.client.post(
                    self.calculate_url,
                    data={'expression': expression},
                    HTTP_X_REQUESTED_WITH='XMLHttpRequest'
                )
                
                self.assertEqual(response.status_code, 200)
                data = json.loads(response.content)
                self.assertEqual(data['result'], expected)

    def test_calculate_endpoint_invalid_expression(self):
        """Test the calculate endpoint with invalid expressions"""
        invalid_expressions = [
            '2++2',
            '10/0',
            'abc',
            '5+',
            '()',
        ]

        for expression in invalid_expressions:
            with self.subTest(expression=expression):
                response = self.client.post(
                    self.calculate_url,
                    data={'expression': expression},
                    HTTP_X_REQUESTED_WITH='XMLHttpRequest'
                )
                
                self.assertEqual(response.status_code, 400)
                data = json.loads(response.content)
                self.assertIn('error', data)

    def test_non_ajax_request(self):
        """Test that non-AJAX requests are rejected"""
        response = self.client.post(
            self.calculate_url,
            data={'expression': '2+2'}
        )
        self.assertEqual(response.status_code, 400)

    def test_empty_expression(self):
        """Test handling of empty expressions"""
        response = self.client.post(
            self.calculate_url,
            data={'expression': ''},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 400)


class CalculatorUITests(TestCase):
    def test_calculator_ui_elements(self):
        """Test that all calculator buttons are present"""
        response = self.client.get(reverse('calculator'))
        
        buttons = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '+', '-', '*', '/', '=', 'C', 'DEL', '(', ')', '.'
        ]
        
        for button in buttons:
            with self.subTest(button=button):
                self.assertContains(response, f'value="{button}"')