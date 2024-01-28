from flask import Flask, request, jsonify
from transformers import LlamaForCausalLM, LlamaTokenizer

app = Flask(__name__)

# Load the model and tokenizer
model_path = './models'  # Adjust the path as necessary
model = LlamaForCausalLM.from_pretrained(model_path)
tokenizer = LlamaTokenizer.from_pretrained(model_path)


def process_input(input_text):
    """
    Processes the input text and returns the model's response.

    Parameters:
        input_text (str): The input text to be processed.

    Returns:
        str: The model's response
    """
    try:
        # Tokenize the input text
        inputs = tokenizer.encode(input_text, return_tensors="pt")

        # Generate a response
        output = model.generate(inputs, max_length=50000)  # Adjust max_length as needed
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        return response
    except Exception as e:
        return f"Error processing input: {e}"


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        if not data or 'text' not in data:
            return jsonify({'error': 'No text provided'}), 400

        input_text = data['text']
        response = process_input(input_text)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': f'An error occurred: {e}'}), 500


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
