from pprint import pprint
import os
book = {}
catalog = 'catalog.txt'
def cat_log(catalog):
    with open(catalog, encoding='utf-8') as file_s:
        for file in file_s:
            name_of_dish = file.strip()
            good = []
            ingredient = ['ingredient_name', 'quantity', 'measure']
            for item in range(int(file_s.readline())):
                goods = file_s.readline().strip().split('|')
                ingr_edient = dict(zip(ingredient, goods))
                good.append(ingr_edient)
                book[name_of_dish] = good
        file_s.readline()
        return book
dishes = cat_log(catalog)
pprint(dishes)
print()

def get_shop_list_by_dishes(dishes, person_list):
    resurs = {}
    for dish in dishes:
        if dish in book:
            for ingridients in book[dish]:
                ing = int(ingridients['quantity'])
                name = ingridients['ingredient_name']
                if ingridients['ingredient_name'] in resurs:
                    resurs[name]['quantity'] = ing * person_list
                else:
                    resurs[name] = {'measure': ingridients['measure'],
                                                'quantity' : ing * person_list}
    return resurs
recipe = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
pprint(recipe)
print()

def len_story(*txt_file):
    res = {}
    for file in txt_file:
        with open(file, encoding='utf-8') as files:
            text_len = len(files.readlines())
            res.setdefault(file, text_len)
    sort_txt = sorted(res, key=res.get)
    sort_text = {}
    for fi_le in sort_txt:
        sort_text[fi_le] = res[fi_le]
    return sort_text


def story_t(dictionary):
    base_path = os.getcwd()
    story_text = 'story.txt'

    full_path = os.path.join(base_path, story_text)
    text = {}
    for k, v in dictionary.items():
        with open(k, encoding='utf-8') as file:
            text.setdefault(k, file.read().strip())

    with open(full_path, 'a', encoding='utf-8') as files:
        for key, value in text.items():
            files.write(f'{key}\n')
            files.write(f'{str(dictionary[key])}\n')
            files.write(f'{value}\n')


new_file = len_story('text1.txt', 'text2.txt', 'text3.txt')

story_t(new_file)


