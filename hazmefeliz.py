import requests
from constantes import API_KEY
from PIL import Image

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence

def storeText(key, text, label):
  #checkApiKey(key)
    
  url = ("https://machinelearningforkids.co.uk/api/scratch/" + 
         key + 
         "/train")

  response = requests.post(url, 
                           json={ "data" : text, "label" : label })

  if response.ok == False:
    # if something went wrong, display the error
    print (response.json())


def ingresarNuevoEjemplo(text):
    
    respuestaUsuario = input("¿Quiere añadir la palabra al modelo de entrenamiento? (S/N)")
    respuestaUsuario = respuestaUsuario.lower()

    if respuestaUsuario == 's':
        print()
        print("Vamos a añadir un nuevo texto, el texto va a ser: ", text)

        etiqueta = input("¿Dónde quieres añadir el ejemplo? (cosas_buenas o cosas_malas)")
        etiqueta = etiqueta.lower()

        if etiqueta == 'cosas_buenas':
            print()
            print("Vamos a añadir", text, "ha la etiqueta", etiqueta)
        
        elif etiqueta == 'cosas_malas':
            print()
            print("Vamos a añadir", text, "ha la etiqueta", etiqueta)

        else:
            print("La respuesta tiene que ser cosas_buenas o cosas_malas, una de las dos opciones")



    elif respuestaUsuario == 'n':
        print("Has respondido NO")
    
    else:
        print("Tienes que responder con S para Si o con N para No")



def classify(text):
    key = API_KEY
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"
    
    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        confidence = responseData[0]

        print(responseData)
        print()
        
        if confidence['confidence'] >= 60:
            topMatch = responseData[0]
            return topMatch

        else:
            print("No entiendo la respuesta")
            ingresarNuevoEjemplo(text)

    else:
        response.raise_for_status()

def respuesta(recognized):

    label = recognized['class_name']

    if label == "cosas_buenas":
        print("Muchas gracias, eres muy agradable")
        img = Image.open('feliz.png')
        #print(img) #<PIL.PngImagePlugin.PngImageFile image mode=RGB size=640x438 at 0x7F0D12A351F0>
        debug=img.show()
        print(debug)

    else:
        print("No me ha gustado lo que has dicho")
        img = Image.open('triste.png')
        #print(img)
        debug=img.show()
        print(debug)



# Cambiamos a partir de aquí la forma de usar el módelo de entrenamiento. 
#demo = classify("Eres bonito")

#label = demo["class_name"]
#confidence = demo["confidence"]

# CHANGE THIS to do something different with the result
#print ("result: '%s' with %d%% confidence" % (label, confidence))

def run():
    texto = input('¿Que quieres decirme? ')

    recognized = classify(texto)


if __name__ == '__main__':
    run()

   