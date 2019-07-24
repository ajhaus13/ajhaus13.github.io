from jinja2 import Environment, FileSystemLoader

ENVIRONMENT = Environment(
    loader=FileSystemLoader('./')
)

with open("index.html", "w") as html:
    output = ENVIRONMENT.get_template('template.html').render()
    html.write(output)
