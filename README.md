# CheckoutPy

CheckoutPy is a **local checkout system** that allows you to manage products, handle purchases, and generate receipts—all from your terminal!

## Features
✅ **Product Management** - Add, delete, and update products via admin mode.<br>
✅ **Stock Control** - Keeps track of product stock to prevent overselling.<br>
✅ **Discounts** - Automatically applies discounts to eligible products.<br>
✅ **Weight & Quantity Support** - Supports per-item (`ea`) and weight-based (`kg`) pricing.<br>
✅ **Receipt Generation** - Generates a detailed receipt with total cost and discounts applied.<br>
✅ **Admin Mode** - Special admin interface for modifying products and managing stock.<br>
✅ **Colorized CLI** - Uses ANSI color codes for a **clear and professional** interface.<br>

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/zimoshi/checkoutpy.org
   cd checkoutpy.org
   ```
2. Ensure you have **Python 3** installed.
## Usage
Run the script:
```sh
python self.py
```
### Shopping Mode
1. Enter the **name of a product** to add it to the cart.
2. If it's sold by **weight (kg)**, enter the weight when prompted.
3. If it's sold by **quantity (ea)**, enter the number of units.
4. Once finished, press **Enter** to complete checkout.
5. A **receipt** will be generated with the total cost and applied discounts.

### Admin Mode
To enter **Admin Mode**, type:
```
_slogin
```
Enter an **Admin ID**, then choose an action:
- `add` - Add a new product.
- `del` - Delete an existing product.
- `rts` - Return to shopping mode.

## Example
```
CheckoutPy: The checkout right on your computer.

Hello, welcome to CheckoutPy!
Enter product name (or press Enter to finish): eggs
How many would you like? 2
Added 2x eggs to cart.

Generating receipt....

--- Checkout Receipt ---
Eggs: $8.00 (2 ea) (Discount: -$2.00)
Total: $8.00
--- Thank you for shopping! ---
```

## Future Improvements
🔹 Save transaction history.
🔹 Implement barcode scanning support.
🔹 Support for loyalty programs and user accounts.

## Contributors
👤 Zimo Shi - [GitHub](https://github.com/zimoshi)

---

🚀 **Happy Shopping!**

