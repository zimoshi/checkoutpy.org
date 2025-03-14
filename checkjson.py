import json

class DictDecoderProducts():
    def decode(self, json_str):
        try:
            # Load JSON string into a dictionary
            product_data = json.loads(json_str)
            
            # Extract products
            return product_data.get("products", {})
        except json.JSONDecodeError as e:
            print("\033[1;31mError decoding JSON:\033[0m", e)
            return {}
        
class DictDecoder():
    def decode(self, json_str):
        try:
            # Load JSON string into a dictionary
            product_data = json.loads(json_str)
            return product_data
        except json.JSONDecodeError as e:
            print("\033[1;31mError decoding JSON:\033[0m", e)
            return {}
    
    def generate_receipt(self, cart):
        total = 0
        print("\n\033[1;34m--- Checkout Receipt ---\033[0m")

        for item in cart:
            name = item.get("name")
            if not name:
                name = "\033[1;33mUnknown Item\033[0m"
            else:
                name = name.capitalize()

            price = item.get("price", 0)
            discount = item.get("discount", 0)

            # Get quantity (prefer qual, then kg for weight-based products)
            if "qual" in item:
                quantity = item["qual"]
            elif item.get("koe") == "kg":
                quantity = float(item.get("kg", 1))
            else:
                quantity = 1  # Default for "ea" products

            final_price = (price - discount) * quantity
            total += final_price

            # Display discount details if applicable
            discount_info = f" (Discount: -${discount:.2f})" if discount > 0 else ""

            print(f"\033[1;36m{name}:\033[0m \033[1;32m${final_price:.2f}\033[0m ({quantity} {item.get('koe', 'ea')}){discount_info}")

        print(f"\033[1;35mTotal: ${total:.2f}\033[0m")
        print("\033[1;34m--- Thank you for shopping! ---\033[0m\n")

        return total

    def save_products(self, path, products):
        try:
            with open(path, "w") as f:
                json.dump({"products": products}, f, indent=4)
            print("\033[1;32mProducts updated successfully!\033[0m")
        except Exception as e:
            print("\033[1;31mError saving products:\033[0m", e)