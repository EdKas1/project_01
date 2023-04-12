# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    dtr = s.replace("!", "")
    return dtr
print(remove_exclamation_marks("Nothing!!!!!!"))
# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    str = s.rstrip("!")
    return str
print(remove_last_em("Hi! Hello!!!"))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"


## Буду рад увидеть от вас более лаконичное решение)
def remove_word_with_one_em(s):
    s1 = s.split()
    res = []
    aa = "!"
    xxx = 0
    for x in s1:
        if aa in x:
            for aa in x:
                xxx+=1
                if xxx != 1:
                    continue 
                else:
                    res.append(x)

        else:
            res.append(x)   
        
    return " ".join(res)
print(remove_word_with_one_em("Hi!! Hi Hi! Hi !Hi!"))

### удалил слово, содержащее "!"
def remove_word_with_them(s):
    s1 = s.split()
    res = []
    aa = "!"
    for x in s1:
        if aa in x:
            continue
        else:
            res.append(x)
    return " ".join(res)
print(remove_word_with_them("Hi! Hi Hi! Hi !Hi! !Hi"))