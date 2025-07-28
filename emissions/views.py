import os
from django.shortcuts import render
from .calculator import EmissionCalculator

def index(request):
    if request.method == 'POST':
        try:
            # Get and validate input
            energy_input = request.POST.get('energy', '').strip()
            
            if not energy_input:
                raise ValueError("Please enter a value")
            
            try:
                energy = float(energy_input)
            except ValueError:
                raise ValueError("Must be a valid number")
            
            if energy <= 0:
                raise ValueError("Must be greater than 0")
            
            # Calculate emissions
            calculator = EmissionCalculator()
            result = calculator.calculate_emissions(energy)
            
            if not result:
                raise ValueError("API request failed. Please try again later.")
            
            # Prepare context for results page
            context = {
                'co2e': result.get('co2e'),
                'unit': result.get('co2e_unit'),
                'energy_used': result.get('activity_data', {}).get('activity_value'),
                'source': result.get('emission_factor', {}).get('name'),
                'region': result.get('emission_factor', {}).get('region')
            }
            return render(request, 'result.html', context)
            
        except ValueError as e:
            error_message = str(e)
            return render(request, 'error.html', {'message': error_message})
        
        except Exception as e:
            # Log unexpected errors (check VS Output window)
            print(f"Unexpected error: {str(e)}")  
            return render(request, 'error.html', {
                'message': "An unexpected error occurred. Please try again."
            })
    
    # GET request - show empty form
    return render(request, 'index.html')

def result(request):
    """Fallback view if someone accesses /result directly"""
    return render(request, 'error.html', {
        'message': "Please submit the form first"
    })