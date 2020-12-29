# First-class functions allow to use functions as objects, e.g., return them as another function's return value or just pass functions around as arguments.
# For example:

def square(x):
    return x*x

def cube(x):
    return x**3

def process(f, args):
    for x in args:
        print( "{}({}) = {}".format(f.__name__,x, f(x)) )

process( square, [1,2,3,4,5,6,7,8,9,10])
process( cube, [1,2,3,4,5,6,7,8,9,10])

# We can also implement a simple HTML DSL using this functions :D
def html_tag(tag):
    def wrap(*text_elements):
        n_elements = len(text_elements)
        content = ""
        for index,element in enumerate(text_elements):
            content += element
            if n_elements > 1 and index < n_elements -1:
                content += "\n"

        return "<{0}>{1}</{0}>".format(tag,content)

    return wrap

# Simple HTML DSL 
html = html_tag("html")
head = html_tag("head")
head_title = html_tag( "title" )
body = html_tag("body")

h1 = html_tag("h1")
p = html_tag( "p")

# Render a page!
my_page = html(
    head(
        head_title("Hello, world!")
    ),
    body(
        h1( "This is my Python DSL for HTML!" ),
        p( "Really cool!" ),
        p( "You can really append everything")
    )
)

print( my_page )