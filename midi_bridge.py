import time
import rtmidi
from midi_map import translate
import sys

class MidiInputHandler(object):
    def __init__(self, midi_out):
        self.midi_out = midi_out

    def __call__(self, event, data=None):
        events = translate(event)

        if debug:
            print(str(event[0]) + ' -> ' + str(events))

        for each in events:
            self.midi_out.send_message(each)


debug = False
if len(sys.argv) > 1:
    debug=True


midi_in = rtmidi.MidiIn()
available_ports = midi_in.get_ports()
print(available_ports)
bridge_port = input("Bridge Port Number: ")
midi_in.open_port(int(bridge_port))

midi_out = rtmidi.MidiOut()
available_ports = midi_out.get_ports()
print(available_ports)
sp404_port = input("SP404 Port Number: ")
midi_out.open_port(int(sp404_port))

midi_in.set_callback(MidiInputHandler(midi_out))

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('')
finally:
    print("Exit.")
    midi_in.close_port()
    midi_out.close_port()
    del midi_in
    del midi_out
