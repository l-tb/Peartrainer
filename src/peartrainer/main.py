"""Peartrainer - A musical ear training software written in Python."""
import rtmidi
import sys


def generate_interval() -> tuple[int]:
    """Generate random interval."""
    return (60, 60)


def play_midi_interval(interval: tuple[int]) -> None:
    """
    Play interval from given tuple.

    Tuple contains midi Note Values.
    """
    pass


def main() -> None:
    """Run controller for Peartrainer and set up software."""
    midiout = rtmidi.MidiOut()
    availablePorts = midiout.get_ports()

    portOptions = "Select Midiport:\n"
    for port in availablePorts:
        portOptions = portOptions + f"\n({availablePorts.index(port)}) {port}"

    portOptions = portOptions + f"\n({len(availablePorts)}) create Port\n\n> "
    chosenPort = input(portOptions)

    try:
        port = int(chosenPort)
    except ValueError:
        print("Invalid port option.")
        sys.exit(1)
    midiout.open_port(port)


if __name__ == "__main__":
    main()
