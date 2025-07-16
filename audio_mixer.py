import ffmpeg

def merge_audio_tracks(vocal_path, music_path, output_path="final_output.wav"):
    input_vocal = ffmpeg.input(vocal_path)
    input_music = ffmpeg.input(music_path)

    ffmpeg.output(input_vocal, input_music, output_path, 
                  shortest=None, acodec='aac', ar='44100').run(overwrite_output=True)

    return output_path
