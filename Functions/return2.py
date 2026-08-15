# another example of return

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("john", "doe")

print(full_name)
# output - John Doe (first letter will be capitalize)
