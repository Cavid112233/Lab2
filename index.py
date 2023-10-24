def hasili_hesabla(arr):
    hasil = 1
    for element in arr:
        if element > 9:
            hasil *= element
    return hasil


B = [5, 10, 3, 15, 8, 7, 20]


hasili = hasili_hesabla(B)


print("9-dan boyuk elementlerin hasili:", hasili)
