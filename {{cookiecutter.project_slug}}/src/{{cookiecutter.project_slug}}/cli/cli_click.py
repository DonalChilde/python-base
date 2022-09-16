"""A very basic click app."""

import click


@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def main(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello {name}!")
        click.echo("More info at: https://click.palletsprojects.com/en/8.1.x/")


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
