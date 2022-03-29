"""Test Midi Output of Peartrainer."""
import pytest
import rtmidi
import threading
import time
from peartrainer import main as pt


@pytest.fixture
def midiout():
    out = rtmidi.MidiOut()
    return out


@pytest.fixture
def midiin():
    midiinput = rtmidi.MidiIn()
    return midiinput


def collect_midi(midiin: rtmidi.MidiIn, messages: list):
    for i in range(20):
        current_message = midiin.get_message()
        messages.append(current_message)
        time.sleep(0.1)


def test_system_midi(midiout, midiin):
    midiin.open_virtual_port()
    midiout.open_port(1)
    messages = []
    midiCollector = threading.Thread(
        target=collect_midi, args=(midiin, messages)
    )
    midiCollector.start()
    pt.play_midi_interval((60, 64), midiout)

    midiCollector.join()
    cleanMidi = []
    for message in messages:
        if message is None:
            continue
        else:
            cleanMidi.append(message[0])

    assert cleanMidi == [
        [144, 60, 112],
        [144, 68, 112],
        [128, 60, 112],
        [128, 68, 112],
    ]
