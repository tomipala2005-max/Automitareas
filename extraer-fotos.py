#!/usr/bin/env python3
"""Saca las fotos que estaban incrustadas en la versión anterior del sitio
y las guarda como archivos en fotos/.

Uso (parado en esta carpeta):
    python3 extraer-fotos.py                      # las baja del sitio publicado
    python3 extraer-fotos.py ruta/index-viejo.html  # o las toma de un archivo local
"""
import base64
import pathlib
import re
import sys
import urllib.request

SITIO = "https://automitareas-vercel-tomi-e-tomi.vercel.app/"
SLOTS = ("trama", "placa", "pantalla")

if len(sys.argv) > 1:
    html = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
else:
    with urllib.request.urlopen(SITIO) as r:
        html = r.read().decode("utf-8")

destino = pathlib.Path(__file__).parent / "fotos"
destino.mkdir(exist_ok=True)

for slot in SLOTS:
    m = re.search(r"--img-" + slot + r':\s*url\("data:image/(\w+);base64,([A-Za-z0-9+/=]+)"\)', html)
    if not m:
        sys.exit(f"No encontré la foto '{slot}' incrustada. ¿Es la versión vieja del sitio?")
    archivo = destino / f"{slot}.{m.group(1)}"
    archivo.write_bytes(base64.b64decode(m.group(2)))
    print(f"ok  {archivo}  ({archivo.stat().st_size // 1024} KB)")
