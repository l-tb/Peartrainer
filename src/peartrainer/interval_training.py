"""Class for intervaltraining."""
import sys
import rtmidi
from random import randint, choice
import global_vars
import time
import click
import os


class IntervalTraining:
    """Controller class for peartrainer."""

    intervals: list
    intervalNames: dict
    helpStr: str
    midiout: rtmidi.MidiOut

    def __init__(self, midiout) -> None:
        """Initialize controller."""
        self.intervals = global_vars.intervals
        self.intervalNames = global_vars.intervalNames
        self.helpStr = global_vars.helpStr
        self.midiout = midiout

    def _generate_interval(
        self, ascending: bool, descending: bool
    ) -> tuple[tuple[int], str]:
        """Generate random interval."""
        firstNote = randint(48, 73)
        newInterval = randint(0, 12)

        if ascending is True and descending is False:
            secondNote = firstNote + newInterval
        elif ascending is False and descending is True:
            secondNote = firstNote - newInterval
        elif ascending is True and descending is True:
            boolean = choice([True, False])
            if boolean is True:
                secondNote = firstNote + newInterval
            else:
                secondNote = firstNote - newInterval

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

    def run(self, ascending: bool, descending: bool) -> bool:
        """
        Run peartrainer.

        Returns True if peartrainer should exit emidiatly.
        The booleans determin what types of intervals will be played.
        """
        generateNew = True
        while True:
            if generateNew is True:
                currentInterval = self._generate_interval(
                    ascending, descending
                )
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
                del self.midiout
                return True
            elif answere == "leave":
                return False
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
