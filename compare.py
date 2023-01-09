def compare(song_frequencies, midi_notes):
    # Compare song frequencies and MIDI notes to determine if song is lip syncing
    for i, frequency in enumerate(song_frequencies):
        if frequency != midi_notes[i][0]:
            return 'Lip syncing'

    return 'Not lip syncing'
