"""final project"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("FinalProject")

@app.route("/emotionDetector")
def emotion_detector_route():
    """emotion detection via API"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    response = list(response.items())
    emotions = ", ".join([F"{k}: {v}" for k,v in response[:-1]])
    dominant_emotion = response[-1][1]
    if dominant_emotion is None:
        return "Invalid text! Please try again!."
    answ = "For the given statement, the system response is {em}. The dominant emotion is {dom_em}."
    return answ.format(em=emotions, dom_em=dominant_emotion)


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")


if __name__ == "__main__":

    #This functions executes the flask app and deploys it on localhost:5000

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
