def analyze(song_file):
    # Use sound analysis library to analyze song and extract frequencies at each time point
    song_frequencies = []
    for time_point in song_file:
        song_frequencies.append(time_point.frequency)

    return song_frequencies
    
