import pyttsx3

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

def speak_feedback(feedback_messages):
    """
    Convert a list of feedback messages into speech.
    """
    for message in feedback_messages:
        tts_engine.say(message)
    tts_engine.runAndWait()

def check_posture(landmarks):
    feedback = []
    # Add granular feedback conditions (e.g., angles, positions)
    if landmarks[11].y > landmarks[12].y:  # Example condition for shoulders
        feedback.append("Your left shoulder is lower than your right. Straighten up.")

    if landmarks[23].y < landmarks[24].y:  # Example condition for hips
        feedback.append("Your left hip is higher than your right. Adjust your stance.")

    # Add more conditions as per pose requirements...

    # Call text-to-speech for feedback
    if feedback:
        speak_feedback(feedback)

    return feedback
