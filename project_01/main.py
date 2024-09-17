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

NUM_DIGITS = 15
MAX_GUESSES = 15


def main():
    print("""
            Saya sedang memikirkan sebuah angka, tanpa digit yang berulang.
            Coba tebak angka apa itu? berikut petunjuknya
            ketika saya mengatakan: artinya:
            Pico = Satu digit benar tapi pada posisi yang salah
            Fermi = Satu digit benar dan pada posisi yang tepat
            Begel = tidak ada digit yang benar
          
            misalnya, jika nomor rahasia adalah 248 dan tebakan anda 843, petunjuknya adalah Fermi, Pico.
            """.format(NUM_DIGITS))

    while True:  # Main game loop
        secretNum = getSecretNum()
        print("Saya sudah menemukan sebuah nomor sebanyak {} digit.".format(NUM_DIGITS))
        print("anda harus menebak {} untuk mendapatkannya".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # terus lakukan pengulangan hingga tebakan valid yang diinput:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Tebakan #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getCluess(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("Tebakan anda habis.")
                print("Jawabannya adalah {}.".format(secretNum))

        print("Apakah kamu ingin bermain lagi? (ya atau tidak)")
        if not input('> ').lower().startswith('y'):
            break
    print("Terima kasih sudah bermain!.")


def getSecretNum():
    numbers = list("0123456789")
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getCluess(guess, secretNum):
    if guess == secretNum:
        return 'Kamu mendapatkanya, betul angkanya adalah = .'.format(secretNum)

    clues = []

    for i in range(len(guess)):
        if (guess[i] == secretNum[i]):
            clues.append('Fermi ')
        elif guess[i] in secretNum:
            clues.append('Pico ')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ''.join(clues)


if __name__ == '__main__':
    main()