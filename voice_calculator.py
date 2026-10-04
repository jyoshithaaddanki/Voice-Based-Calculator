import speech_recognition as sr

recognizer = sr.Recognizer()

print("=" * 45)
print("       VOICE BASED CALCULATOR")
print("=" * 45)

with sr.Microphone() as source:
    print("\n🎤 Say a calculation...")
    print("Example: 25 plus 10")

    recognizer.adjust_for_ambient_noise(source, duration=1)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio).lower()

    print("\nRecognized:", text)

    text = text.replace("plus", "+")
    text = text.replace("minus", "-")
    text = text.replace("times", "*")
    text = text.replace("multiplied by", "*")
    text = text.replace("divided by", "/")

    result = eval(text)

    print("✅ Result:", result)

except sr.UnknownValueError:
    print("❌ Could not understand your voice.")

except sr.RequestError:
    print("❌ Speech recognition service is unavailable.")

except Exception:
    print("❌ Please say a valid calculation.")