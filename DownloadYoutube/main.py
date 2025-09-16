import os
from pytubefix import YouTube
import getpass

def crear_carpeta_descargas():
    # Obtiene el usuario actualx
    usuario = getpass.getuser()
    # Ruta al escritorio
    escritorio = os.path.join("C:/Users", usuario, "Desktop")
    # Carpeta DescargasYT
    carpeta = os.path.join(escritorio, "DescargasYT")
    
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
        print(f"✅ Carpeta creada en: {carpeta}")
    else:
        print(f"📂 Carpeta ya existe en: {carpeta}")
    return carpeta

def descargar_video(url, carpeta):
    yt = YouTube(url)
    print(f"\n🎬 Título: {yt.title}")
    print("📥 Descargando video en la mejor calidad disponible...")
    video = yt.streams.get_highest_resolution()
    video.download(output_path=carpeta)
    print("✅ Video descargado correctamente.")


def descargar_audio(url, carpeta):
    yt = YouTube(url)
    print(f"\n🎵 Título: {yt.title}")
    print("📥 Descargando solo audio...")
    audio = yt.streams.filter(only_audio=True).first()
    archivo = audio.download(output_path=carpeta)
    # Cambiamos la extensión a .mp3 (opcional, pero seguirá siendo AAC dentro)
    base, ext = os.path.splitext(archivo)
    nuevo_archivo = base + ".mp3"
    os.rename(archivo, nuevo_archivo)
    print("✅ Audio descargado correctamente.")


def menu():
    print("\n===== DESCARGADOR DE YOUTUBE =====")
    url = input("👉 Pega la URL del video: ")
    
    print("\n¿Qué deseas descargar?")
    print("1. 🎬 Video")
    print("2. 🎵 Solo audio")
    opcion = input("Selecciona (1 o 2): ")
    
    carpeta = crear_carpeta_descargas()
    
    if opcion == "1":
        descargar_video(url, carpeta)
    elif opcion == "2":
        descargar_audio(url, carpeta)
    else:
        print("❌ Opción no válida.")


if __name__ == "__main__":
    menu()
