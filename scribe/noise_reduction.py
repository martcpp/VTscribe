import warnings
# Suppress the warning from the installation of ffmpeg or avcon (whichever you used) which is nt need from thr convertion to work.
warnings.filterwarnings("ignore", message="Couldn't find ffmpeg or avconv")
from pydub import AudioSegment
# Load the audio file

def adjust_audio(audio_file):
    audio = AudioSegment.from_file(audio_file)
    # Adjust for noise (reduce noise) in db
    audio = audio -10  # You can adjust the value to control the noise reduction level
    # Export the adjusted audio to a new file
    output_file = "adjusted.wav"
    audio.export(output_file, format="wav")
    print("Noise reduction completed. Adjusted audio saved as", output_file)
    return output_file
