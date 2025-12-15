import requests
import xml.etree.ElementTree as ET

# URL des XML-Feeds
url = "https://mediathekviewweb.de/feed?query=Mord%20hallo%20Deutschland"

# HTTP-Anfrage an den Feed
response = requests.get(url)
if response.status_code != 200:
    print("Fehler beim Laden des Feeds")
else:
    # Set zur Speicherung eindeutiger Links, um Duplikate zu vermeiden
    unique_links = set()

    # XML-Inhalt parsen
    root = ET.fromstring(response.content)

    # Alle Links durchsuchen, die mit p37v17.mp4 enden
    for item in root.findall(".//link"):
        link = item.text
        if link and link.endswith("p37v17.mp4"):
            unique_links.add(link)

    # Speichern der Links in einer m3u-Datei
    with open("m11ap4.m3u", "w") as file:
        for link in unique_links:
            file.write(link + "\n")

    print("Links erfolgreich in m11ap4.m3u gespeichert.")
