import json
import pyaudio
import time

import sounddevice as sd
import torch
from vosk import Model, KaldiRecognizer

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000 # 48000
speaker = 'kseniya' # aidar, baya, kseniya, xenia, random
put_accent = True
put_yo = True
device = torch.device('cpu')


model = Model('model_small')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()


device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'model.pt'

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)
def va_speak(what: str):
    audio = model.apply_tts(text=what+"..",
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)

    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()

def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']
                print('Start listening...')
for text in listen():
    time.sleep(1)
    va_speak(text)

    print(text)

