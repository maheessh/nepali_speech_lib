def generate_response(input_text):
    responses = {
        "नमस्ते": "नमस्ते, तपाईंलाई कस्तो छ?",
        "तपाईंको नाम के हो?": "मेरो नाम ChatGPT हो।",
        # Add more responses as needed
    }
    return responses.get(input_text, "माफ गर्नुहोस्, मलाई थाहा भएन।")
