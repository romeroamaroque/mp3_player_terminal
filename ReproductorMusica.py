import pygame
import os

def listar_canciones(carpeta):
    canciones = []
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".mp3"):
            canciones.append(archivo)
    return canciones

def reproducir_musica(carpeta, cancion):
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(carpeta, cancion))
    pygame.mixer.music.play()

def pausar_musica():
    pygame.mixer.music.pause()

def continuar_musica():
    pygame.mixer.music.unpause()

def detener_musica():
    pygame.mixer.music.stop()

def main():
    carpeta = ""  # Inicializamos la variable carpeta fuera del bucle para que sea accesible en todo el programa
    while True:
        
        
        
        print("1. Seleccionar carpeta de música")
        print("2. Reproducir música")
        print("3. Pausar música")
        print("4. Continuar música")
        print("5. Detener música")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            carpeta = input("Introduzca la ruta de la carpeta de música: ")
            if os.path.exists(carpeta):
                print("Canciones disponibles:")
                canciones = listar_canciones(carpeta)
                for i, cancion in enumerate(canciones):
                    print(f"{i+1}. {cancion}")
            else:
                print("La carpeta no existe.")
        elif opcion == "2":
            if carpeta == "":
                print("Primero seleccione una carpeta de música.")
            else:
                cancion_index = int(input("Seleccione el número de la canción que desea reproducir: ")) - 1
                cancion_seleccionada = listar_canciones(carpeta)[cancion_index]
                reproducir_musica(carpeta, cancion_seleccionada)
        elif opcion == "3":
            pausar_musica()
        elif opcion == "4":
            continuar_musica()
        elif opcion == "5":
            detener_musica()
        elif opcion == "6":
            print("Saliendo del reproductor de música.")
            detener_musica()
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
