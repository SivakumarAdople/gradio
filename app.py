import gradio as gr

def add_numbers(a, b):
    return a + b

# Create a Gradio interface
iface = gr.Interface(
    fn=add_numbers,          # The function to be called
    inputs=["number", "number"],  # Inputs are two numbers
    outputs="number"          # Output is a single number
)

# Launch the app
iface.launch()
