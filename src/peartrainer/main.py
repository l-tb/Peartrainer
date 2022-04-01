"""Peartrainer - A musical ear training software written in Python."""
import rtmidi
import click
import time
from random import randint
import sys


intervals = [
    "u",
    "2b",
    "2",
    "3b",
    "3",
    "4",
    "5b",
    "5",
    "6b",
    "6",
    "7b",
    "7",
    "8"
]

intervalNames = {
    "u": "unison",
    "2b": "minor second",
    "2": "major second",
    "3b": "minor third",
    "3": "major third",
    "4": "perfect fourth",
    "5b": "tritone",
    "5": "perfect fifth",
    "6b": "minor sixth",
    "6": "major sixth",
    "7b": "minor seventh",
    "7": "major seventh",
    "8": "octave"
}

helpStr = f"""

Interval Keys:
  {intervalNames[intervals[0]]}: {intervals[0]}
  {intervalNames[intervals[1]]}: {intervals[1]}
  {intervalNames[intervals[2]]}: {intervals[2]}
  {intervalNames[intervals[3]]}: {intervals[3]}
  {intervalNames[intervals[4]]}: {intervals[4]}
  {intervalNames[intervals[5]]}: {intervals[5]}
  {intervalNames[intervals[6]]}: {intervals[6]}
  {intervalNames[intervals[7]]}: {intervals[7]}
  {intervalNames[intervals[8]]}: {intervals[8]}
  {intervalNames[intervals[9]]}: {intervals[9]}
  {intervalNames[intervals[10]]}: {intervals[10]}
  {intervalNames[intervals[11]]}: {intervals[11]}
  {intervalNames[intervals[12]]}: {intervals[12]}

If you don't know the answere type 'skip' to reveal the interval
and get a new question.

To exit Peartrainer type 'quit'.
"""


def generate_interval() -> tuple[tuple[int], str]:
    """Generate random interval."""
    firstNote = randint(48, 73)
    newInterval = randint(0, 12)
    secondNote = firstNote + newInterval
    newIntervalName = intervals[newInterval]
    return ((firstNote, secondNote), newIntervalName)


def play_midi_interval(interval: tuple[int]) -> None:
    """
    Play interval from given tuple.

    Tuple contains midi Note Values.
    """
    pass


def main() -> None:
    """Run Peartrainer and set up software."""
    midiout = rtmidi.MidiOut(3)
    availablePorts = midiout.get_ports()

    portOptions = "Select Midiport:\n"
    for port in availablePorts:
        portOptions = portOptions + f"\n({availablePorts.index(port)}) {port}"

    portOptions = portOptions + f"\n({len(availablePorts)}) create Port\n\n> "
    chosenPort = input(portOptions)

    try:
        port = int(chosenPort)
    except ValueError:
        print("\nInvalid port option.")
        sys.exit(1)

    if 0 <= port < len(availablePorts):
        midiout.open_port(port)
    elif port == len(availablePorts):
        midiout.open_virtual_port(name="Peartrainer")
        input("\nPlease connect the Port. (press Enter to continue)")
    else:
        print("\nInvalid port option.")

    print("\nPlaying test...")
    midiout.send_message([0x90, 60, 112])
    time.sleep(0.5)
    midiout.send_message([0x80, 60, 112])
    time.sleep(0.1)
    click.confirm("Did you hear a sound?", default=True)

    generateNew = True
    while True:
        if generateNew is True:
            currentInterval = generate_interval()
            play_midi_interval(currentInterval[0])

        answere = click.prompt(
            "Type the correct interval (type help for more information)"
        )
        if answere == "help":
            print(helpStr)
        elif answere == "quit":
            break
        elif answere == "skip":
            print(
                f"The correct interval was {intervalNames[currentInterval[1]]}"
            )
            continue
        elif answere is currentInterval[1]:
            print("Correct answere")
            generateNew = True
        elif answere in intervals:
            print("Wrong answere")
            generateNew = False
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
