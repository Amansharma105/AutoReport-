import typer

app = typer.Typer()

@app.command()
def hello():
    print("AutoReport CLI is working!")

if __name__ == "__main__":
    app()
