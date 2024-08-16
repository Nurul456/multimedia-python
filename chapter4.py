import pygame
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play

# Inisialisasi Pygame
pygame.init()

# Mengatur tampilan
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

# Memuat dan mengubah ukuran gambar agar sesuai dengan layar
image = pygame.image.load('balon.png')
image = pygame.transform.scale(image, (200, 200))  # Mengubah ukuran gambar

# Memuat suara
sound = pygame.mixer.Sound('result.wav')

# Memutar suara
sound.play()

# Loop utama permainan dengan animasi
x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Memperbarui posisi
    x += 1
    if x > 900:
        x = 0

    # Menggambar gambar di posisi baru
    screen.fill((255, 255, 255))  # Mengubah latar belakang menjadi putih
    screen.blit(image, (x, 200))  # Menempatkan gambar di tengah-tengah layar secara vertikal

    # Memperbarui tampilan
    pygame.display.flip()

# Keluar dari Pygame setelah loop selesai
pygame.quit()

# Membuat jendela utama untuk pemutar musik
root = tk.Tk()
root.title("Music Player")

# Mendefinisikan fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        play(audio)

# Membuat tombol play
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# Menjalankan loop acara Tkinter
root.mainloop()
