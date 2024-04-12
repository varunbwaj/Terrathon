import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the saved model
model_path = "torchNLP.pth"  # Update with the path to your saved model
model = AutoModelForCausalLM.from_pretrained("roberta-base")
model.load_state_dict(torch.load(model_path, map_location=torch.device('cuda')))
model.eval()  # Set the model to evaluation mode

# Initialize the tokenizer
tokenizer = AutoTokenizer.from_pretrained("roberta-base")

# Function to generate text
def generate_text(input_text, max_length=50):
    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt")

    # Generate text
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=max_length)
    print(outputs)
    # Decode the generated tokens
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text

# Example usage
input_text = "Im so lonely lately, i feel like i will never have any friends and i will end up alone"
generated_sentence = generate_text(input_text)
print("Generated sentence:", generated_sentence)
