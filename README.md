# 🎬 YouTube Downloader en Python

Este proyecto es un **descargador de videos y audios de YouTube** desarrollado en Python.  
Permite al usuario elegir si desea descargar el **video completo** o únicamente el **audio**, guardando los archivos en una carpeta llamada `DescargasYT` en el Escritorio.

---

## 🚀 Características
- Menú interactivo en consola.
- Descarga en la mejor calidad disponible.
- Opción de descargar **solo audio** en formato `.mp3`.
- Crea automáticamente la carpeta `DescargasYT` en el Escritorio del usuario.

---

## 📦 Requisitos

Antes de ejecutar el programa, asegúrate de tener instalado **Python 3.8+** y las siguientes dependencias:

```bash
pip install pytubefix
```

> ⚠️ Se utiliza **pytubefix** (un fork actualizado de `pytube`) para evitar errores con cambios en YouTube.

---

## ▶️ Uso

1. Clona este repositorio:

```bash
git clone https://github.com/tuusuario/YouTube-Downloader.git
cd YouTube-Downloader
```

2. Ejecuta el programa:

```bash
python main.py
```

3. Pega la URL del video de YouTube cuando se te solicite.  
4. Elige si quieres descargar:
   - `1` → 🎬 Video
   - `2` → 🎵 Solo audio

5. El archivo se guardará automáticamente en:

```
Escritorio/DescargasYT
```

---

## 📂 Estructura del Proyecto

```
📁 YouTube-Downloader
 ├── main.py         # Código principal
 └── README.md       # Documentación
```

---

## 💡 Ejemplo de uso

```
===== DESCARGADOR DE YOUTUBE =====
👉 Pega la URL del video: https://www.youtube.com/watch?v=abc123xyz

¿Qué deseas descargar?
1. 🎬 Video
2. 🎵 Solo audio
Selecciona (1 o 2): 1

✅ Carpeta creada en: C:/Users/TuUsuario/Desktop/DescargasYT
📥 Descargando video en la mejor calidad disponible...
✅ Video descargado correctamente.
```

---

## 📜 Licencia

Este proyecto se distribuye bajo la licencia **MIT**.  
¡Eres libre de usarlo, modificarlo y compartirlo! 🎉
