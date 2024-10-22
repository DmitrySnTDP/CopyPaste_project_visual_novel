# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define s = Character('Саша', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    show Sasha at left

    "Это Саша"
    "Саша работает тестировщиком."
    "Работа Саши заключается в нахождении ошибок и отправки их разработчику."
    
    # Смена сцены, вид на ноутбук
    scene bg ofice
    
    "Саша получил первую программу."
    "А именно Калькулятор."
    "Его задача вроверить весь функционал программы и вызвать все имеющиеся ошибки"
    # Смена сцены (бой с делением на ноль)
    scene bg cyberspace1

    "Ты находишься перед выбором действий. Что ты будешь делать?"

    jump action_choice

label action_1:
    "You chose the first action."

    # Возвращаемся к выбору
    jump action_choice

label action_2:
    "You chose the second action."

    # Возвращаемся к выбору
    jump action_choice

label action_3:
    "You chose the third action."

    "This action ends the choice."
    return

label action_choice:
    # Показываем меню с выбором действий
    menu:
        "First action":
            jump action_1
        "Second action":
            jump action_2
        "Third action (Finish)":
            jump action_3
