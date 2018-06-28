import json
import chardet


def open_file_json(target_file):
    encode = None
    strings = None
    with open("json_files/{}".format(target_file), "rb") as json_file:
        specimen = json_file.read()
        encode = chardet.detect(specimen)
    with open("json_files/{}".format(target_file), encoding=encode["encoding"]) as json_file:
        strings = json.load(json_file)
    return strings


def count_frequency(target_file):
    data = open_file_json(target_file)
    calc_dict = {}
    values = []
    for news_item in data["rss"]["channel"]["items"]:
        values.extend(news_item["description"].strip().split(" "))
    for every_word in values:
        if len(every_word) < 6:
            values.remove(every_word)
        elif every_word in calc_dict.keys():
            calc_dict[every_word] += 1
        else:
            calc_dict[every_word.lower()] = 1
    print("\nВ выбранном Вами файле {}:".format(target_file))
    for index in (sorted(calc_dict, key=calc_dict.get, reverse=True)[:10]):
        print("слово '{}' встречается {} раз".format(index, calc_dict[index]))


def main():
    answer = ""
    while True:
        print("\nПрограмма для работы с json готова к работе.\nВыберите нужный файл и нажмите соответствующую цифру:\n",
            "Для 'newsafr.json' нажмите 1\n",
            "Для 'newscy.json' нажмите 2\n",
            "Для 'newsfr.json' нажмите 3\n",
            "Для 'newsit.json' нажмите 4\n",
            "Для выхода нажмите q\n")
        answer = input()
        if answer == "1":
            count_frequency("newsafr.json")
        elif answer == "2":
            count_frequency("newscy.json")
        elif answer == "3":
            count_frequency("newsfr.json")
        elif answer == "4":
            count_frequency("newsit.json")
        elif answer == "q":
            print("Программа для работы с json завершена.")
            break
        else:
            print("команда неверна попробуйте ещё раз")


main()