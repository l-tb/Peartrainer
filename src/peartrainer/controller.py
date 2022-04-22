"""Controller and main menu of peartrainer."""
from interval_training import IntervalTraining
from main_menu import mainMenu, menuChoices
import inquirer
import rtmidi
import click
import time
import sys


class Controller:
    """Controller and main menu of Peartrainer."""

    midiout: rtmidi.MidiOut

    def __init__(self, midiApi: int) -> None:
        """Initialize main menu for peartrainer."""
        self.midiout = rtmidi.MidiOut(midiApi)

    def open_port(self) -> None:
        """Open midiport."""
        availablePorts = self.midiout.get_ports()

        portOptions = "Select Midiport:\n"
        for port in availablePorts:
            portOptions = portOptions + (
                f"\n({availablePorts.index(port)}) " f"{port}"
            )

        portOptions = portOptions + (
            f"\n({len(availablePorts)}) create Port\n\n> "
        )
        chosenPort = input(portOptions)

        try:
            port = int(chosenPort)
        except ValueError:
            print("\nInvalid port option.")
            sys.exit(1)

        if 0 <= port < len(availablePorts):
            self.midiout.open_port(port)
        elif port == len(availablePorts):
            self.midiout.open_virtual_port(name="Peartrainer")
            input("\nPlease connect the Port. (press Enter to continue)")
        else:
            print("\nInvalid port option.")

    def output_test(self) -> None:
        """Test midi output."""
        testing = True
        while testing:
            print("\nPlaying test...")
            self.midiout.send_message([0x90, 60, 112])
            time.sleep(0.5)
            self.midiout.send_message([0x80, 60, 112])
            time.sleep(0.1)
            confirmation = click.confirm("Did you hear a sound?", default=True)
            if confirmation is True:
                testing = False
            else:
                input(
                    "Please check your midi connections"
                    " (press enter to replay)"
                )

    def run(self) -> None:
        """Show main menu and run excercises."""
        self.open_port()
        self.output_test()
        intervaltrianing = IntervalTraining(self.midiout)
        while True:
            selection = inquirer.prompt(mainMenu)

            if selection["mainMenu"] == menuChoices[0]:
                returnvalue = intervaltrianing.run(True, False)
            elif selection["mainMenu"] == menuChoices[1]:
                returnvalue = intervaltrianing.run(False, True)
            elif selection["mainMenu"] == menuChoices[2]:
                returnvalue = intervaltrianing.run(True, True)
            elif selection["mainMenu"] == [3]:
                returnvalue = True
            if returnvalue is True:
                break
            else:
                continue
