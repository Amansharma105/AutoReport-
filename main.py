import typer

app = typer.Typer()

@app.command()
def generate():
    print("Generating report...")

@app.command()
def validate():
    print("Validating template...")

@app.command()
def list_templates():
    print("Available templates:")
    print("- sales")
    print("- hr")
    print("- inventory")

if __name__ == "__main__":
    app()
