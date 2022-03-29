"""Peartrainer - A musical ear training software written in Python."""
import rtmidi


def generate_interval() -> tuple[int]:
    """Generate random interval."""
    return (60, 60)


def play_midi_interval(interval: tuple[int], port: rtmidi.MidiIn) -> None:
    """
    Play interval from given tuple.

    Tuple contains midi Note Values.
    """
    noteOneOn = [0x90, interval[0], 112]
    noteOneOff = [0x80, interval[0], 112]
    noteTwoOn = [0x90, interval[1], 112]
    noteTwoOff = [0x80, interval[1], 112]


def main() -> None:
    """Run controller for Peartrainer and set up software."""
    pass


if __name__ == '__main__':
    main()
