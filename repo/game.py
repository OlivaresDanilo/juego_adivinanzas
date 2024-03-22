import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número de vidas
lives = 5

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
print("Tienes 5 vidas para tratar de adivinarla")
print("")
print("Dificultad:")
print("1: Fácil")
print("2: Media")
print("3: Difícil")
dificultad = int(input("Ingrese la dificultad (1/2/3): "))
while dificultad != 1 and dificultad != 2 and dificultad != 3:
    print("Ingresaste un valor inválido!")
    dificultad = int(input("Ingrese la dificultad (1/2/3): "))

# Inicializar la palabra parcialmente adivinada según la dificultad
word_displayed = ""
if dificultad == 1:
    for letter in secret_word:
        if letter in 'aeiou':
            word_displayed += letter
        else:
            word_displayed += "_"
elif dificultad == 2:
    word_displayed = secret_word[0] + "_" * (len(secret_word) - 2) + secret_word[-1]
else:
    word_displayed = "_" * len(secret_word)

print(f"Palabra: {word_displayed}")

while lives != 0:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    
    if letter == "":
       while letter == "":
         print('ERROR, no ingresaste una letra!')
         letter = input("Vuelve a ingresar una letra: ")
    elif letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
        # Construir la nueva palabra parcialmente adivinada
        new_displayed_word = ""
        for i in range(len(secret_word)):
            if secret_word[i] == letter or word_displayed[i] != '_':
                new_displayed_word += secret_word[i]
            else:
                new_displayed_word += "_"
        word_displayed = new_displayed_word
    else:
        lives -= 1
        print("Lo siento, la letra no está en la palabra.")
        print(f'Te quedan {lives} vidas')

    print(f"Palabra: {word_displayed}")

    # Verificar si se ha adivinado la palabra completa
    if "_" not in word_displayed:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus 5 vidas.")
    print(f"La palabra secreta era: {secret_word}")
