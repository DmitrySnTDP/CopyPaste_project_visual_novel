init python:
    import random

    def get_random_elem_in_array(array):
        random_elem = array[random.randint(0, len(array)-1)]
        return random_elem

define s = Character("Саша",color="#f85454")
define r = Character("Рома",color="#78ea3b")
define ai = Character('ИИ помощник', color="#ee7220ff")
define b = Character("Начальник",color="#86dbfc")

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

define phrases_developer_call = ["Нам нужны только радикальные меры для победы над ней!",
    "Давай победим её как можно скорее!",
    "Нужно быть предельно осторожными, чтобы не разможить ему подобных",
    "За дело!"]

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

    jump part1

label part1:
    hide sasha
    scene black with fade
    centered "На следующий день"
    
    scene bg office with fade
    show sasha excited
    "Это первый день Саши в этой кампании."
    # Фон: Офис IT-кампании. Саша взволнован от ожидания начала работы (располагается по центру экрана).

    
    scene bg in_office with fade
    show sasha excited
    s "Мне так нетерпится приступить к работе и показать себя в деле!"
    "Помогите Саше найти проблемные места в программе."

    $ num_fight = 0
    jump inspect

label part2:
    show roma normal:
        xalign 0.25
        yalign 1.0
    r "Это было классно!"
    s "Согласен! Спасибо тебе за помощь."
    r "Обращайся!"
    hide roma
    s "Надо передохнуть и после продолжим искать баги."
    scene black with fade
    centered "Спустя 30 минут"
    scene bg in_office with fade
    show sasha normal
    show boss normal:
        xalign 0.25
        yalign 1.0
    b "У меня есть хорошая новость для тебя."
    s "Какая?"
    b "Одна из наших команд закончила разработку ИИ помощника для тестирования программ."
    b "Ты можешь им пользоваться, но будь осторожней, он ещё не до конца проверен."
    s "Спасибо, сейчас же пойду и опробую его!"

    "Теперь у тебя появилась кнопка \"Помошь ИИ\" в битве с багом, она убирает один из неправильных вариантов за раз."
    "Но не злоупотребляй ей, нейросеть ещё сырая!"
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
    scene bg program_testing
    show sasha normal at right

    menu:
        s "Давай выберем место программы, где может быть ошибка."

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
        "Выбран вариант [num_elem+1], верно."
        if num_fight == 0:
            menu:
                "Теперь напиши разрабочику, что нашёл первую ошибку."
                "Написать":
                    "{color=#f85454}[s]{/color}\n Привет, я нашёл ошибку. Поможешь мне справиться с ней?"
                    "{color=#f85454}[s]{/color}\n Привет, я нашёл ошибку. Поможешь мне справиться с ней?\n{color=#78ea3b}[r]{/color}\n Привет, конечно, скоро приду и победим её!"

        scene black with fade
        centered "Бой с ошибкой [names_bugs[num_fight]]."
        scene bg fight with dissolve
        show roma normal:
            xalign 0.1
            yalign 0.5
        show sasha normal at left
        image monster = "monsters/monster[num_fight].png"
        show monster at right

        r "[get_random_elem_in_array(phrases_developer_call)]"
        $ shown_options = [0, 1, 2, 3, 4]
        jump fight
    "Выбран вариант [num_elem+1], неверно."
    $ number_mistakes += 1
    jump inspect

label fight:
    menu:
        s "Давай выберем вариант, который исправит ошбику."
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
        pause(0.2)
        hide monster
        "Выбран вариант [num_elem+1], Верно."
        scene bg in_office with fade
        show sasha normal
        jump select_part
    "Выбран вариант [num_elem+1], Неверно."
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
        renpy.say(ai, "Мне кажется, что вариант [phrases_fight[num_fight][del_item]] не правильный.")
    jump fight