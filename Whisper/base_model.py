import whisperx 

from google.colab import userdata
import gc

_model = whisperx.load_model('large-v2')

TRUTHFUL_DIR = userdata.get('TRUTHFUL_DIR')
DCEPTIVE_DIR = userdata.get('DECEPTIVE_DIR')

audio_truth = whisperx.load_model()
audio_deceptive = whisperx.load_model()

def whisperxmodel(input_file, language: str = None, task: str = "transcribe"): 
    self.model = model 
    self.file_input = file_input

    audio = whisperx.load_model(str(file_input))
    audio = whisperx.pad_or_trim(audio)
    
