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



