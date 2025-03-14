import checkjson
import openmanager
import os

text = openmanager._open("data.json", "r")

admins = {"|0|": "zimo1", "|1|": "zimo2", "|2|": "zimo3"}

if text:  # Ensure the file isn't empty
    products = checkjson.DictDecoderProducts().decode(text)

    def admin(person: str):
        os.system("cls" if os.name == "nt" else "clear")  # Cross-platform clear screen
        print(f"\033[1;33mWelcome, {person.capitalize()}!\033[0m")
        
        decoder = checkjson.DictDecoder()  # Create a decoder instance
        
        while True:
            answ = input("\033[1;36mEnter action (add: add item, del: delete item, rts: return to shopping mode): \033[0m").strip().lower()
            
            if answ == "add":
                try:
                    jso1 = input("\033[1;34mEnter product name: \033[0m").strip()
                    jso2 = float(input("\033[1;34mEnter product price: \033[0m").strip())
                    jso3 = input("\033[1;34mEnter product kg or ea: \033[0m").strip()
                    jso4 = int(input("\033[1;34mEnter product discount: \033[0m").strip())
                    jso5 = input("\033[1;34mEnter product hex: \033[0m").strip()
                    jso6 = int(input("\033[1;34mEnter product stock: \033[0m").strip())

                    # Add new product correctly
                    products[jso1] = {
                        "name": jso1,
                        "price": jso2,
                        "koe": jso3,
                        "discount": jso4,
                        "producthex": jso5,
                        "stock": jso6,
                        "buycount": 0
                    }

                    decoder.save_products("data.json", products)
                    print("\033[1;32mItem added successfully.\033[0m")

                except ValueError:
                    print("\033[1;31mInvalid input. Please enter numeric values for price, discount, and stock.\033[0m")

            elif answ == "del":
                ind = input("\033[1;34mDeleting item: \033[0m").strip()
                if ind in products:
                    del products[ind]
                    print(f"\033[1;32mDeleted {ind}.\033[0m")
                    decoder.save_products("data.json", products)
                else:
                    print("\033[1;31mItem not found.\033[0m")

            elif answ == "rts":
                print("\033[1;35mReturning to shopping mode...\033[0m")
                os.system("cls" if os.name == "nt" else "clear")  # Cross-platform clear screen
                break  # Ensure loop exits properly
            else:
                print("\033[1;31mInvalid action, please try again.\033[0m")

    os.system("cls" if os.name == "nt" else "clear")  # Cross-platform clear screen

    print("\033[1;37mCheckoutPy: The checkout right on your computer.\033[0m")

    print("\033[1;37mHello, welcome to CheckoutPy!\033[0m")

    cart = []
    while True:
        product = input("\033[1;34mEnter product name (or press Enter to finish or type 'menu' for the shopping list): \033[1;36m").strip().lower()

        if not product:  # Exit if the user enters nothing
            print("\033[1;36mCheckout complete!\033[0m")
            break

        if product == "_slogin":
            passw = input("Admin key: ")
            admin(admins[passw])
            continue
        
        if product == "menu":
            print("\n\033[1;36m--- Shopping List ---\033[0m")
            for pname, pinfo in products.items():
                print(f"\033[1;32m{pname.capitalize()}\033[0m - ${pinfo['price']:.2f} per {pinfo['koe']} | Stock: {pinfo['stock']}")
            print("\033[1;36m--------------------\033[0m")
            continue  # Go back to asking for a product

        if product in products:
            try:
                item = products[product].copy()  # Copy to avoid modifying the original dictionary

                if item.get("koe") == "kg":
                    kg = input("\033[1;34mHow heavy is it in kg? \033[1;36m").strip()
                    item["kg"] = float(kg)  # ✅ Save correct weight in cart
                    quantity = item["kg"]
                else:
                    quantity = int(input("\033[1;34mHow many would you like? \033[1;36m").strip())
                    item["quantity"] = quantity  # ✅ Save correct quantity in cart

                # Check if enough stock is available
                if quantity > products[product]["stock"]:
                    print("\033[1;31mNot enough stock available!\033[0m")
                    continue

                item["quantity"] = quantity  # Store only "quantity"
                cart.append(item)

                # Update stock and buy count
                decoder = checkjson.DictDecoder()
                products[product]["stock"] -= quantity
                products[product]["buycount"] += quantity  # Increase purchase count
                decoder.save_products("data.json", products)

                print(f"\033[1;32mAdded {quantity}x {product} to cart.\033[0m")

            except ValueError:
                print("\033[1;31mInvalid quantity. Please enter a number.\033[0m")
            except Exception as e:
                print(f"\033[1;31mError: {e}\033[0m")

        else:
            print("\033[1;31mProduct not found. Please try again.\033[0m")

    print("\033[1;34mGenerating receipt....\033[0m")
    os.system("cls" if os.name == "nt" else "clear")  # Clear screen before showing the receipt

    inst = checkjson.DictDecoder()
    inst.generate_receipt(cart)

    input("\n\033[1;33mPress Enter to exit CheckoutPy...\033[0m")  

else:
    print("\033[1;31mError: data.json is empty or missing!\033[0m")
