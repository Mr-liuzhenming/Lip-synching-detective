import GUI
import analyze_song
import compare
import parse_midi

def main():
    # Display GUI
    GUI.display()

    # Prompt user to select song and MIDI files
    song_file = GUI.prompt_for_file('song')
    midi_file = GUI.prompt_for_file('MIDI')

    # Analyze song and MIDI files
    song_frequencies = analyze_song.analyze(song_file)
    midi_notes = parse_midi.parse(midi_file)

    # Compare song and MIDI data to determine if lip syncing
    result = compare.compare(song_frequencies, midi_notes)

    # Display result in GUI
    GUI.display_result(result)

if __name__ == '__main__':
    main()
