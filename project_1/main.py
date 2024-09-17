"""
Permainan Bagels adalah jenis permainan deduktif di mana pemain harus menebak angka rahasia yang terdiri dari tiga digit. Setiap kali pemain membuat tebakan, permainan akan memberikan petunjuk berdasarkan seberapa dekat tebakan tersebut dengan angka rahasia:

Pico: Salah satu digit dari tebakan Anda benar, tetapi posisinya salah.
Fermi: Salah satu digit dari tebakan Anda benar dan berada di posisi yang tepat.
Bagels: Tidak ada digit dalam tebakan Anda yang benar.
Pemain harus menggunakan logika deduktif untuk menafsirkan petunjuk yang diberikan setelah setiap tebakan. Pemain diberikan maksimal 10 kesempatan untuk menebak angka rahasia.

Program Beraksi
Ketika Anda menjalankan bagels.py, outputnya akan terlihat seperti ini:

Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.
Guess #1:
> 123
Pico
Guess #2:
> 456
Bagels
Guess #3:
> 178
Pico Pico
--snip--
Guess #7:
> 791
Fermi Fermi
Guess #8:
> 701
You got it!
Do you want to play again? (yes or no)
> no
Thanks for playing!


Bagaimana aturannya?
Perlu diingat bahwa program ini tidak menggunakan nilai integer melainkan nilai string yang berisi digit numerik. Misalnya, '426'adalah nilai yang berbeda dari 426. Kita perlu melakukan ini karena kita melakukan perbandingan string dengan nomor rahasia, bukan operasi matematika. Ingat bahwa '0'dapat berupa digit awal: string '026'berbeda dari '26', tetapi integer 026sama dengan 26.

"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print("""
            Saya sedang memikirkan sebuah angka, tanpa digit yang berulang.
            Coba tebak angka apa itu? berikut petunjuknya
            ketika saya mengatakan: artinya:
            Pico = Satu digit benar tapi pada posisi yang salah
            Fermi = Satu digit benar dan pada posisi yang tepat
            Begel = tidak ada digit yang benar
          

            """)