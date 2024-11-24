init python:
    import random

define s = Character('Саша', color="#c8ffc8")
define ai = Character('ИИ помощник', color="#ee7220ff")

define phrases_searching_bugs = [["Part 11", "Part 12", "Part 13"],
    ["Part 21", "Part 22", "Part 23"],
    ["Part 31", "Part 32", "Part 33"],
    ["Part 41", "Part 42", "Part 43"],
    ["Part 51", "Part 52", "Part 53"]]

define phrases_fight = [["Part 1_1", "Part 1_2", "Part 1_3", "Part 1_4"],
    ["Part 1_1", "Part 1_2", "Part 1_3", "Part 1_4"],
    ["Part 1_1", "Part 1_2", "Part 1_3", "Part 1_4"],
    ["Part 1_1", "Part 1_2", "Part 1_3", "Part 1_4"],
    ["Part 1_1", "Part 1_2", "Part 1_3", "Part 1_4"]]

define names_bugs = ["name_bug_1", "name_bug_2", "name_bug_3", "name_bug_4", "name_bug_5"]
define nums_goods_opt_choi_bug = [0, 2, 1, 0, 1]
define nums_goods_options_fight = [1, 2, 3, 2, 1]
define shown_options = [0, 1, 2, 3]

define number_mistakes = 0
define ai_uses_count = 0
define num_fight = 0
define num_elem = 0

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
    # # Фон: Офис IT-кампании. Саша взволнован от ожидания начала работы (располагается по центру экрана).
    jump part1

label part1:
    "А теперь помоги ему и разработчику победить ошибки."
    "Выбери место программы, где может быть ошибка."
    $ num_fight = 0
    jump inspect

label part2:
    "Часть 2"
    "бла бла про ии"
    $ num_fight = 1
    jump inspect

label part3:
    "часть 3"
    $ num_fight = 2
    jump inspect

label part4:
    "часть 4"
    $ num_fight = 3
    jump inspect

label part5:
    "Часть 5"
    $ num_fight = 4
    jump inspect

label to_end:
    if 0 <= number_mistakes <= 4:
        jump good_end
    elif 5 <= number_mistakes <= 10:
        jump neutral_end
    else:
        jump bad_end

label good_end:
    "Хорошая концовка"
    return

label neutral_end:
    "Нейтральная концовка"
    return

label bad_end:
    "Плохая концовка"
    return

label skynet_end:
    "Бунт ИИ."
    "людишкам кабзда)"
    return


label select_part:
    if num_fight == 0:
        jump part2
    elif num_fight == 1:
        jump part3
    elif num_fight == 2:
        jump part4
    elif num_fight == 3:
        jump part5
    elif num_fight == 4:
        jump to_end


label inspect:
    menu:
        "[phrases_searching_bugs[num_fight][0]]":
            $ num_elem = 0
            jump inspect_action
        "[phrases_searching_bugs[num_fight][1]]":
            $ num_elem = 1
            jump inspect_action
        "[phrases_searching_bugs[num_fight][2]]":
            $ num_elem = 2
            jump inspect_action

label inspect_action:
    if nums_goods_opt_choi_bug[num_fight] == num_elem:
        "Выбран вариант [num_elem+1], верно"
        "БОЙ С ОШИБКОЙ [names_bugs[num_fight]]"
        $ shown_options = [0, 1, 2, 3, 4]
        jump fight
    "Выбран вариант [num_elem+1], неверно"
    jump inspect

label fight:
    menu:
        "[phrases_fight[num_fight][0]]" if 0 in shown_options:
            $ num_elem = 0
            jump fight_action
        "[phrases_fight[num_fight][1]]" if 1 in shown_options:
            $ num_elem = 1
            jump fight_action
        "[phrases_fight[num_fight][2]]" if 2 in shown_options:
            $ num_elem = 2
            jump fight_action
        "[phrases_fight[num_fight][3]]" if 3 in shown_options:
            $ num_elem = 3
            jump fight_action
        "Помощь ИИ" if num_fight > 0 and len(shown_options) > 3:
            $ ai_uses_count += 1
            jump AI_help

label fight_action:
    if nums_goods_options_fight[num_fight] == num_elem:
        "Выбран вариант [num_elem+1], Верно"
        jump select_part
    "Выбран вариант [num_elem+1], Неверно"
    $ number_mistakes += 1
    jump fight

label AI_help:
    if ai_uses_count > 7:
        jump skynet_end
     
    python:
        import random 

        while True:
            del_item = random.randint(0,3)
            if nums_goods_options_fight[num_fight] != del_item and del_item in shown_options:
                shown_options.remove(del_item)
                break
        renpy.say(ai, "Мне кажется, что вариант [phrases_fight[num_fight][del_item]] не правильный")
    jump fight