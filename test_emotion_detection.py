from EmotionDetection.emotion_detection import emotion_detector
import unittest

"""
"I am glad this happened"	"joy"
"I am really mad about this"	"anger"
"I feel disgusted just hearing about this"	"disgust'
"I am so sad about this"	"sadness"
"I am really afraid that this will happen"	"fear"
"""

class TestEmotionDetection(unittest.TestCase):
    def test_dominant_emotion(self):
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotion"], "joy")
        self.assertEqual(emotion_detector("I am really mad about this")["dominant_emotion"], "anger")
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"], "disgust")
        self.assertEqual(emotion_detector("I am so sad about this")["dominant_emotion"], "sadness")
        self.assertEqual(emotion_detector("I am really afraid that this will happen")["dominant_emotion"], "fear")

unittest.main()
