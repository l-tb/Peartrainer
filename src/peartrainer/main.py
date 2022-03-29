"""Peartrainer - A musical ear training software written in Python."""
import rtmidi
import time


def generate_interval() -> tuple[int]:
    """Generate random interval."""
    return (60, 60)


def play_midi_interval(interval: tuple[int], port: rtmidi.MidiOut) -> None:
    """
    Play interval from given tuple.

    Tuple contains midi Note Values.
    """
    noteOneOn = [0x90, interval[0], 112]
    noteOneOff = [0x80, interval[0], 112]
    noteTwoOn = [0x90, interval[1], 112]
    noteTwoOff = [0x80, interval[1], 112]

    port.send_message(noteOneOn)
    time.sleep(0.5)
    port.send_message(noteTwoOn)
    time.sleep(0.7)
    port.send_message(noteOneOff)
    port.send_message(noteTwoOff)
    time.sleep(0.1)


def main() -> None:
    """Run controller for Peartrainer and set up software."""
    pass


if __name__ == '__main__':
    main()
