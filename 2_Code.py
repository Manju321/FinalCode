"""Using Python 3.6

Ans for 2nd

Write a program to reverse a string “abcdef” --> “fedcba”
"""



def reverse(text):

    lst = []
    count = 1

    for i in range(0,len(text)):

        lst.append(text[len(text)-count])
        count += 1

    lst = ''.join(lst)
    return lst

print(reverse("abcdef"))
