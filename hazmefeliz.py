import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "0c936cc0-8385-11ec-b027-c76f2f304ab930aa22f0-d0c1-40f9-bfde-b876d48cefae"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to something you want your machine learning model to classify
demo = classify("The text that you want to test")

label = demo["class_name"]
confidence = demo["confidence"]


# CHANGE THIS to do something different with the result
print ("result: '%s' with %d%% confidence" % (label, confidence))