"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Python Base."""


if __name__ == "__main__":
    main(prog_name="python-base")  # pragma: no cover