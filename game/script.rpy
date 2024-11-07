# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define s = Character('Саша', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

define number_tests = 6

define number_mistakes = 0
define ai_uses = 0

# Игра начинается здесь:
label start:

    scene bg room_sasha
    show sasha welcoming at left
    "Это Саша. Он закончил учиться и ищет работу тестировщиком."
    # Фон: комната Саши, он стоит и приветствует игрока(мб машет рукой или просто улыбается), на заднем плане виден его ноутбук. (Саша стоит слева)

    scene bg sachas_computer
    show sasha surprised at right
    "О, на его вакансию откликнулась крупная кампания и предложила протестировать их новый проект."
    "Если Саша хорошо справится с задачей, то его примут на работу."
    # Фон: крупный план на его ноутбук, на экране крупно отображается новое сообщение о отклике на его вакансию. Саша удивлён и рад. (Саша стоит справа)

    hide sasha
    scene black
    centered "На следующий день"

    scene bg ofice
    show sasha excited
    "Это первый день Саши в этой кампании."
    s "Мне так нетерпится начать и показать себя в деле!"
    "Помогите Саше найти проблемные места в программе."
    # Фон: Офис IT-кампании. Саша взволнован от ожидания начала работы (располагается по центру экрана).



    "ТЕКСТ ДЛЯ ПЕРВОЙ ОШИБКИ"
    "ОСМОТР КОДА ПЕРВОЙ ОШИБКИ"
    "А теперь помоги ему и разработчику победить ошибки."
    jump inspect1

label inspect1:
    menu:
        "1":
            jump inspect1_action1
        "2":
            jump inspect1_action2
        "3 (Верно)":
            jump inspect1_action3

label inspect1_action1:
    "Выбран 1"
    jump inspect1

label inspect1_action2:
    "Выбран 2"
    jump inspect1

label inspect1_action3:
    "Выбран 3"
    "БОЙ С ОШИБКОЙ"
    jump fight1

label fight1:
    menu:
        "1":
            $ number_mistakes += 1
            jump fight1_action1
        "2":
            $ number_mistakes += 1
            jump fight1_action2
        "3":
            $ number_mistakes += 1
            jump fight1_action3
        "4 (Верно)":
            $ number_mistakes += 1
            jump fight1_action4

label fight1_action1:
    "Выбран 1"
    jump fight1

label fight1_action2:
    "Выбран 2"
    jump fight1

label fight1_action3:
    "Выбран 3"
    jump fight1

label fight1_action4:
    "Выбран 4"
    "ОБРАЩЕНИЕ К РАЗРАБОТЧИКУ"
    jump inspect2



label inspect2:
    menu:
        "1 (Верно)":
            jump inspect2_action1
        "2":
            jump inspect2_action2
        "3":
            jump inspect2_action3

label inspect2_action1:
    "Выбран 1"
    "БОЙ С ОШИБКОЙ"
    jump fight2

label inspect2_action2:
    "Выбран 2"
    jump inspect2

label inspect2_action3:
    "Выбран 3"
    jump inspect2


label fight2:
    menu:
        "1":
            $ number_mistakes += 1
            jump fight2_action1
        "2":
            $ number_mistakes += 1
            jump fight2_action2
        "3 (Верно)":
            jump fight2_action3
        "4":
            $ number_mistakes += 1
            jump fight2_action4
        "Помощь ИИ":
            $ ai_uses += 1
            jump fight2_action_ai

label fight2_ai:
    menu:
        "2":
            $ number_mistakes += 1
            jump fight2_action2
        "3 (Верно)":
            jump fight2_action3
        "4":
            $ number_mistakes += 1
            jump fight2_action4

label fight2_action1:
    "Выбран 1"
    jump fight2

label fight2_action2:
    "Выбран 2"
    jump fight2

label fight2_action3:
    "Выбран 3"
    "ОБРАЩЕНИЕ К РАЗРАБОТЧИКУ"
    jump inspect3

label fight2_action4:
    "Выбран 4"
    jump fight2

label fight2_action_ai:
    "Выбрана помощь ИИ"
    jump fight2_ai



label inspect3:
    menu:
        "1":
            jump inspect3_action1
        "2":
            jump inspect3_action2
        "3 (Верно)":
            jump inspect3_action3

label inspect3_action1:
    "Выбран 1"
    jump inspect3

label inspect3_action2:
    "Выбран 2"
    jump inspect3

label inspect3_action3:
    "Выбран 3"
    "БОЙ С ОШИБКОЙ"
    jump fight3

label fight3:
    menu:
        "1 (Верно)":
            jump fight3_action1
        "2":
            $ number_mistakes += 1
            jump fight3_action2
        "3":
            $ number_mistakes += 1
            jump fight3_action3
        "4":
            $ number_mistakes += 1
            jump fight3_action4
        "Помощь ИИ":
            $ ai_uses += 1
            jump fight3_action_ai

label fight3_ai:
    menu:
        "1 (Верно)":
            $ number_mistakes += 1
            jump fight3_action1
        "3":
            jump fight3_action3
        "4":
            $ number_mistakes += 1
            jump fight3_action4

label fight3_action1:
    "Выбран 1"
    "ОБРАЩЕНИЕ К РАЗРАБОТЧИКУ"
    return

label fight3_action2:
    "Выбран 2"
    jump fight3

label fight3_action3:
    "Выбран 3"
    jump fight3

label fight3_action4:
    "Выбран 4"
    jump fight3

label fight3_action_ai:
    "Выбрана помощь ИИ"
    jump fight3_ai