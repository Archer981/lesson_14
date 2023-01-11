# География кинематографа
#
# А теперь давайте выберем из базы, все страны в которых снято 100 или более фильмов и сериалов.
# Аналогично предыдущему заданию выведите в первой колонке наименование страны
# а во второй количество снятых фильмов
#
# Пример результата:
# +----------------+------------+
# |     Страна     | количество |
# +----------------+------------+
# | United States  |    2555    |
# +----------------+------------+
#
# Структура таблицы
# -----------------------
# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актеры
# country — страна производства
# date_added — когда добавлен на Нетфликс
# release_year — когда выпущен в прокат
# rating — возрастной рейтинг
# duration — длительность
# duration_type — минуты или сезоны
# listed_in — список жанров и подборок
# description — краткое описание
# -----------------------
import sqlite3
import prettytable

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = ("""
                select country as 'Страна', count(*) as 'количество'
                from netflix
                where country not null
                group by country
                having count(*) >= 100
                order by count(*) desc
""")  # TODO измените код запроса
result = cur.execute(sqlite_query)

# не удаляйте код дальше, он нужен для вывода результата
# запроса в красивом формате

mytable = prettytable.from_db_cursor(result)
mytable.max_width = 30


if __name__ == '__main__':
    print(mytable)
