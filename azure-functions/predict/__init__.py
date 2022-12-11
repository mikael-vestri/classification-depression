import logging
import azure.functions as func
import joblib
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    print('hello')
    input_text = req.params.get("I'm very sad")

    # loading the model to test
    loaded_model = joblib.load('ml_model')
    vectorizer = joblib.load('ml_model_vec')

    X = vectorizer.transform([input_text])

    y = loaded_model.predict(X)
    print(y[0])

    return func.HttpResponse(f"The inference for the text {input_text} was {y[0]}", status_code=200)


