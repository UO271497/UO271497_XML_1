import xml.etree.ElementTree as ET


def traducirHTML(archivoXML, archivoHTML):
    try:
        tree = ET.parse(archivoXML)
    except IOError:
        print('No se encuentra el archivo ', archivoXML)
        exit()

    except ET.ParseError:
        print("Error procesando en el archivo XML = ", archivoXML)
        exit()
    file = open(archivoHTML, "w", encoding='utf-8')

    root = tree.getroot()
    # Vamos a crear un string que contenga el contenido del documento html y luego lo escribiremos al archivo
    html = "<!DOCTYPE HTML>" + "<html lang='es'>" + \
           "<head><link rel='stylesheet' type='text/css' href='estilo.css' >" + \
           "<title>Red social</title>" + \
           " <meta charset='UTF-8' > <meta name='author' content='Miguel Suárez Artime'>" + \
           " <meta name ='viewport' content ='width=device-width, initial-scale=1.0'>" + \
           "</head>" + \
           "<body>"
    html += "<h1>Red social</h1>"
    for element in root.iter():
        # recorre el arbol en profundidad, explorando primero la persona, luego los datos y finalmente sus amigos
        html += "\n"
        if (element.tag != "personas"):
            if (element.tag == "persona"):
                html += "<h2>"
                html += element.attrib.get("nombre") + " "
                html += element.attrib.get("apellidos")
                html += "</h2>"
            elif (element.tag == "fechaNacimiento"):
                html += "<h3>Nacimiento</h3><p>Fecha de nacimiento: "
                html += element.text
                html += "</p>"
            elif (element.tag == "lugarResidencia"):
                html += "<h3>Lugar Residencia</h3><p>Lugar Residencia: "
                html += element.text
                html += "</p>"
            elif (element.tag == "coordenadasNacimiento"):
                html += "<h4>Coordenadas de nacimiento</h4>"
            elif (element.tag == "coordenadasResidencia"):
                html += "<h4>Coordenadas de residencia</h4>"
            elif (element.tag == "fotografia"):
                html += "<img src='media/"
                html += element.text
                html += "' alt='Una imagen de una persona'>"
            elif (element.tag == "lugarNacimiento"):
                html += "<p>Lugar de nacimiento: " + element.text + "</p>"
            elif (element.tag == "latitud"):
                html += "<p>Latitud: " + element.text + "</p>"
            elif (element.tag == "longitud"):
                html += "<p>Longitud: " + element.text + "</p>"
            # elif (element.tag == "altitud"):
            #   html += "<p>Latitud: " + element.text + "</p>"
            elif (element.tag == "video"):
                html += "<video src='media/" + element.text + "' controls preload='auto'> Video </video>"
            elif (element.tag == "altitud"):
                html += "<p>Altitud: " + element.text + "</p>"
            elif (element.tag == "comentario"):
                html += "<p>Comentario: " + element.text + "</p>"

    # cerramos el body y escribimos en el archivo
    html += "</body>"
    file.write(html)
    print('Ejecución finalizada, archivo HTML generado con éxito')


def main():
    archivoXML = input('Introduzca un archivo XML = ')
    archivoSalida = input('Introduzca el nombre del archivo HTML=')
    # archivoXML = "arbol.xml"
    # archivoSalida = "index.html"
    traducirHTML(archivoXML, archivoSalida)


main()
