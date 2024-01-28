import argparse
from transformers import LlamaForCausalLM, LlamaTokenizer

def load_model_and_tokenizer(model_path, device='cpu'):
    """
    Loads a LLaMA model and tokenizer from a specified file path.

    Parameters:
        model_path (str): Path to the model file.
        device (str): The device type to load the model onto, e.g., 'cpu' or 'cuda'.

    Returns:
        model: The loaded LLaMA model.
        tokenizer: The associated tokenizer for the model.
    """
    try:
        # Load the tokenizer and model using Hugging Face's Transformers
        tokenizer = LlamaTokenizer.from_pretrained(model_path)
        model = LlamaForCausalLM.from_pretrained(model_path)

        # Move model to the specified device
        model.to(device)

        print("Model and tokenizer loaded successfully.")
        return model, tokenizer
    except FileNotFoundError:
        print("Error: The model path is not correct.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Load a LLaMA model and tokenizer.')
    parser.add_argument('model_path', type=str, help='Path to the model directory.')
    parser.add_argument('--device', type=str, default='cpu', help='Device type (cpu or cuda).')
    args = parser.parse_args()

    model, tokenizer = load_model_and_tokenizer(args.model_path, args.device)
