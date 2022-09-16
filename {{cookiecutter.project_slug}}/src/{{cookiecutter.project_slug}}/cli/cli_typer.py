"""A very basic Typer app."""

import typer


main = typer.Typer()


@main.command()
def hello(name: str):
    print(f"Hello {name}!")
    print("More info at: https://typer.tiangolo.com/")


@main.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    main()
