# Задача 2. В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.
""
def fruits():
    words = list()
    fruits=("Абрикос",
            "Авокадо",
            "Австромиртус",
            "Азимина",
            "Айва",
            "Акебия",
            "Аки",
            "Алыча",
            "Ананас",
            "Аннона",
            "Апельсин",
            "Араза",
            "Арбуз",
            "Астрокариум",
            "Баккорея",
            "Бакупари",
            "Банан",
            "Билимби",
            "Бирсонима",
            "Бойзенова ягода",
            "Боярышник",
            "Бромелия",
            "Бунхозия",
            "Вампи",
            "Виноград",
            "Вишня",
            "Воаванга",
            "Восковница",
            "Гандария",
            "Гарциния",
            "Генипа",
            "Гетеромелес",
            "Гилоцереус",
            "Гранадилла",
            "Гранат",
            "Гревия",
            "Грейпфрут",
            "Грумичама",
            "Груша",
            "Гуава",
            "Гуайява",
            "Давидсония",
            "Дакриодес",
            "Джамбоза",
            "Джамболан",
            "Джамбу",
            "Джекфрут",
            "Дуриан",
            "Дыня",
            "Жаботикаба",
            "Звёздчатое яблоко",
            "Имбу",
            "Инга",
            "Инжир (фига)",
            "Ирга",
            "Каимито",
            "Какао",
            "Канистель",
            "Канталупа",
            "Капулин",
            "Карамбола",
            "Кариокар",
            "Карисса",
            "Квини",
            "Кепель",
            "Кешью",
            "Кивано",
            "Киви",
            "Кизил",
            "Кокколоба",
            "Кокона",
            "Кокос",
            "Корлан",
            "Королёк",
            "Криптокария",
            "Ксимения",
            "Кудрания",
            "Кумкват",
            "Купуасу",
            "Куруба",
            "Лайм",
            "Лангсат",
            "Лардизабала",
            "Лимон",
            "Личи",
            "Лонган",
            "Луума",
            "Луло",
            "Лума",
            "Малина",
            "Манго",
            "Мангостан",
            "Мандарин",
            "Маракуйя",
            "Маранг",
            "Мелоди",
            "Минеола",
            "Мирциария",
            "Момбин",
            "Момордика",
            "Мунтингия",
            "Мушмула",
            "Наранхилья",
            "Нектарин",
            "Опунция",
            "Оробланко",
            "Пальма",
            "Пандан",
            "Папайя",
            "Папеда",
            "Пассифлора",
            "Переския",
            "Персик",
            "Питайя (питахайя)",
            "Питецеллобиум",
            "Питомба",
            "Платония",
            "Плумкот",
            "Помароза",
            "Помелит",
            "Помело",
            "Померанец",
            "Пулазан",
            "Пурума",
            "Ракум-салакка",
            "Рамбутан",
            "Рангпур",
            "Родомирт",
            "Роллиния",
            "Салак",
            "Сантол",
            "Саподилла",
            "Сапота",
            "Саусеп",
            "Сахарное яблоко",
            "Свити",
            "Сизигиум",
            "Сикана",
            "Сирсак",
            "Склерокария",
            "Слива",
            "Страстоцвет",
            "Стрихнос",
            "Тамарилло",
            "Тамаринд",
            "Угни",
            "Учува",
            "Фальза",
            "Фейхоа",
            "Фига",
            "Физалис",
            "Фикус",
            "Филлантус",
            "Хурма",
            "Цедра",
            "Чалта",
            "Чемпедак",
            "Черёмуха",
            "Черешня",
            "Черимойя",
            "Чомпу",
            "Чулюпа",
            "Чупа-чупа",
            "Шелковица",
            "Шефердия",
            "Эвтерпа",
            "Элеокарпус",
            "Яблоко")
    letter = input("Введите букву : ").upper()
    for el in fruits:
        if el[0] == letter:
            words.append(el)
    return words

n =fruits()
print(n)