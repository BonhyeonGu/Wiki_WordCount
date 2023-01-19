import pickle as pic


def list_chuck(arr, n):
    if len(arr) % n != 0:
        n -= 1
    n = len(arr) // n
    return [arr[i: i + n] for i in range(0, len(arr), n)]

if __name__ == "__main__":
    locale = './'
    split_count = 5

    with open(locale + 'anchorData.pkl', 'rb') as f:
        dict_full:dict = pic.load(f)
    print(len(dict_full))

    dict_key_list = list(dict_full.keys())
    lists = list_chuck(dict_key_list, split_count)
    
    for i in range(len(lists)):
        print(len(lists[i]))
        with open('keyOnly%s.pkl'%(str(i)),'wb') as f:
            pic.dump(lists[i], f)
    print("end")