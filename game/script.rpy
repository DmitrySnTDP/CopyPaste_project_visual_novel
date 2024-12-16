init python:
    import random

    def get_random_elem_in_array(array):
        random_elem = array[random.randint(0, len(array)-1)]
        return random_elem

define s = Character("Саша",color="#f85454")
define r = Character("Рома",color="#78ea3b")
define ai = Character('ИИ помощник', color="#ee7220ff")
define b = Character("Начальник",color="#86dbfc")

define phrases_searching_bugs = [[
        "Случай некорректного рейтинга не обработан в функции calculate_bonus()",
        "функция возвращает None для некорректного рейтинга.",
        "Проблема с выводом результата, использован неправильный формат строки."],

    ["Некорректное преобразование типов в одной из записей.",
        "отсутствует проверка на существование ключа amount в записи.",
        "Значение amount в одном из записей представлено строкой вместо числа. "],

    ["Некорректное распределение задач между сотрудниками.",
        "Список сотрудников пуст, из-за чего происходит деление на ноль. ",
        "Ошибка в выводе результата: список задач не соответствует сотрудникам."],

    ["Part 41",
        "Part 42",
        "Part 43"],

    ["Part 51",
        "Part 52",
        "Part 53"]]

define phrases_fight = [[
        "Исключить сотрудников с некорректным рейтингом из списка employee_data.",
        "Добавить условие else, возвращающее бонус 0 для некорректных рейтингов.",
        "Переписать функцию для обработки всех возможных значений рейтингов.",
        "Вернуть значение None вместо бонуса для некорректного рейтинга."],

    ["Пропустить некорректную запись и вывести предупреждение.",
        "Проверить все записи на корректность данных перед началом подсчёта.",
        "Добавить проверку типа данных перед сложением и преобразовать строку в число. ",
        "Исключить записи с некорректными типами данных из обработки."],

    ["Заменить пустой список сотрудников на значение по умолчанию.",
        "Вывести сообщение об ошибке и остановить выполнение программы.",
        "Пропустить распределение задач, если список сотрудников пуст.",
        "Добавить проверку, что список сотрудников не пуст, перед началом распределения задач."],

    ["Part 4_1",
        "Part 4_2",
        "Part 4_3",
        "Part 4_4"],

    ["Part 5_1",
        "Part 5_2",
        "Part 5_3",
        "Part 5_4"]]


define names_bugs = ["name_bug_1", "name_bug_2", "name_bug_3", "name_bug_4", "name_bug_5"]

define phrases_developer_call = ["Нам нужны только радикальные меры для победы над ней!",
    "Давай победим её как можно скорее!",
    "Нужно быть предельно осторожными, чтобы не размножить ему подобных!",
    "За дело!"]

define nums_goods_opt_choi_bug = [0, 2, 1, 0, 1]
define nums_goods_options_fight = [1, 2, 3, 2, 1]
define shown_options = [0, 1, 2, 3]

image monster one = "monsters/monster1.png"
image bg fantasy_world = im.Scale("fantasy_worlds/fantasy_world1.png" , 1920, 1080)

define number_mistakes = 0
define ai_uses_count = 0
define num_fight = 0
define num_elem = 0
define hp_sasha = 100
define xalign_s = 0.5


label start:
    play music "start_fone_music.ogg"
    scene bg room_sasha
    show sasha welcoming at left
    "Это Саша. Он только что закончил учёбу и ищет работу тестировщиком."
    "Работа тестировщика — это не просто поиск ошибок в программах. Это сложный и важный процесс, 
    от которого зависит, насколько хорошо будет работать продукт."
    "Тестировщики проверяют код на стабильность, ищут баги и помогают разработчикам сделать программы идеальными."
    "Саша всегда любил разбираться в мелочах, искать логические несостыковки и находить решения. 
    Именно поэтому он решил, что тестирование программ — это то, чем он хочет заниматься." 
    "И вот, наконец, он получил предложение пройти испытательный срок в крупной IT-компании. 
    Для него это шанс не только начать карьеру, но и узнать, каково это — быть частью команды, создающей будущее." 

    scene bg sachas_computer
    "Если Саша хорошо справится с задачей, то его примут на работу."
    stop music fadeout 1

    jump part1


label part1:
    hide sasha
    scene black with fade
    centered "На следующий день"
    play music "people_fone1.ogg" fadein 1
    
    scene bg in_office with fade
    show sasha normal:
        xalign 0.15
        yalign 1.0
    show boss normal
    show roma normal:
        xalign 0.75
        yalign 1.0

    b "Ну что, Саша, готов приступить к своей первой задаче?"
    s "Конечно, готов. Всего-то нужно проверить код и найти ошибки. Это ведь то, на что я учился."
    r "Вот только не забывай: ошибки здесь бывают далеко не учебные. Некоторые баги умудряются прятаться так, что их и с фонарём не найдёшь."
    s "Не страшно. Если что — есть ты, Рома, чтобы меня выручить."
    r "Ага, мечтай. Я тебе дам пару подсказок, но всё остальное — твоя зона ответственности. Так что готовься потеть."
    b "Мы даём тебе важную задачу. В нашем деле качество продукта — это всё. Если ты найдёшь и исправишь баг, ты не просто улучшишь программу, ты сэкономишь нашей компании кучу денег."
    s "Понял. Не подведу."
    r "Ладно, герой, вот тебе первая программа. Начинай с неё. И если увидишь что-то странное, просто скажи: “Рома, я тут кое-что нашёл”, — и мы разберёмся."
    b "Рома, ты слишком расслабляешь новичков. Саша, если застрянешь, не стесняйся спрашивать. Но я уверен, что ты справишься."
    s "Спасибо за доверие. Приступаю!"
    hide boss
    hide roma
    show sasha excited
    s "Мне так не терпится приступить к работе и показать себя в деле!"
    s "Что-то мне становится нехорошо, кружится голова, ощущение, что меня куда-то засасывает."
    stop music fadeout 1
    call teleport

    scene bg fantasy_world
    show sasha surprised
    play music "disturbing_music.ogg" fadein 1
    s "Где я? Как я сюда попал? Ладно, для начала надо осмотреться."
    show sasha surprised:
        xalign 0.3
        yalign 1.0
    "Пока Саша ходит, он не перестает размышлять о том, как можно решить его первую задачу на работе."
    show sasha surprised:
        xalign 0.7
        yalign 1.0
    s "Почему-то все пути вели меня в одно место, такое ощущение, что я ищу ошибку и все ближе и ближе к ней приближаюсь."
    show sasha surprised:
        xalign 0.9
        yalign 1.0
    s "Она должна быть где-то здесь!"
    
    jump inspect


label part2:
    play music "people_fone2.ogg" fadein 1
    scene bg in_office with fade
    show roma normal
    show sasha normal:
        xalign 0.25
        yalign 1.0
    r "Это было классно!"
    s "Согласен! Спасибо тебе за помощь."
    r "Обращайся!"
    hide roma
    s "Надо передохнуть и после продолжим искать баги."
    stop music fadeout 1
    scene black with fade
    centered "Спустя 30 минут"
    play music "people_fone2.ogg" fadein 1
    scene bg in_office with fade
    show boss normal
    show sasha normal:
        xalign 0.25
        yalign 1.0
    b "У меня есть хорошая новость для тебя."
    s "Какая?"
    b "Одна из наших команд закончила разработку ИИ помощника для тестирования программ."
    b "Ты можешь им пользоваться, но будь осторожней, он ещё не до конца проверен."
    s "Спасибо, сейчас же пойду и опробую его!"
    hide boss
    "Теперь у тебя появилась кнопка \"Помошь ИИ\" в битве с багом, она убирает один из неправильных вариантов за раз."
    "Но не злоупотребляй ей, нейросеть ещё сырая!"
    
    s "Хорошо, что Рома помог. Надо разобраться с остальными задачами." 
    s "Я чувствую, что скоро снова окажусь в этом странном месте. Наверное, когда я буду совсем близко к решению следующей проблемы…" 
    # <Саша возвращается к своему рабочему столу. > 
    scene bg workplace
    # show sasha normal at right
    "Он сосредоточенно работает над второй задачей. Часы тикают. Он чувствует всё нарастающее чувство тревоги, ощущение дежавю." 
    "Саша перепроверяет каждый оператор, каждую переменную."
    "Он снова чувствует… то же самое ощущение, что и в прошлый раз. Голова начинает кружиться…"
    s "Нет… только не это, снова… "
    "Мир вокруг Саши начинает искажаться. Цвета становятся неестественными, предметы расплываются. Звуки искажаются в неприятный гул... "
    call teleport
    play music "disturbing_music.ogg" fadein 1
    $ num_fight = 1
    jump inspect


label part3:
    play music "people_fone2.ogg" fadein 1
    scene bg in_office with fade
    show roma normal
    show sasha normal:
        xalign 0.25
        yalign 1.0
    s "Ну вот, задача решена. Все данные теперь числовые, и счётчик работает. Я был почти уверен, что это будет сложнее. Где же этот сложный баг, который ты мне обещал?"
    r "Ты что, ждал, что я пошлю тебя искать баг с лазерными лучами и роботами? Иногда самые простые ошибки — это самые опасные."
    s "О да, строка вместо числа — это просто хитроумный заговор. Я почти почувствовал, как меня сбивают с пути величественные цифровые лабиринты."
    r "И я думал, ты в первый раз с багами встречаешься! На самом деле, эта ошибка — как раз тот момент, когда ты мог бы почувствовать себя экспертом. Всё очень просто, и именно поэтому её так легко не заметить."
    s "Ну да, этот баг был такой \"невидимый\", что я почти стал верить, что сам ошибся. Ведь кто ещё, как не я, мог бы не заметить, что строка — это не число?"
    r "Да, ты поистине первый человек, который мог бы пропустить это. Просто не забывай: иногда для того, чтобы победить баг, нужно меньше думать, а больше искать очевидное."
    s "Я понял, Рома. Обещаю в следующий раз искать \"очевидное\", пока не буду полностью уверен, что это не будет таким же \"невидимым\" багом, как сейчас."
    r "Отлично, а я, между прочим, начну проверку кодов для самых очевидных ошибок... ну, если ты решишь, что это будет легко. Ты ведь теперь мастер!"
    s "Конечно, мастер... Пожалуй, я поставлю себе медаль \"Победитель очевидных ошибок\" на стол."
    stop music fadeout 1
    call teleport
    play music "disturbing_music.ogg" fadein 1
    $ num_fight = 2
    jump inspect


label to_end:
    if 0 <= number_mistakes <= 3:
        jump good_end
    elif 4 <= number_mistakes <= 8:
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


label sasha_died:
    stop music
    hide sasha
    hide hp sasha
    play sound "wilhelm_scream.ogg"
    pause(1.0)
    scene black with fade
    scene bg hospital_room with fade
    play sound "game_over1.ogg" fadein 1
    "Саша впадает в кому и больше никогда не приходит в себя"
    scene black with fade
    centered "GAME OVER"
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
        jump to_end


label teleport:
    play sound "teleport.ogg"
    scene bg teleport with fade
    pause(1.0)
    return


label inspect:
    scene bg fantasy_world
    
    show sasha normal at right
    image deffect code = "codes/code[num_fight+1].png"
    show deffect code:
        yalign 0.0
        xalign 0.5

    menu:
        "Помогите ему понять в чем была ошибка в программе."

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
        play sound "klick.ogg"
        "Выбран вариант [num_elem+1], верно."
        stop music fadeout 1
        call teleport

        play music "fight1.ogg" fadein 1
        scene bg fight with dissolve
        show sasha normal at left
        image monster = "monsters/monster[num_fight+1].png"
        show monster:
            xalign 0.5
            yalign 0.6
        if num_fight == 0:
            s "Уф, сколько раз это ещё будет повторяться!?"
            s "О нет, кажется это та самая ошибка..."
            s "Самостоятельно я точно не справлюсь, жалко, что моего друга-разработчика нет рядом..."

            show roma normal at right
            r "Молодец, ты смог найти свою первую ошибку!"
            s "Как ты сюда попал? Ты знал про этот мир?"
            r "Это каждый тестировщик знает, ты в каком веке живешь? Я появляюсь в этом мире, когда тестировщику плохо. Меньше слов - больше дела."
            image hp sasha = "hp/hp [hp_sasha]%.png"
            show hp sasha:
                yalign 0.32
                xalign 0.00
            show sasha excited at left
            s "Это что за полоска надо мной появилась!? HP!?"
            r "Да, и к сожанию они будут уменьшаться при каждой ошибке в бою. Если они закончатся, то ты больше не сможешь выбраться из этого мира."
            s "\"Таких приколов я не видел еще парни!\""
            show sasha normal at left
        else:
            show roma normal at right
            show monster 
            s "Вот мы и снова здесь..."
        r "[get_random_elem_in_array(phrases_developer_call)]"

        $ shown_options = [0, 1, 2, 3, 4]
        jump fight
    play sound "klick_NO.ogg"
    "Выбран вариант [num_elem+1], неверно."
    $ number_mistakes += 1
    jump inspect

label fight:
    image hp sasha = "hp/hp [hp_sasha]%.png"
    show hp sasha:
        yalign 0.32
        xalign 0.00
    menu:
        s "Давай выберем вариант, который исправит ошибку."
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
        play sound "klick.ogg"
        pause(0.2)
        play sound "wilhelm_scream.ogg"
        hide monster
        "Выбран вариант [num_elem+1], Верно."
        stop music fadeout 1
        call teleport
        jump select_part
    play sound "klick_NO.ogg"
    "Выбран вариант [num_elem+1], Неверно."
    $ hp_sasha -= 10
    if hp_sasha == 0:
        jump sasha_died

    $ number_mistakes += 1
    jump fight

label AI_help:
    play sound "fuck-you1.ogg"
    if ai_uses_count > 4:
        jump skynet_end
     
    python:
        import random 

        while True:
            del_item = random.randint(0,3)
            if nums_goods_options_fight[num_fight] != del_item and del_item in shown_options:
                shown_options.remove(del_item)
                break
        renpy.say(ai, "Мне кажется, что вариант \"[phrases_fight[num_fight][del_item]]\" не правильный.")
    jump fight