"""Controller for peartrainer."""
import sys
from random import randint
import global_vars
import rtmidi
import time
import click
import os


class Controller:
    """Controller class for peartrainer."""

    def __init__(self, midiApi: int) -> None:
        """Initialize controller."""
        self.intervals = global_vars.intervals
        self.intervalNames = global_vars.intervalNames
        self.helpStr = global_vars.helpStr

        self.midiout = rtmidi.MidiOut(midiApi)

    def _generate_interval(self) -> tuple[tuple[int], str]:
        """Generate random interval."""
        firstNote = randint(48, 73)
        newInterval = randint(0, 12)
        secondNote = firstNote + newInterval
        newIntervalName = self.intervals[newInterval]
        return ((firstNote, secondNote), newIntervalName)

    def _play_midi_interval(self, interval: tuple[int]) -> None:
        """
        Play interval from given tuple.

        Tuple contains midi Note Values.
        """
        noteOneOn = [0x90, interval[0], 112]
        noteOneOff = [0x80, interval[0], 112]
        noteTwoOn = [0x90, interval[1], 112]
        noteTwoOff = [0x80, interval[1], 112]

        self.midiout.send_message(noteOneOn)
        time.sleep(0.8)
        self.midiout.send_message(noteTwoOn)
        time.sleep(0.7)
        self.midiout.send_message(noteOneOff)
        self.midiout.send_message(noteTwoOff)
        time.sleep(0.1)

    def output_test(self):
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

    def open_port(self):
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

    def run(self):
        """Run peartrainer."""
        generateNew = True
        while True:
            if generateNew is True:
                currentInterval = self._generate_interval()
                self._play_midi_interval(currentInterval[0])
                os.system("cls" if os.name == "nt" else "clear")

            generateNew = False
            try:
                answere = click.prompt(
                    "Type the correct interval"
                    " (type help for more information)"
                )
            except KeyboardInterrupt:
                sys.exit(1)
            if answere == "help":
                print(self.helpStr)
            elif answere == "quit":
                break
            elif answere == "skip":
                print(
                    "The correct interval was "
                    f"{self.intervalNames[currentInterval[1]]}"
                )
                generateNew = True
                continue
            elif answere == "replay":
                self._play_midi_interval(currentInterval[0])
            elif answere == currentInterval[1]:
                print("Correct answere")
                generateNew = True
            elif answere in self.intervals:
                print("Wrong answere\n")
            else:
                print("Invalid input\n")
