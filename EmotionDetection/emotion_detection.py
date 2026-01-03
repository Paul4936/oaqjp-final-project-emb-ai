import requests  # Import the requests library to handle HTTP requests
import json


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=myobj, headers=header)

    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        # Extracting sentiment label and score from the response
        emotions = formatted_response['emotionPredictions'][0]["emotion"]
        #score = formatted_response['documentSentiment']['score']
        pass
    elif response.status_code == 500:
        emotions = None
    elif response.status_code == 400:
        emotions = {
                    "anger": None, 
                    "disgust": None, 
                    "fear": None, 
                    "joy": None, 
                    "sadness": None, 
                    "dominant_emotion": None}
        return emotions

    dominant_emotion = None
    tmp_maxVal = None
    for emotion, value in emotions.items():
        if tmp_maxVal is None or value > tmp_maxVal:
            tmp_maxVal = value
            dominant_emotion = emotion
    
    emotions["dominant_emotion"] = dominant_emotion

    # Returning a dictionary containing sentiment analysis results
    #return {'label': label, 'score': score}
    return emotions