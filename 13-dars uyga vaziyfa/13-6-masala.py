starting_amplitude = float(input("Boshlang'ish amplitudani kiriting: "))
stop_amplitude = float(input("To'xtash amplitudasini kiriting: "))
summ = 0
while starting_amplitude >= stop_amplitude:
  summ += 1
  starting_amplitude *= 0.916  # har safar mayatnikning tebranish amplitudasi 8.4 % ga pasayadi
print("Mayatnik", summ, "ta tebranishdan keyin to'xtagan deb hisoblanadi")