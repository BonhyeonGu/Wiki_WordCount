import pickle as pic

if __name__ == "__main__":
    file_locales = ['./keyOnly0_ret.pkl', './keyOnly1_ret.pkl', './keyOnly2_ret.pkl', './keyOnly3_ret.pkl', './keyOnly4_ret.pkl']
    firstDict = file_locales[0]
    with open(firstDict, 'rb') as f:
        firstDict:dict = pic.load(f)
    
    for file_locale in file_locales:
        with open(file_locale, 'rb') as f:
            tmpDict:dict = pic.load(f)
        firstDict.update(tmpDict)

    with open('wordCount.pkl','wb') as f:
        pic.dump(firstDict, f)

    print("end")