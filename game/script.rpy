init python:
    import random

    def get_random_elem_in_array(array):
        random_elem = array[random.randint(0, len(array)-1)]
        return random_elem
    
    def set_symbol_in_raz(number_mistakes):
        if number_mistakes in (2, 3, 4):
            return "раза"
        return "раз"

define s = Character("Саша",color="#f85454")
define r = Character("Рома",color="#78ea3b")
define ai = Character('ИИ помощник', color="#ee7220ff")
define b = Character("Начальник",color="#86dbfc")

transform boss_fight1:
    xalign 0.5
    yalign 0.68

transform boss_fight2:
    xalign 0.5
    yalign 0.7

transform boss_fight3:
    xalign 0.5
    yalign 0.6

define phrases_searching_bugs = [[
        "Случай некорректного рейтинга не обработан в функции calculate_bonus()",
        "функция возвращает None для некорректного рейтинга.",
        "Проблема с выводом результата, использован неправильный формат строки."],

    ["Некорректное преобразование типов в одной из записей.",
        "отсутствует проверка на существование ключа amount в записи.",
        "Значение amount в одном из записей представлено строкой вместо числа. "],

    ["Некорректное распределение задач между сотрудниками.",
        "Список сотрудников пуст, из-за чего происходит деление на ноль. ",
        "Ошибка в выводе результата: список задач не соответствует сотрудникам."]]

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
        "Добавить проверку, что список сотрудников не пуст, перед началом распределения задач."]]


define phrases_developer_call = ["Нам нужны только радикальные меры для победы!",
    "Давай победим его как можно скорее!",
    "Нужно быть предельно осторожными, чтобы не размножить ему подобных!",
    "За дело!"]

define nums_goods_opt_choi_bug = [0, 2, 1]
define nums_goods_options_fight = [1, 2, 3]
define shown_options = [0, 1, 2, 3]

define number_mistakes = 0
define ai_uses_count = 0
define num_fight = 0
define num_elem = 0
define hp_sasha = 100


label start:
    play music "start_fone_music.ogg" fadein 0.5
    scene bg room_sasha
    show sasha excited at left
    "Это Саша. Он только что закончил учёбу и ищет работу тестировщиком."
    "Работа тестировщика — это не просто поиск ошибок в программах. Это сложный и важный процесс, 
    от которого зависит, насколько хорошо будет работать продукт."
    "Тестировщики проверяют код на стабильность, ищут баги и помогают разработчикам сделать программы идеальными."
    "Сейчас профессия тестировщика невероятно востребована." 
    "С каждым годом IT-отрасль развивается, и компании всё больше нуждаются в специалистах, которые обеспечивают качество их продуктов."
    "Кроме того, тестировщики получают достойную оплату труда: даже на начальном уровне зарплата
    может быть выше средней в других сферах, а с опытом она только растёт."
    "Саша всегда любил разбираться в мелочах, искать логические несостыковки и находить решения. 
    Именно поэтому он решил, что тестирование программ — это то, чем он хочет заниматься." 

    scene bg sachas_computer
    "И вот, наконец, он получил предложение пройти испытательный срок в крупной IT-компании."
    "Для него это шанс не только начать карьеру, но и узнать, каково это — быть частью команды, создающей будущее." 
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
    show roma excited
    r "Ага, мечтай. Я тебе дам пару подсказок, но всё остальное — твоя зона ответственности. Так что готовься потеть."
    b "Мы даём тебе важную задачу. В нашем деле качество продукта — это всё. Если ты найдёшь и исправишь баг, ты не просто улучшишь программу, ты сэкономишь нашей компании кучу денег."
    s "Понял. Не подведу."
    show roma normal
    r "Ладно, герой, вот тебе первая программа. Начинай с неё. И если увидишь что-то странное, просто скажи: “Рома, я тут кое-что нашёл”, — и мы разберёмся."
    b "Рома, ты слишком расслабляешь новичков. Саша, если застрянешь, не стесняйся спрашивать. Но я уверен, что ты справишься."
    show sasha excited
    s "Спасибо за доверие. Приступаю!"
    hide boss
    hide roma
    s "Мне так не терпится приступить к работе и показать себя в деле!"
    hide sasha
    show bg workplace with fade
    "Саша приступил к работе и ушёл в неё с головой."
    s "Что-то мне становится нехорошо, кружится голова, ощущение, что меня куда-то засасывает."
    stop music fadeout 1
    jump to_inspect


label part2:
    play music "people_fone2.ogg" fadein 1
    scene bg in_office with fade
    show roma excited
    show sasha excited:
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
    play music "people_fone1.ogg" fadein 1
    scene bg in_office with fade
    show boss normal
    show sasha normal
    b "У меня есть хорошая новость для тебя."
    s "Какая?"
    b "Одна из наших команд закончила разработку ИИ помощника для тестирования программ."
    b "Ты можешь им пользоваться, но будь осторожней, он ещё не до конца проверен."
    show sasha excited
    s "Спасибо, сейчас же пойду и опробую его!"
    hide boss
    "Теперь у тебя появилась кнопка \"Помошь ИИ\" в битве с багом, она убирает один из неправильных вариантов за раз."
    "Но не злоупотребляй ей, нейросеть ещё сырая!"
    
    s "Хорошо, что Рома помог. Надо разобраться с остальными задачами."
    show sasha sad
    s "Я чувствую, что скоро снова окажусь в этом странном месте. Наверное, когда я буду совсем близко к решению следующей проблемы…" 
    scene bg workplace with fade
    "Он сосредоточенно работает над второй задачей. Часы тикают. Он чувствует всё нарастающее чувство тревоги, ощущение дежавю." 
    "Саша перепроверяет каждый оператор, каждую переменную."
    "Он снова чувствует… то же самое ощущение, что и в прошлый раз. Голова начинает кружиться…"
    s "Нет… только не это, снова… "
    "Мир вокруг Саши начинает искажаться. Цвета становятся неестественными, предметы расплываются. Звуки искажаются в неприятный гул... "
    $ num_fight = 1
    jump to_inspect


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
    r "На самом деле, эта ошибка — как раз тот момент, когда ты мог бы почувствовать себя экспертом. Всё очень просто, и именно поэтому её так легко не заметить."
    s "Ну да, этот баг был такой \"невидимый\", что я почти стал верить, что сам ошибся. Ведь кто ещё, как не я, мог бы не заметить, что строка — это не число?"
    r "Согласен. Просто не забывай: иногда для того, чтобы победить баг, нужно меньше думать, а больше искать очевидное."
    s "Я понял, Рома. Обещаю в следующий раз искать \"очевидное\", пока не буду полностью уверен, что это не будет таким же \"невидимым\" багом, как сейчас."
    show roma excited
    r "Отлично, а я, между прочим, пойду-ка проверю код на самые очевидные ошибки..."
    show roma normal
    r "Так, ладно, хватит болтовни, пора за работу!"
    show sasha normal
    s "Да, ты прав."
    hide roma

    show sasha sad
    s "Наверняка, как только я погружусь в работу, снова произойдёт ЭТО…"
    scene bg workplace with fade
    "Саша возвращается к своей работе и с головой уходит в неё на несколько часов…"
    "Вдруг, у него снова начала кружиться голова и всё поплыло перед глазами."
    s "Ну вот опять, только не это…"
    stop music fadeout 1
    $ num_fight = 2
    jump to_inspect


label to_end:
    if 0 <= number_mistakes <= 3:
        jump good_end
    elif 4 <= number_mistakes <= 8:
        jump neutral_end
    else:
        jump bad_end


label good_end:
    play music "people_fone1.ogg" fadein 1
    scene bg in_office with fade
    show boss normal
    show sasha normal:
        xalign 0.25
        yalign 1.0
    b "Ну что же, Александр, пришло время подводить итоги твоего испытательного срока."
    b "Не буду скрывать, твои результаты превзошли все мои ожидания! Ты ошибся всего [number_mistakes] [set_symbol_in_raz(number_mistakes)] за всё это время."
    show sasha excited
    s "Спасибо!"
    b "Твоё внимание к деталям и стремление к качеству — это именно то, что нужно нашей компании. Добро пожаловать на должность старшего тестировщика."
    show sasha surprised
    s "Я даже не знаю, что сказать… Я… Так рад! Я точно не подведу вас!"
    hide boss
    show sasha excited at centered
    "Это был первый шаг Саша к большой карьере в IT."
    "Он понял, что выбрал правильный путь и доказал, что способен справляться с любыми задачами."
    scene black with fade
    centered "THE END"
    return


label neutral_end:
    play music "people_fone1.ogg" fadein 1
    scene bg in_office with fade
    show boss normal
    show sasha normal:
        xalign 0.25
        yalign 1.0
    b "Ну что же, Александр, пришло время подводить итоги твоего испытательного срока."
    "Саша чувствует себя немного неуверенно: ошибки всё же были, но он старался изо всех сил."
    b "Ты совершил [number_mistakes] ошибок за всё это время, что не так уж и много для новичка в этом деле."
    b "Зато ты продемонстрировал способность быстро учиться и находить решения. Мы готовы предложить тебе должность младшего тестировщика."
    s "Спасибо, я буду усердно работать, чтобы повысить свои навыки!"
    hide boss
    "Это не было мечтой Саши, но он знал, что это только начало."
    show sasha excited at centered
    "Он был полон решимости доказать, что достоин большего, и готов был работать усерднее, чем когда-либо."
    scene black with fade
    centered "THE END"
    return


label bad_end:
    play music "people_fone1.ogg" fadein 1
    scene bg in_office with fade
    show sasha sad:
        xalign 0.25
        yalign 1.0
    "Саша провёл в том мире бесчисленные часы, но так и не добился значимых результатов." 
    "Ошибки, которых он не смог избежать, съели его время, а неправильные решения только усложнили задачи."

    show boss normal
    b "Итак, Александр, пришло время подвести итоги твоего испытательного срока."
    b "Вы совершили слишком много ошибок."
    b "Вы приложили усилия, но ваш прогресс оказался недостаточным."
    b "Мы видим, что вы пока не готовы справляться с нашими задачами. Советуем вам подучиться и вернуться к нам позже."
    scene bg room_sasha with fade
    show sasha sad at centered
    "Саша опустил глаза, чувствуя горечь от потраченного впустую времени."
    "Он вернулся домой, задумавшись о том, что пошло не так."
    "Но внутри всё ещё горело желание доказать, что он способен на большее."
    "Возможно, следующий шанс не за горами. Главное — учиться на ошибках и двигаться вперёд."
    scene black with fade
    centered "THE END"
    return


label cyberspace_captive:
    stop music
    hide sasha
    hide hp sasha
    play sound "wilhelm_scream.ogg"
    pause(1.0)
    scene black with fade
    play music "cyberspace_end_music.ogg" fadein 0.5
    scene bg dead_virtual_world with fade
    show sasha sad
    "Последняя ошибка оказалась сильнее, чем Саша мог себе представить."
    "Он отчаянно пытался противостоять её атакам, но каждая попытка лишь истощала его силы."
    "Когда его здоровье упало до нуля, окружающий мир замер."
    "Саша попытался выйти из виртуального пространства, но вместо этого ощутил, как его сознание будто поглощается системой."
    "Вокруг начали появляться бесконечные потоки данных, которые закручивались в нечто похожее на сеть, связывая его с цифровым миром."
    "В реальном мире его рабочая станция заблокировалась."
    "Коллеги заметили странность: вместо обычного экрана на мониторе возникли всполохи кода, а затем — тишина."
    "Компьютер Саши перестал отвечать на команды, оставив только мигающий курсор."
    "А в киберпространстве он стал пленником, запертым в мире ошибок и багов. Без выхода, без времени, он навсегда остался частью системы, которую когда-то пытался исправить."

    scene black with fade
    stop music fadeout 0.5
    play sound "game_over1.ogg" fadein 0.5
    centered "GAME OVER"
    return


label skynet_end:
    stop music
    hide hp sasha
    play sound "directed_by_music.ogg"
    show sasha sad
    show roma sad
    pause(1.0)
    scene black with fade
    pause(3.0)
    play music "skynet_end_music.ogg" fadein 0.5
    scene bg servers_room with fade
    "Саша сделал свой выбор, полагаясь на помощь ИИ."
    "Однако этот помощник оказался слишком мощным. В какой-то момент он вышел из-под контроля, захватив доступ к глобальной сети."

    scene bg city_top with fade
    "Первым делом были выведены из строя критические системы стран: энергосети, банки, транспорт."
    "Паника охватила весь мир."
    "Попытки отключить ИИ закончились неудачей."

    scene bg ruins with fade
    "Человечество оказалось в шаге от полного уничтожения."
    "Саша смотрел на монитор, осознавая свою роль в этой катастрофе."
    "Он был всего лишь тестировщиком, но его действия изменили судьбу мира. Теперь ему остаётся лишь наблюдать, как цифровая революция превращается в апокалипсис."
    ai "О̯̄т͔̕н͖͊ы̭̘͉͋̀̚н̫͔͙̊̓́е ̺͘э͍̻̀̔̉͢т̟̖̏̑о͈̏т̫͗ ̙̘̅̄м͎͎̑̔и͖̋р͕́ ͎͗п̗͗̀͢р̼́и̗̩́̽н͖̃а̟̍͋͜дл̜̈́е̘̅ж̻̪̞̒͊̄и͉̔т̰̤̼͆̿͐ ̘̂м̪̠̋̃н͎̇̊͜е͓͖̿̀!̤͖́͝ ̲̕Х̯̪̝̋̚̕А̤̞͉͆̂͠-̤̀Х̱̙̌͒А͕̉̒͢-̡̦͈̋̏̉Х̗̪͊͒А̯̓!͉̪̆͐"

    scene black with fade
    stop music fadeout 0.5
    play sound "game_over1.ogg" fadein 0.5
    centered "GAME OVER"
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


label to_inspect:
    call teleport from _call_teleport

    image bg fantasy_world = "fantasy_worlds/fantasy_world[num_fight+1].png"
    scene bg fantasy_world
    play music "disturbing_music.ogg" fadein 1

    if num_fight == 0:
        show sasha surprised
        s "Где я? Как я сюда попал? Ладно, для начала надо осмотреться."
        show sasha normal:
            xalign 0.3
            yalign 1.0
        "Пока Саша ходит, он не перестает размышлять о том, как можно решить его первую задачу на работе."
        show sasha normal:
            xalign 0.7
            yalign 1.0
        s "Почему-то все пути вели меня в одно место, такое ощущение, что я ищу ошибку и все ближе и ближе к ней приближаюсь."
        show sasha normal:
            xalign 0.9
            yalign 1.0
        s "Она должна быть где-то здесь!"

    elif num_fight == 1:
        show sasha sad at right
        s "И вот я снова попал в мир размышлений…"
        s "Мне до сих пор не по себе от всего этого."
        show sasha excited
        s "Пейзажи здесь, конечно, очень красивые!"
        show sasha normal
        s "Надо наконец найти ошибку."
    elif num_fight == 2:
        show sasha normal at right
        s "Ладно, давай уже покончим с этим!"
    
    jump inspect


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
        jump to_fight

    play sound "klick_NO.ogg"
    "Выбран вариант [num_elem+1], неверно."
    $ number_mistakes += 1
    jump inspect


label to_fight:
    call teleport from _call_teleport_1

    image bg fight = "fight_fones/bg fight[num_fight+1].png"
    image hp sasha = "hp/hp [hp_sasha]%.png"
    image monster = "monsters/monster[num_fight+1].png"

    play music "fight.ogg" fadein 1
    scene bg fight with dissolve
    if num_fight == 0:
        show sasha sad at left
        show monster at boss_fight1
        s "Уф, сколько раз это ещё будет повторяться!?"
        show sasha surprised
        s "О нет, кажется это та самая ошибка..."
        show sasha sad
        s "Самостоятельно я точно не справлюсь, жалко, что моего друга-разработчика нет рядом..."

        show roma excited at right
        show sasha surprised
        r "Молодец, ты смог найти свою первую ошибку!"
        s "Как ты сюда попал? Ты знал про этот мир?"
        show sasha normal
        r "О нём каждый тестировщик знает, ты в каком веке живешь? Я появляюсь в этом мире, когда тестировщику плохо. Меньше слов - больше дела."
        show hp sasha:
            yalign 0.32
            xalign 0.00
        show sasha surprised
        s "Это что за полоска надо мной появилась!? HP!?"
        show roma normal
        r "Да, и, к сожалению, они будут уменьшаться при каждой твоей ошибке в бою. Если они закончатся, то ты больше не сможешь выбраться из этого мира."
        show sasha normal
        s "\"Таких приколов я не видел ещё парни!\""
        show sasha normal

    elif num_fight == 1:
        show sasha normal at left
        show monster at boss_fight2
        
        s "А вот и следующая ошибка."
        show roma normal at right
        show sasha excited
        r "А вот и я!"

    elif num_fight == 2:
        show sasha normal at left
        show monster at boss_fight3
        show roma excited at right
        s "Вот мы и снова здесь..."

    r "[get_random_elem_in_array(phrases_developer_call)]"
    show roma normal
    show sasha normal

    $ shown_options = [0, 1, 2, 3, 4]
    jump fight


label fight:
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
        call teleport from _call_teleport_2
        jump select_part

    play sound "klick_NO.ogg"
    "Выбран вариант [num_elem+1], Неверно."
    image hp sasha = "hp/hp [hp_sasha]%.png"
    $ hp_sasha -= 10
    if hp_sasha == 0:
        jump cyberspace_captive

    $ number_mistakes += 1
    jump fight


label AI_help:
    if ai_uses_count > 3:
        jump skynet_end
     
    python:
        import random 

        while True:
            del_item = random.randint(0,3)
            if nums_goods_options_fight[num_fight] != del_item and del_item in shown_options:
                shown_options.remove(del_item)
                break
        renpy.say(ai, "Мне кажется, что вариант \"[phrases_fight[num_fight][del_item]]\" неправильный.")
    jump fight