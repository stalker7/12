from pprint import pprint

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
                                                'quantity' : ing * person_list }


    return resurs



recipe = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
pprint(recipe)



