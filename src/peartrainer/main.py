"""Peartrainer - A musical ear training software written in Python."""
import rtmidi
import click
import time
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
    """Run Peartrainer and set up software."""
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


if __name__ == "__main__":
    main()
