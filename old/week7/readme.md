# Week 7 - More Python

## Exercises

This week, we're going to do a number of exercises to get better at Python.

### Exercise 1 - What language should I use?

When going on a trip, it's important to know which languages are used in whichever countries you're going to. We're going to make a simple program to tell someone which language they should learn before going somewhere.

For now we're only going to worry about a few countries:

 - Australia - English
 - Britain - English
 - Germany - German
 - Japan - Japanese
 - Croatia - Croatian

We're going to use `input()` to get the country that the person is going to, and then use `print()` to display the language the country speaks.

```py
country = input("Which country are you visiting? ")

if country == "Australia":
    print("English")
else:
    print("Not sure...")
```

### Exercise 2 - What timezone will I be in?

Flying somewhere else also means changing timezones. Below we have an array (shelf) of timezones, and an array of countries, both in the same order:

```py
timezones = ["GMT 10+","GMT 1+","GMT 2+","GMT 8+","GMT 2+"]
countries = ["Australia" ,"Britain" ,"Germany" ,"Japan" ,"Croatia"]
```

and a piece of code that tells you the index of an item in an array:

```py
def indexOf(array,value): #Take an array, and a value to search for
    try:
        return array.index(value) #Try to return the index
    except:
        return -1 #If that fails, return -1
```

using these two things, try to write a piece of code that takes a country as input, then tells you which timezone it is in.

For example,

```py
country: Australia
GMT 10+

country: Croatia
GMT 2+

country: Japan
GMT 8+
```

#### Hint

Here, the two arrays are associative.

`"Australia"`, the first element in the `countries` array, is in the timezone `GMT 10+`, which is the first element in the `timezones` array.

Similarly `"Croatia"` is the `5th` element in the `countries` array, and the `5th` element of `timezones` is `"GMT 2+"`.

### Exercise 3 - What time is it back home?

When overseas, it's important to remember that the people back at home are still in your home timezone, otherwise if you try to text them you might wake them up, or disturb them while they're doing important stuff.

Using the timezones again, we're going to write a program that asks the user which country they're visiting, and where they're from, then the current hour (in 24 hour format), then tell them what time it is in their home country.

```py
def indexOf(array,value): #Take an array, and a value to search for
    try:
        return array.index(value) #Try to return the index
    except:
        return -1 #If that fails, return -1


timezones = [10,1,2,8,2]
countries = ["Australia" ,"Britain" ,"Germany" ,"Japan" ,"Croatia"]

visitingcountry = input("Which country are you visiting? ")
homecountry = input("Where is your home country? ")
time = input("What hour is it? ")
```

#### Hint

When it is `10` (10am) in Australia, it's `1` (1am) in Britain, and when it's `12` (12pm) in Japan, it's `14` (2pm) in Australia.

You can get the time difference between two countries with simple subtraction - in the above examples:

```
it's 10 in Australia

Australia is 10+
Britain is 1+

The difference between the two is 10 - 1
 = 9

The time in Britain is the time in Australia - the difference

The time in Britain is 10 - 9
 = 1
```

The only other issue is that, say it's 23 (11pm) in Britain, and we want to know the time in Australia:

```
23 in Britain.

Britain is 1+
Australia is 10+

The difference is 1 - 10
 = -9

The time in Australia is the time in Britain - the difference

The time in Australia is 23 - (- 9)
 = 32
```

Obviously, 32 is not a legitimate time, so we have to use a maths operation we have talked about before - Modulu (remainder).

We also have to use `int()` to convert out input into a number.

### Extention - Pyramids

An example of something great you can see while travelling is a pyramid, and as a _leet coder_ you want to have some way of remembering them. Not every pyramid is the same size though, so you decide to write a program that can make pyramids of any size.

#### Part 1

To get started, you write a program that takes an input (the number of layers), then simply displays a staircase made of stars, eg., for the number 5:

```
Enter height: 5

*
**
***
****
*****
```

This program will need a loop, and the use of a special thing in Python.

Try typing the code:
```py
print("*"*5)
```

Notice that it produces:

```
*****
```

This is important for this task.

Similarly try:

```py
for i in range(1,6):
    print(i)
```

That should produce:

```
1
2
3
4
5
```

Try to figure out how to do the staircase by yourself.

#### Part 2

Unsatisfied with a left aligned staircase, you set your sights higher - or rather wider. Pyramids don't look like a right-angled triangle made of stars stuck to the left of a computer screen. Everything's wrong!

You want your pyramids to look like this:

```
Enter height: 3

    *
  *****
*********
```

```
Enter height: 4

      *
    *****
  *********
*************
```

To explain this a little further:

```
+---------+-----------+------------+
|     line|     # of *| # of spaces|
|---------+-----------+------------|
|        1|          1|           6|
|        2|          5|           4|
|        3|          9|           2|
|        4|         13|           0|
+---------+-----------+------------+
```