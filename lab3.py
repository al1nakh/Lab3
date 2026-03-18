#lambda
#1.1
check=lambda x:"положительное" if x>0 else "отрицательное" if x <0 else"ноль"
print(check(5))
print(check(-3))
print(check(0))
#1.2
words=["арбуз", "кот", "машина", "дом", "ананас"]
sorted_words = sorted(words, key=lambda word : (len(word),word[0]))
print(sorted_words)
#1.3
numbers=[5,12,7,20,33,8]
result = list(filter(lambda x: x %2 == 0 and x >10, numbers))
print(result)
#1.4
numbers = [1,2,3,4,5,6]
result = list(map(lambda x: x**2 if x%2 ==0 else x*3,numbers))
print(result)
#1.5
compare = lambda a,b: "a больше" if a>b else "b больше" if b>a else "равны"
print(compare(10,7))
print(compare(3,5))
print(compare(4,4))
#1.6
numbers = [0, -3, 5, -7, 8]
result = [(lambda x: "positive" if x>0 else ("negative" if x<0 else "neutral")) for x in numbers]
print(result)
#2.1
def even_numbers(n):
    for x in range(1,1+n):
        if x % 2 == 0:
            if x %4 == 0:
                yield "kratno 4"
            else:
                yield x
for x in even_numbers(10):
    print(x)
#2.2
def filter_words(words):
    for word in words:
        if len(word) > 4:
            if "а" in word :
                yield "а с"
            else:
                yield word
words = ["кот", "машина", "арбуз", "дом"]
for w in filter_words(words):
    print(w)
#2.3
def infinite_numbers():
    x =1
    while True:
        if x % 3 == 0:
            yield "Fizz"
        elif x % 5 == 0:
            yield " Buzz"
        elif x % 3 == 0 and x % 5 == 0:
            yield "FizzBuzz"
        else :
            yield x
        x += 1
gen = infinite_numbers()
for _ in range(15):
    print(next(gen))
#2.4
def squares(n):
    for i in range(1, n+1):
        sq = i ** 2
        if sq % 2 ==0:
            yield "чётный квадрат"
        else :
            yield sq
for x in squares(5):
    print(x)
#3.1
eve_squares = [x**2 for x in range(1,21) if x % 2 ==0]
print(eve_squares)
#3.2
matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = lambda lst: lst[0] * result(lst[1:]) if lst else 1
row = [result(row) for row in matrix]
print(row)
#3.3
words =["кот", "машина", "ананас", "дом"]
result = [word for word in words if len(word)>4 and "а" not in word]
print(result)
#3.4
numbers = [1,2,3,4,5]
result = {n: "чётное" if n % 2 == 0 else "нечётное" for n in numbers}
print(result)
#3.5
matrix = [[1,2],[3,4],[5,6]]
result = [ num for row in matrix for num in row]
print(result)
#3.6
fizzbuzz =[
    "FizzBuzz" if x % 3 == 0 and x % 5 == 0 else
    "Fizz" if x % 3 == 0 else
    "Buzz" if x % 5 == 0 else
    x
    for x in range (1,21)
]
print(fizzbuzz)
#4.1
def is_prime(x):
    if x < 2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
def special_numbers(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 3 ==0 :
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        elif is_prime(i):
            yield "простое"
        else:
            yield i
for number in special_numbers(10):
    print(number)
#4.2
words = ["кот", "машина", "арбуз", "дом", "ананас"]
result = [
    (lambda w: (w.upper() if len(w)>4 else "short") + ("*" if "а" in w.lower() else ""))(word)
    for word in words
]
print(result)
#4.3
def process_numbers(numbers):
    filtered_nums= filter(lambda x: x >= 0,numbers)
    mapped_nums = map(lambda x: x /2 if x % 2 == 0 else x *3 +1, filtered_nums)
    for num in mapped_nums:
        if num == 0.0:
            yield 0
        else:
            yield num
numbers = [5,-2,8,0,-7,3]
for x in process_numbers(numbers):
    print(x)
#4.4
students = [("Иван", 85), ("Анна", 72), ("Пётр", 90), ("Мария", 60)]
grades = {
    name:(lambda s: "Отлично" if s >= 90 else "Хорошо" if s >= 70 else "Удовлетворительно")(score)
    for name, score in students
}
print(grades)
#4.5
def matrix_transform(matrix):
    yield from (
        "кратно 6" if x % 2 == 0 and x % 3 == 0 else
        "чётное" if x % 2 == 0 else
        "кратно 3" if x % 3 == 0 else
        x
        for row in matrix
        for x in row
    )
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for x in matrix_transform(matrix):
    print(x)
#5.1
numbers=[1,2,3,4,5]
doubled = list(map(lambda x: x*2, numbers))
print(doubled)
#5.2
words = ["кот", "машина", "арбуз", "дом"]
result = list(map(lambda w: w.upper() + ("!" if len(w) > 3 else ""),words))
print(result)
#5.3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x% 2 == 0,numbers))
print(evens)
#5.4
numbers = [0, 5, 12, 7, 20, -3, 8]
result = list (
    map(
        lambda x: x /2 if x % 2 == 0 else x * 3,
        filter(lambda x: x >5,numbers)
    )
)
print(result)