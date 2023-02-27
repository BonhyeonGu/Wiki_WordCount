import pickle as pic

if __name__ == "__main__":
    file_locales = ['./keyOnly0.pkl', './keyOnly1.pkl', './keyOnly2.pkl', './keyOnly3.pkl']
    firstdict = file_locales[0]
    with open(firstdict, 'rb') as f:
        firstdict:dict = pic.load(f)

    with open('end_ret.pkl','wb') as f:
        pic.dump(firstdict, f)

    print("end")