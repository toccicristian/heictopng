from PIL import Image
import pillow_heif
import sys
import os
from os.path import normpath, expanduser, isfile, isdir



if len(sys.argv) < 2:
    print("Faltan argumentos.\n")
    sys.exit()

if len(sys.argv) == 2 and len([x for x in ['-h','--help','--ayuda'] if x == sys.argv[1]]) > 0:
    printf("convierte archivos heic a png.")
    sys.exit()

if not isfile(normpath(expanduser(sys.argv[1]))):
    print(f"El archivo {normpath(expanduser(sys.argv[1]))} no existe.\n")

destino = "salida.png"
if len(sys.argv) > 2 and isdir(os.path.split(normpath(expanduser(sys.argv[2])))[0]):
    destino = normpath(expanduser(sys.argv[2]))

ar_heif = pillow_heif.read_heif(normpath(expanduser(sys.argv[1])))
image = Image.frombytes(
    ar_heif.mode,
    ar_heif.size,
    ar_heif.data.tobytes(),
    "raw",
)

image.save(normpath(expanduser(destino)), format("png"))



#changed heif_file.data to heif_file.data.tobytes()
