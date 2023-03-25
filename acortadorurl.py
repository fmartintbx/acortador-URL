import pyshorteners
url = input("Porfavor, ingresa la URL para poder acortarla:  ")

#Servicio de TinyURL
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(url)

print("Tu URL acortada es la siguiente:  " + short_url)

