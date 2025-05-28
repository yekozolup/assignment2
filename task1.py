def select(grades : list, passgrade = 60.0 ) -> list:
    """
    Функція приймає на вхід список з дійсних чисел та повертає відфільтрований список із значень більших за введене число
    """
    result = []
    for el in grades:
        if el >= passgrade:
            result.append(el)
    return result

gradebook = {"Yevhenii": [60, 56, 89, 46, 100],
             "Sonya" : [54, 43, 100, 86],
             "Danya" : [30, 10, 3, 100, 100],
             "Ruslan" : [100, 100, 100, 100, 100]}

for key in gradebook:
    a = select(gradebook[key])
    print(f"{key}:", *a, f"Average : {sum(a)/len(a)}")