# AutoMiTareas

Sitio de una sola página. No necesita build ni dependencias: es un `index.html`
con el CSS y el JS adentro, más unos pocos archivos estáticos.

```
index.html             la página
favicon.svg            ícono de la pestaña
apple-touch-icon.png   ícono al guardar el sitio en el celular
og.png                 imagen de la vista previa al compartir el link
fotos/                 fotos de fondo (trama, placa, pantalla)
vercel.json            cabeceras y caché
extraer-fotos.py       trae las fotos de la versión anterior del sitio
```

## Primera vez: traer las fotos

Las fotos antes estaban incrustadas dentro del `index.html`. Ahora van como
archivos aparte en `fotos/` (la página carga más rápido y se guardan en caché).
Para traerlas de la versión publicada, parado en esta carpeta:

    python3 extraer-fotos.py

Si preferís sacarlas de tu `index.html` viejo:

    python3 extraer-fotos.py ruta/al/index-viejo.html

Sin las fotos la página funciona igual, solo se ven los fondos lisos.

## Subirlo a Vercel

**Opción A, conectando el repo.** En vercel.com, en el proyecto, *Settings → Git*
y conectá este repositorio. Cada push a la rama principal se publica solo.
Framework: "Other". Sin comando de build.

**Opción B, por consola.** Con Node instalado, parado en esta carpeta:

    npx vercel          # publica una vista previa
    npx vercel --prod   # publica en la URL definitiva

## Cambiar las imágenes

Reemplazá el archivo en `fotos/` manteniendo el nombre, o cambiá la ruta en el
bloque `<style id="fotos">` de arriba de todo del `index.html`.

## Si cambia la dirección del sitio

Si pasás a un dominio propio, actualizá la URL en `index.html` (etiquetas
`canonical`, `og:url`, `og:image` y el bloque `ld+json`) y en `extraer-fotos.py`.
