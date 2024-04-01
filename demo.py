# Check
import datetime
import whisper


model = whisper.load_model('base.en')
option = whisper.DecodingOptions(language='en', fp16=False)
result = model.transcribe('video\prakash_raj.mp4')

print(result['text'])
