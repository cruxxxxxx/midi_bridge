# Midi Bridge
Midi Bridge for translating messages to SP404 MK2 FX. An example of usage is to bind Resolume VFX to Audio FX.

Currently, I create the "bridge" virtual MIDI Channel using loopMIDI on Windows. 

This code can probably be expanded so it can act as a bridge/broadcaster to many channels. Managing MIDI across programs sucks, so this could help mitigate that. There may be a cleaner way to handle translation mapping as well, but some of it is kinda dynamic, so it gets tricky. 

Run:
```
pip install python-rtmidi
python midi_bridge.py
```

