import vosk, pathlib, os, pyaudio, threading, sys

def listen(rec: vosk.KaldiRecognizer, stream: pyaudio.Stream):
    while True:
        data = stream.read(4000)
        if rec.AcceptWaveform(data):
            print(rec.Result()[14:-2])

models_path = pathlib.Path(os.path.dirname(__file__)) / "models"


model = vosk.Model( model_path= str(models_path / "Russian") )
rec = vosk.KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer= 4000)
stream.start_stream()

thread = threading.Thread(target=listen, kwargs={"rec": rec, "stream": stream}, daemon=True)
thread.start()