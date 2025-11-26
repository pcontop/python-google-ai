import click


def summarize_text(text: str, max_len: int = 100) -> str:
    """Return a short summary (first max_len characters) of the text.

    This function is a simple example to show a small unit-testable function.
    """
    if text is None:
        return ""
    return text.strip()[:max_len]


@click.command()
@click.argument("text", required=False)
@click.option("--max-len", default=100, type=int, help="Maximum summary length")
def main(text, max_len):
    """A very small CLI used for demos.

    Usage: python -m python_google_ai.main "Some text..."
    """
    if not text:
        click.echo("No text provided. Please pass TEXT argument or pipe text in.")
        return
    result = summarize_text(text, max_len=max_len)
    click.echo(result)


if __name__ == "__main__":
    main()
