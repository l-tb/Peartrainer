"""Peartrainer - A musical ear training software written in Python."""
import rtmidi


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


if __name__ == '__main__':
    main()
