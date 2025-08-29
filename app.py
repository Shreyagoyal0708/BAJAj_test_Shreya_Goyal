from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get("data", [])

        # Replace with your details
        user_id = "shreya_goyal_29082002"
        email = "shreya@example.com"
        roll_number = "21BCE1234"

        odd_numbers, even_numbers, alphabets, special_characters = [], [], [], []
        sum_numbers = 0
        alpha_concat = ""

        for item in data:
            if item.isdigit():
                num = int(item)
                sum_numbers += num
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
            elif item.isalpha():
                alphabets.append(item.upper())
                alpha_concat += item
            else:
                special_characters.append(item)

        # Alternating caps in reverse order
        rev_alt_caps = ""
        toggle = True
        for char in alpha_concat[::-1]:
            rev_alt_caps += char.upper() if toggle else char.lower()
            toggle = not toggle

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(sum_numbers),
            "concat_string": rev_alt_caps
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
