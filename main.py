import whisper

model = whisper.load_model("base")
result = model.transcribe("Skazki_-_Kolobok_(musmore.com).mp3")
print(result["text"])