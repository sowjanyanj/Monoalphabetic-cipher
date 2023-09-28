from flask import Flask, render_template, request

app = Flask(__name__)

# Define the mapping for encryption and decryption
encryption_key = {
    'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't',
    'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm',
    'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f',
    'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'
}

def encrypt(plaintext):
    return ''.join(encryption_key.get(c.lower(), c) for c in plaintext)

def decrypt(ciphertext):
    decryption_key = {v: k for k, v in encryption_key.items()}
    return ''.join(decryption_key.get(c.lower(), c) for c in ciphertext)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        operation = request.form['operation']

        if operation == 'Encrypt':
            result = encrypt(text)
        elif operation == 'Decrypt':
            result = decrypt(text)
        else:
            result = "Invalid operation"

        return render_template('index.html', result=result, text=text, operation=operation)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
