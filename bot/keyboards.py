# Модуль для создания клавиатур Telegram бота.

# Этот модуль содержит функции для создания:
# 1. Клавиатуры с темами задач (с пагинацией)
# 2. Клавиатуры для выбора минимальной сложности
# 3. Клавиатуры для выбора максимальной сложности

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOPICS_PER_PAGE = 8

TOPICS = [
    "math",
    "greedy",
    "sortings",
    "games",
    "data structures",
    "graphs",
    "dp",
    "bitmasks",
    "combinatorics",
    "probabilities",
    "trees",
    "constructive algorithms",
    "brute force",
    "dfs and similar",
    "number theory",
    "shortest paths",
    "binary search",
    "implementation",
    "hashing",
    "strings",
    "flows",
    "interactive",
    "dsu",
    "divide and conquer",
    "two pointers",
    "ternary search",
    "matrices",
    "chinese remainder theorem",
    "geometry",
    "2-sat",
    "fft",
    "*special",
    "expression parsing",
    "string suffix structures",
    "graph matchings",
    "schedules",
    "meet-in-the-middle",
]


def get_topics_keyboard(page: int = 0) -> InlineKeyboardMarkup:
    start = page * TOPICS_PER_PAGE
    end = start + TOPICS_PER_PAGE
    page_topics = TOPICS[start:end]

    buttons = []
    row = []
    for i, topic in enumerate(page_topics, 1):
        row.append(InlineKeyboardButton(text=topic, callback_data=f"topic:{topic}"))
        if i % 2 == 0:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)

    nav_buttons = []
    if page > 0:
        nav_buttons.append(
            InlineKeyboardButton(text="⬅️ Назад", callback_data=f"page:{page - 1}")
        )
    if end < len(TOPICS):
        nav_buttons.append(
            InlineKeyboardButton(text="Вперёд ➡️", callback_data=f"page:{page + 1}")
        )
    if nav_buttons:
        buttons.append(nav_buttons)

    return InlineKeyboardMarkup(inline_keyboard=buttons)


DIFFICULTIES = [
    "800",
    "1000",
    "1200",
    "1400",
    "1600",
    "1800",
    "2000",
    "2200",
    "2400",
    "2600",
]


def get_difficulties_keyboard() -> InlineKeyboardMarkup:
    buttons = []
    row = []
    for i, diff in enumerate(DIFFICULTIES, 1):
        row.append(
            InlineKeyboardButton(text=f"От {diff}", callback_data=f"difficulty:{diff}")
        )
        if i % 3 == 0:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_difficulties_to_keyboard(difficulty_from: float) -> InlineKeyboardMarkup:
    valid_difficulties = [
        diff for diff in DIFFICULTIES if float(diff) > difficulty_from
    ]

    buttons = []
    row = []
    for diff in valid_difficulties:
        row.append(
            InlineKeyboardButton(
                text=f"До {diff}", callback_data=f"difficulty_to:{diff}"
            )
        )
        if len(row) == 3:  # 3 кнопки в строке
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    return InlineKeyboardMarkup(inline_keyboard=buttons)
