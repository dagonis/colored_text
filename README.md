colored_text
==============
A simple library that allows for printed colored text in python.

Usage
--------------
Usage is simple, I have included a test script.

I recommend doing "from colored_text import colored_text" or as I have below "from colored_text import colored_text as ct"

colored_text takes two arguments. The first is the string to print, the second is the color.

> from colored_text import colored_text as ct <br />
>  <br />
> print(ct("*", "red")*15) <br />
> print(ct("Test", "blue")) <br />
> print(ct("*", "green")*15) <br />
> print(ct("Test", "h_red")) <br />
> name = "Bob" <br />
> print(ct("Hello, my name is {}!".format(name), "magenta")) <br />
> print(ct("Hello, my name is %s!" % name, "cyan")) <br />