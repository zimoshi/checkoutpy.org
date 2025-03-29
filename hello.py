import argparse
import shlex

class UnicodingStr(str):
    def encode(self, encoding="unicoding"):
        if encoding.lower() == "unicoding":
            return text_to_unicoding(self).encode("utf-8")
        raise ValueError(f"Unsupported encoding: {encoding}")

    def decode(self, encoding="unicoding"):
        if encoding.lower() == "unicoding":
            return unicoding_to_text(self)
        raise ValueError(f"Unsupported decoding: {encoding}")

def text_to_unicoding(text: str) -> str:
    """Encodes text to Unicoding format."""
    encoded = []
    for char in text:
        if char == " ":
            encoded.append("/")  # Space character
        else:
            binary = format(ord(char), '08b')  # Convert to 8-bit binary
            ocl = binary.replace("0", "(").replace("1", ")")
            encoded.append(ocl)
    return "|".join(encoded)  # Use '|' as separator

def unicoding_to_text(unicoding: str) -> str:
    """Decodes Unicoding format back to text."""
    decoded = []
    for part in unicoding.split("|"):
        if part == "/":
            decoded.append(" ")  # Space character
        else:
            binary = part.replace("(", "0").replace(")", "1")
            decoded.append(chr(int(binary, 2)))
    return "".join(decoded)

def interactive_mode():
    """Starts an interactive Unicoding session."""
    print("🚀 Unicoding Interactive Mode. Type 'exit' or 'quit' to leave.")
    while True:
        command = input("\nEnter 'encode <text>' or 'decode <unicoding>'\n> ").strip()
        if command.lower() in ["exit", "quit"]:
            print("Exiting Unicoding Interactive Mode. 👋")
            break

        try:
            parts = shlex.split(command)  # Better parsing for quotes & spaces
        except ValueError as e:
            print(f"⚠️ Parsing error: {e}")
            continue

        if len(parts) < 2:
            print("⚠️ Invalid command. Use 'encode <text>' or 'decode <unicoding>'.")
            continue

        mode, text = parts[0], " ".join(parts[1:])
        if mode.lower() == "encode":
            print("Encoded:", UnicodingStr(text).encode("unicoding").decode("utf-8"))
        elif mode.lower() == "decode":
            print("Decoded:", UnicodingStr(text).decode())
        else:
            print("⚠️ Invalid mode. Use 'encode' or 'decode'.")

def main():
    parser = argparse.ArgumentParser(description="Unicoding Encoder/Decoder")
    parser.add_argument("mode", choices=["encode", "decode", "interactive"], help="Choose whether to encode, decode, or enter interactive mode")
    parser.add_argument("text", nargs="?", help="Text to encode or decode (not needed in interactive mode)")

    args = parser.parse_args()

    if args.mode == "interactive":
        interactive_mode()
    elif args.text:
        if args.mode == "encode":
            result = UnicodingStr(args.text).encode("unicoding").decode("utf-8")
        else:  # decode
            result = UnicodingStr(args.text).decode()
        print(result)
    else:
        print("⚠️ Missing text input. Run `unicoding interactive` for interactive mode.")

if __name__ == "__main__":
    main()
