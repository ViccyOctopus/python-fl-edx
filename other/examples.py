n = input("You are in the Lost Forest. Go left or right? ")
while n == "right":
    n = input("You are in the Lost Forest. Go left or right? ")
print("you got out of the Lost Forest!")

n = 0
while(n < 5):
    print(n)
    n = n + 1

Output: 0, 1, 2, 3, 4

for n in range(5):
    print(n)

Output: 0, 1, 2, 3, 4

mysum = 0
for i in range (7, 10):
    mysum += i
print(mysum)

mysum = 0
for i in range(5, 11, 2):
    mysum += i
print(mysum)

mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
print(mysum)

x=3
ans = 0
itersLeft = x
while (itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1
print(str(x) + "*" + str(x) + "=" + str(ans))

#This code squares the value of x by repietitive additon

x = int(input("Enter an integer: "))
ans = 0
while ans**3 < x:
    ans += 1
if ans**3 != x:
    print(str(x) + 'is not a perfect cube')
else:
    print("Cube root of " + str(x) + " is " + str(ans))


x = int(input("Enter an integer: "))
ans = 0
while ans**3 <abs(x):
    ans += 1
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = - ans
    print('Cube rot of ' + str(x) + ' is ' + str(ans))

cube = 8
for guess in range(cube + 1):
    if guess**3 == cube:
        print("Cube root of", cube, "is", guess.)



ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True
while ans**2 < x:
    ans += 1
if ans**2 == x:
    print("Square root of", x, "is", ans)
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking... did you mean", -x, "?")


s = "abc"

len(s) #evaluates to 3
s[0]   #evaluates to "a"
s[1]   #evaluates to "b"
s[2]   #evaluates to "c"
s[3]   #trying to index out of bounds, error

s = "abcdefgh"
s[::-1] -> evaluates to "hgfedcba"
s[3:6]  -> evaluates to "def"
s[-1]   -> evaluates to "h"

#strings are imumutable, meaning they cannot be modified
s = "hello"
s[0] = "y"  -> gives an error
s = "y" + s[1:]
#where the output is yellow


s = "abcdefgh"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("There is an i or u")

for char in s:
    if char == 'i' or char == 'u':
        print("There is an i or u")


cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print("Failed on cube root of", cube)
else:
    print(guess, 'is close to the cube root of', cube)


x = 25
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) > epsilon:
    print('low = ' + str(low) + 'high = ' + str(high) + "ans = " + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + 'is close to square root of ' + str(x))


if num < 0:
    isNeg = True
    num = abs(num)
else:
    is Neg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
if isNeg:
    result = '-' + result


def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ", " + firstName)
    else:
        print(firstName, Lastname)

printName('Victoria','Arzumanova', False)


def mult_iter(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

#Multiply a*b, which is the same as adding a to itself b times
#It subtracts b once, then adds a, subtracts b once, adds a
#Suppose you want to do 5 times 3
#b: 5 4 3 2  1  0
#a: 3 6 9 12 15


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

#the file circle.py contains
pi = 3.14159
def area(radius):
    return pi*(radius**2)
def circumference(radius):
    return 2*pi*(radius)

import circle
pi = 3
print(pi)
print(circle.pi)
print(circle.area(3))
print(circle.circumference(3))

This gives you:

3
3.14149
28.27431
18.84953999999998

from circle import *
print(pi)
print(area(3))


te = ()

t = (2, "one", 3)

t[0] #evaluates to 2

(2, "one", 3) + (5,6) #evaluates to (2, "one", 3, 5, 6)

t[1:2] # slices tuple, evaluates to ("one,")

t[1:3] #slices tuple, evaluates to ("one", 3)

t[1] = 4 #gives error, can't modify object


def quotient_and_remainder(x,y):
    q = x//y
    r = x%y
    return (q,r)
(quot, rem) = quotient_and_remainder(4,5)


a_list = [] # this is an empty list
b_list = [2, 'a', 4, True]
L = [2, 1, 3]

len(L)  #evaluates to 3
L[0] #evaluates to 2
L[2] + 1 #evaluates to 4
L[3] #gives an error

i = 2
L[i-1] #evaluates to 1 since L[1] = 1 from above

L[1] = 5
#L is now [2, 5, 3], this is how you can change the elements in a list



total = 0
    for i in range(len(L)):
        total += L[i]
    print(total)

total = 0
    for i in L:
        total += i
    print(total)

L1 = [2,1,3]
L2 = [4,5,6]
L3 = L1 + L2    #L3 is [2,1,3,4,5,6]
L1.extend([0,6])#mutated L1 to [2,1,3,0,6]

L = [2,1,3,6,3,7,0] #do below in order
L.remove(2)   #mutates L = [1,3,6,3,7,0]
L.remove(3)   #mutates L = [1,6,3,7,0]
del(L[1])     #mutates L = [1,3,7,0]
L.pop()      #returns 0 and mutates L = [1,3,7]


warm = ['red', 'yellow', 'orange']
hot = warm

#if you print warm or hot, you get the same thing

hot.append('pink')
print(hot)

#you get ['red', 'yellow', 'orange', 'pink]
#BUT, the same thing prints out for both warm and hot
#Now, let's look at a different case, these are different versions of the same set of strings

cool = ['blue', 'green', 'grey']
chill = ['blue', 'green', 'grey']

print(cool)
print(chill)
#gives the same answer, but they're not the same

chill[2] = 'blue'
print(cool)
# gives you ['blue', 'green', 'grey']
print(chill)
# gives you ['blue', 'green', 'blue']


cool = ['blue', 'green', 'grey']
chill = cool[:]
#this creates a copy, a clone of cool

chill.append('black')
print(chill)
#prints out ['blue', 'green', 'grey', 'black']

print(cool)
#prints out ['blue', 'green', 'grey']

This makes sense, they have not changed

warm = ['yellow', 'orange']
hot = ['red']
brightcolors = [warm]
#this gives you [['yellow', 'orange']]

brightcolors.append(hot)
print(brightcolors)
# this gives you [['yellow', 'orange'], ['red']]

hot.append('pink')
print(brightcolors)
#this gives you [['yellow', 'orange'], ['red', 'pink']]


def applyToEach(L, f):
    """assumes L is a list, f is a function
    mutates L by replacing each element, e
    of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])


my_dict = {}
grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}

grades['John']
#Outputs 'A+'

grades['Sylvan']
#Gives a KeyError

grades['Sylvan'] = 'A'
grades['Sylvan']
#Outputs 'A'


'John' in grades
#Outputs True

'Daniel' in grades
#Outputs False


del(grades'Ana')
grades
#Outputs {John':'A+', 'Denise':'A', 'Katy':'A', 'Sylvan':'A'}




#Code to analyze song lyrics, its going to count how many times a word shows up
#Then, find the word that occurs the most

def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict


def most_common_words(freqs):
    values = freqs.values()
    best = mas(values)
    words = []
    for k in freqs:
        if freqs[] == best:
            words.append(k)
    return (words, best)


def fib_efficient(n,d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

d = {1:1, 2:2}


def fib_efficient(n,d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

numFibCalls = 0
d = {1:1, 2:2}
print(fib_efficient(12,d))
print('function calls', numFibCalls)


class Coordinate(obejct):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"


print(c.distance(origin))
#this outputs to 5


c = Coordinate(3,4)
origin = Coordinate(0.0)
print(c.x)
#The c.x says, print out the x variable associated with c, giving you three.
print(origin.x)
#This gives you the x value of origin (0,0), which gives you 0.

print(isinstance(c, Coordinate))
#Outputs to True

class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self, other):
        numerNew = other.getDenom() * self.getNumer() \
            + other.getNumer() * self.getDenom)()
        denomNew = other.getDenom() * self.getDenom() \
        return fraction(numerNew, denomNew)
    def __sub__(self, other)
        numerNew = other.getDenom() * self.getNumer() \
            - other.getNumer() * self.getDenom)()
        denomNew = other.getDenom() * self.getDenom() \
        return fraction(numerNew, denomNew)


class intSet(object):
    def __init__(self):
        self.vals = []
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
    def member(self, e):
        return e in self.vals
    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + 'not found')
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'


class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname =""):
        self.name = newname
    def __str__(self):
        return "animal": + str(self.name) + ":" + str(self.age)

class Cat(animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.age)


jelly = Cat(1)
#Sets Jelly, the name of a Cat, to be 1 years old.

jelly.get_name()
#Does not output anything, jelly does not have a name yet.

jelly.set_name('JellyBelly')

jelly.get_name()
#Output: 'JellyBelly'
#Jelly now has a name, it is JellyBelly

print(jelly)
#Output: cat:JellyBelly:1

print(Animal.__str__(jelly))
#Output: animal:JellyBelly:1

blob = Animal(1)

print(blob)
#Output: animal.None:1

blob.set_name()

print(blob)
#Output: animal::1


class Rabbit(Animal):
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit:" + str(self.name) + ":" + str(self.age)

peter = Rabbit(5)

jelly.speak()
#Output: meow

peter.speak()
#Output: meep

blob.speak()
#Output: Error, because blob does not have his own category so it defaults to Animal, and Animal does not have a speak function


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self, other)
    #alternate way: diff = self.age - other.age
    diff = self.get_age() - other.get_age()
    if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
            print(self.name, "is", -diff, "years younger than", other.name)
    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)

eric = Person("eric", 45)

john = Person("john", 55)

eric.speak()
#Output: hello

eric.age_diff(john)
#Output: eric is 10 years younger than john

Person.age_diff(john, eric)
#Output: john is 10 years older than eric


import random

class Student(Person):
    def __init__(self, name, age, major=None)
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")
    ef __str__(self):
        return "student:" + str(self.name)+ ":" + str(self.age) + ":" + str(self.major)

eric = Person('Eric', 45)

fred = Student('Fred', 18, 'Course VI')

print(fred)
#Outputs student:Fred:18:Course VI
#It is different because it uses method from Student, not Person





class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1 = None, parent2 = None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag +=1
    def get_rid(self):
        return str(self.rid) .zfill(3)
        #the z.fill is a method on a string to pad the beginning with zeros for example, 001 not 1
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        return Rabbit(0, self, other)
        #where self is parent1, and other is the other parent
    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid \
            and self.parent2.rid == other.parent2.get_rid
        parents_opposite = self.parent2.rid == other.parent1.rid \
            and self.parent1.rid == other.parent2.get_rid
        return parents_same or parents_opposite


#The tag is used to give unique id to each new rabbit instance

peter = Rabbit(2)
peter.set_name('Peter')
hopsy = Rabbit(3)
hopsy.set_name('Hopsy')
cotton = Rabbit(1, peter, hopsy)
#here we're providing explicit arguments
cotton.set_name('Cottontail')

print(cotton)
#Output: animal:Cottontail:1

print(cotton.get_parent1())
#Output: animal:Peter:2

mopsy = peter + hopsy
mopsy.set_name('Mopsy')
print(mopsy.get_parent1())
#Output: animal:Peter:2

print(mopsy.get_parent2())
#Output: animal:Hopsy:3

print(mopsy == hopsy)
#Output: True
#Because their parents are the same


import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName - name.split(' ')[-1]
        #this last line here resembles the assumption that the last element in a name is a person's last name
    def getLastName(self):
        """return self's last name"""
        return self.lastName
    def __str__(self):
        """return self's name"""
        return self.name
    def setBirthday(self, month, day, year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)
    def getAge(self):
        """return's self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    def __lt__(self, other):
        """return True if the self's name is lexicographically less
        than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName



