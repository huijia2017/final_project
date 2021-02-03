"""
subject: python programming
student: Huijia Yang 101156

project description:
    this project is to show how the customer purcharsing and storage managing working in a small market,
    in the shopping list, it's including the item code, name, price and amount, the customer can add, change and
    delete item in the end of shopping, a list containing the total price and all details above will be printed out.

    in the storage managing part, one can enter(r) to get in the repository system. after that, adding the item,
    changing or deleting are available, and the new item list will be printed out.
"""

# define a repository
repository = dict()
shop_list = []

product = [["1001", "p", 88.0, 10],
           ["1002", "y", 69.0, 12],
           ["1003", "t", 59.0, 188],
           ["1004", "h", 109.0, 56],
           ["1005", "o", 108.0, 100],
           ["1006", "n", 77.0, 122]]


# Define a function to initialize the product
def init_repository():
    for i in range(len(product)):
        repository[product[i][0]] = product[i]


# show the list of product
def show_goods():
    print("welcome to 'kocham sie ziabka'")
    print('Item list:')
    print("%13s%40s%10s%10s" % ("code", "name", "price", "amount"))
    for s in repository.values():
        s = tuple(s)
        print("%15s%40s%12s%12s" % s)


# show the shopping list
def show_list():
    print("=" * 80)
    # print out the list if it's not empty.
    if not shop_list:
        print("NO ITEM SELECTED")
    else:
        title = "%-5s|%10s|%10s|%10s|%10s|%10s" % \
                ("ID", "code", "product", "price", "amount", "total")
        print(title)
        print("-" * 80)
        # recording the total price
        sum = 0
        for i, item in enumerate(shop_list, start=1):
            id = i
            # require the first element: code
            code = item[0]
            # name
            name = repository[code][1]
            # price
            price = repository[code][2]
            # amount
            amount = item[1]
            # total
            total = price * amount
            # sum
            sum = sum + total
            line = "%-5s|%10s|%10s|%10s|%10s|%10s" % \
                   (id, code, name, price, amount, total)
            print(line)
        print("-" * 80)
        print("                                            In total: ", sum)
    print("=" * 80)


def add():
    code = input("please enter the product code:\n")
    # code is not found
    if code not in repository:
        print("Code not found, please enter again.")
        return
    goods = repository[code]
    amount = input("please enter the amount:\n")
    shop_list.append([code, int(amount)])


# edit the item amount so that to change the shoping list
def edit():
    id = input("please enter the item ID you want to change:\n")
    index = int(id) - 1
    item = shop_list[index]
    amount = input("please enter the amount you want to purchase:\n")
    item[1] = int(amount)


# deleting items.
def delete():
    id = input("please enter the item ID which you want to delete: ")
    index = int(id) - 1
    # deletet the item by ID
    del shop_list[index]


def payment():
    # print out the list
    show_list()
    print('\n' * 2)
    print("thank you for shopping here")
    # ending
    import os
    os._exit(0)


# Management system
# add item
def adds():
    # require item details
    a = input("please enter the code:")
    b = input('please enter the name:')
    c = input('please enter the price:')
    d = input('please enter the amount:')
    # add the item to the list
    product.append([a, b, c, d])
    # re-print the item list
    init_repository()
    show_goods()


# modify
def edits():
    a = input("please enter the code:")
    # require the new value
    if a in repository.keys():
        e = input("please enter the modified name:")
        f = input("please enter the modified price:")
        g = input("please enter the amount:")
        repository.update({a: [a, e, f, g]})
        print(repository[a])
        show_goods()
    else:
        print('item error')


def deletes():
    h = input('please enter the code you want to delete:')
    # deleting by the code
    repository.pop(h)
    show_goods()


# re-print the item list
def show_good():
    show_goods()


cmd_dicts = {'a': adds, 'e': edits, 'd': deletes, 's': show_good, 'q': quit}


def root():
    # print the list
    show_goods()
    print("welcome to ziabka management platform")
    print("=" * 100)
    while True:
        cmds = input("management system order: \n" +
                     "    adds(a)  edits(e)  deletes(d)  list(s)  return(q)\n")
        if cmds == 'q':
            return
        elif cmds not in cmd_dicts:
            print("no such item!")
        else:
            cmd_dicts[cmds]()


cmd_dict = {'a': add, 'e': edit, 'd': delete, 'p': payment, 's': show_goods, 'r': root}

init_repository()
show_goods()


def show_command():
    cmd = input("the operation order: \n" +
                "    add(a)  edit(e)  delete(d)  purchase(p)  product(s)  manage(r)\n")
    if cmd not in cmd_dict:
        print("sorry! no such item, please check again.")
    else:
        cmd_dict[cmd]()


while True:
    show_list()
    show_command()

# Note: enter P to stop
