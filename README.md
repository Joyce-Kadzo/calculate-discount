# Discount Calculator

A simple Python program that calculates the final price of an item after applying a discount, but only if the discount is 20% or higher.

## Features

- Calculates discounted prices for eligible items
- Maintains original price for discounts below 20%
- User-friendly input prompts
- Clear output showing whether a discount was applied

## How It Works

The program uses a function called `calculate_discount()` that takes two parameters:
- `price`: The original price of the item
- `discount_percent`: The discount percentage to be applied

The function applies the discount only if it's 20% or higher. Otherwise, it returns the original price.

## Code

```python
# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Apply discount only if it's 20% or higher
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  # Return original price if discount is less than 20%

# Main program
# Get input from the user
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price, discount_percent)

# Print the result
if discount_percent >= 20:
    print("The final price after discount is:", final_price)
else:
    print("No discount applied. The price is:", final_price)
```

## Usage

1. Run the program
2. Enter the original price when prompted
3. Enter the discount percentage when prompted
4. The program will display either:
   - The discounted price (if discount was 20% or higher)
   - The original price (if discount was less than 20%)

## Example

```
Enter the original price of the item: 100
Enter the discount percentage: 25
The final price after discount is: 75.0
```

```
Enter the original price of the item: 50
Enter the discount percentage: 15
No discount applied. The price is: 50.0
```

## Requirements

- Python 3.x

## How to Run

1. Save the code to a file (e.g., `discount_calculator.py`)
2. Open a terminal/command prompt
3. Navigate to the directory containing the file
4. Run the program with: `python discount_calculator.py`
