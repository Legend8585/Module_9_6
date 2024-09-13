def all_variants(text):
    for start in range(len(text)):
        variant = ""
        for end in range(start, len(text)):
            variant += text[end]
            yield variant

##Пример работы функции:
a = all_variants("abc")
for i in a:
    print(i)
