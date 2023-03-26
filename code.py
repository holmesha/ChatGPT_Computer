import speech_recognition as sr
import openai

model_engine = "text-davinci-003"
openai.api_key = "YOUR OPEN AI APi HERE"

def GPT(query):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=query,
        max_tokens=1024,
        temperature=0.5,
    )
    return str.strip(response['choices'][0]['text']), response['usage']['total_tokens']

r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone(device_index=0) as source:
    # Adjust for ambient noise before recording
    r.adjust_for_ambient_noise(source)
    
    print("Say something!")
    audio = r.listen(source)

# Use Google Speech Recognition to transcribe the audio
try:
    print("Google Speech Recognition thinks you said:")
    question = r.recognize_google(audio)
    print(question)
    print("="*20)
    (res, usage) = GPT(question)
    print(res)
    print("="*20)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
except openai.error.AuthenticationError:
    print("OpenAI API authentication error.")
