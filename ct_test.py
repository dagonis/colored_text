from colored_text import colored_text as ct

print(ct("*", "red")*15)
print(ct("Test", "blue"))
print(ct("*", "green")*15)
print(ct("Test", "h_red"))
name = "Bob"
print(ct("Hello, my name is {}!".format(name), "magenta"))
print(ct("Hello, my name is %s!" % name, "cyan"))