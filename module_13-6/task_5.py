def count_oscillations(initial_amplitude, stop_amplitude):
    oscillations = 0
    current_amplitude = initial_amplitude

    while current_amplitude > stop_amplitude:
        current_amplitude *= 0.916
        oscillations += 1

    return oscillations


initial_amplitude = float(input("Введите начальную амплитуду: "))
stop_amplitude = float(input("Введите амплитуду остановки: "))

if initial_amplitude > 0 and stop_amplitude > 0 and initial_amplitude > stop_amplitude:
    result = count_oscillations(initial_amplitude, stop_amplitude)
    print(f"Маятник считается остановившимся через {result} колебаний")
else:
    print("Ошибка: введите корректные значения амплитуд!")
