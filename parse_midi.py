def parse(midi_file):
    # Use MIDI parsing library to parse MIDI file and extract notes
    midi_notes = []
    for note in midi_file:
        midi_notes.append((note.frequency, note.start_time, note.end_time))

    return midi_notes
