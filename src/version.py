import typer

app = typer.Typer()


@app.command()
def version():
    print('Tapasya 0.0.1')
