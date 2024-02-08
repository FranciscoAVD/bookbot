

def getWordDic(file_contents):
    dict = {}
    for i in range(0,len(file_contents)):
        if file_contents[i] in dict:
            dict[file_contents[i]] += 1
        else:
            if file_contents[i].isalpha():
                dict[file_contents[i]] = 1
    return dict

def sortedList(dict):
    sorted = []
    for ch in dict:
        sorted.append({"char": ch, "num": dict[ch]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

def sort_on(d):
    return d["num"]

def get_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents.lower()
def format(list):
    for o in list:
        print(f"The '{o["char"]}' character was found {o["num"]} times")
def main():
    content = get_text()
    dict = getWordDic(content)
    sorted = sortedList(dict)
    format(sorted)

main()