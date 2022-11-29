"""#  Reto #5
#  ASPECT RATIO DE UNA IMAGEN
#  Fecha publicación enunciados: 01/02/22
#  Fecha publicación resolución: 07/02/22
#  Dificultad: DIFÍCIL
#
#  Enunciado: Crea un programa que se encargue de calcular y el aspect ratio de una imagen a partir de una url.
#  - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
#  - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1921080px."""

import cv2
import requests
from fractions import Fraction

url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
IMAGE_NAME = "image.png"

def download_image(url_image: str):
    response = requests.get(url_image)

    with open(IMAGE_NAME, "wb") as file:
        file.write(response.content)

def ratio_image(url_image: str):
    download_image(url_image)

    if cv2.
