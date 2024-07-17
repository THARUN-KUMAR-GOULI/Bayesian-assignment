
import click
import ollama

@click.command()
@click.argument("input_text", nargs=-1, required=True)
def assignment(input_text):

    input_text = " ".join(input_text)
    if input_text.endswith('.txt'):
        try:
            with open(input_text, 'r') as file:
                text = file.read()
        except FileNotFoundError:
            click.echo(f"Error: File '{input_text}' not found.")
            return
    else:
        text = input_text

    try:
        response = ollama.chat(model="qwen2:0.5b", messages=[{"role": "user", "content": text}])
        
        summary = response["message"]["content"]

        click.echo(f"Summary:\n{summary}")
    except Exception as e:
        click.echo(f"An error occurred: {e}")

if __name__ == "__main__":
    assignment()
