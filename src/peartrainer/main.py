"""Peartrainer - A musical ear training software written in Python."""
from controller import Controller
import click


@click.command()
@click.option("--alsa", is_flag=True, default=False)
@click.option("--jack", is_flag=True, default=False)
@click.option("--core", is_flag=True, default=False)
@click.option("--multimedia", is_flag=True, default=False)
def main(alsa, jack, core, multimedia) -> None:
    """Run Peartrainer and set up software."""
    if alsa is True:
        controller = Controller(2)
    elif jack is True:
        controller = Controller(3)
    elif core is True:
        controller = Controller(1)
    elif multimedia is True:
        controller = Controller(4)
    else:
        controller = Controller(0)

    controller.run()


if __name__ == "__main__":
    main()
