# Это делаю я (Никита)
#
# На вход подаются 1) нормализованный запрос 2) словарь из нормализованных текстов 
# На выход возвращается список из самых подходящих текстов, если таких текстов нет, то возвращается "None"
#
# Пример:
# Вход: 
# Нормализованный запрос: "восстановить пропуск" 
# Словарь нормализованных текстов: {0: "кабинет соцгум восстановлениe пропуск",
#                                   1: "стол дерево", 2: "восстановить отчисление прийти кабинет 999"}
#
# Выход: {0: "кабинет соцгум восстановлениe пропуск", 2: "восстановить отчисление прийти кабинет 999"}
