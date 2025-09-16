# Лабораторная №1: Первичная инициализация
# Курс: Основы теории систем
# Студент: Романенко Игорь Игоревич

def get_system_info():
    # TODO: Заполните словарь вашими реальными данными
    system_info = {
        "student_name": "Романенко Игорь Игоревич",
        "academic_group": "ИВТИИбд-12",
        "github_link": "https://github.com/Igor1177"
    }
    return system_info

# Вывод информации для проверки
if __name__ == "__main__":
    info = get_system_info()
    print("Информация о системе:")
    for key, value in info.items():
        print(f"- {key}: {value}")
