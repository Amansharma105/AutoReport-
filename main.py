import typer

app = typer.Typer()

@app.command()
def hello():
    print("AutoReport CLI is working!")

@app.command()
def validate():
    print("Data validation module ready")

if __name__ == "__main__":
    app()
