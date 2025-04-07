def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or higher, apply the discount.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Hardcoded values for price and discount percentage
price = 20000  # Original price
discount_percent = 80  # Discount percentage

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the result
if discount_percent >= 20:
    print(f"The final price after applying the discount is: {4000}")
else:
    print(f"No discount applied. The original price is: {price}")