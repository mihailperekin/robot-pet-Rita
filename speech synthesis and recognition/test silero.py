import time

import sounddevice as sd
import torch

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000 # 48000
speaker = 'petr' # aidar, baya, kseniya, xenia, random
put_accent = True
put_yo = True
device = torch.device('cpu') # cpu или gpu
text = "Привет, я робот помощник Рита и я постараюсь скрасить ваши серые будни"
text1 = "бронетранспорт+ёр"


device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'model.pt'

model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)

# воспроизводим
def va_speak(what: str):
    audio = model.apply_tts(text=what+"..",
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)

    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()

va_speak(text)
va_speak(text1)
