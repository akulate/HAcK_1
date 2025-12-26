import pickle
from rules import rule_check

vectorizer, model = pickle.load(open("model.pkl", "rb"))

def predict(symptoms, age):
    rule = rule_check(symptoms, age)
    if rule:
        return {"label": rule[0], "reason": rule[1]}

    X = vectorizer.transform([symptoms])
    label = model.predict(X)[0]
    return {"label": label, "reason": "ML prediction"}
