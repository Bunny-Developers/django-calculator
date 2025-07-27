from django.shortcuts import render
from django.http import JsonResponse
import re
import operator
import ast

def calculator_view(request):
    return render(request, 'calculator_app/calculator.html')

def calculate(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        expression = request.POST.get('expression', '')
        try:
            # Validate and evaluate the expression safely
            result = safe_eval(expression)
            return JsonResponse({'result': result})
        except (ValueError, SyntaxError, TypeError, ZeroDivisionError) as e:
            return JsonResponse({'error': 'Invalid expression'}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Calculation error'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def safe_eval(expression):
    """
    Safely evaluate mathematical expressions without using eval().
    Only allows basic arithmetic operations: +, -, *, /, (, ), and numbers.
    """
    # Remove whitespace
    expression = expression.replace(' ', '')
    
    # Validate that expression only contains allowed characters
    if not re.match(r'^[0-9+\-*/().]+$', expression):
        raise ValueError("Invalid characters in expression")
    
    # Check for empty expression
    if not expression:
        raise ValueError("Empty expression")
    
    # Parse and evaluate using AST (Abstract Syntax Tree)
    try:
        node = ast.parse(expression, mode='eval')
        return _eval_node(node.body)
    except SyntaxError:
        raise ValueError("Invalid syntax")

def _eval_node(node):
    """
    Recursively evaluate AST nodes for safe mathematical operations.
    """
    if isinstance(node, ast.Constant):  # Numbers
        return node.value
    elif isinstance(node, ast.Num):  # Numbers (older Python versions)
        return node.n
    elif isinstance(node, ast.BinOp):  # Binary operations
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        
        if isinstance(node.op, ast.Add):
            return left + right
        elif isinstance(node.op, ast.Sub):
            return left - right
        elif isinstance(node.op, ast.Mult):
            return left * right
        elif isinstance(node.op, ast.Div):
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            return left / right
        else:
            raise ValueError("Unsupported operation")
    elif isinstance(node, ast.UnaryOp):  # Unary operations (like negative numbers)
        operand = _eval_node(node.operand)
        if isinstance(node.op, ast.UAdd):
            return +operand
        elif isinstance(node.op, ast.USub):
            return -operand
        else:
            raise ValueError("Unsupported unary operation")
    else:
        raise ValueError("Unsupported expression type")