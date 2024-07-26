from nepali_speech_lib.speech_recognition import recognize_speech
from nepali_speech_lib.text_to_speech import text_to_speech
from nepali_speech_lib.responses import generate_response



def main():
    recognized_text = recognize_speech()
    if recognized_text:
        response = generate_response(recognized_text)
        print(f"Responding with: {response}")
        text_to_speech(response)

if __name__ == "__main__":
    main()
