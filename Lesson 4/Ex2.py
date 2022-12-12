# Создать словарь цветов, в котором ключ - название или кодировка цвета; значение - кортеж из rgb этого цвета

colors = {"red": (255, 0, 0), "army green": (75, 83, 32)}
colors.update({"orange": (255, 165, 0)})
colors["sapphire"] = (8, 37, 103)
print("The final dictionary is:", colors)
