from jinja2 import Environment, FileSystemLoader
import yaml

ENVIRONMENT = Environment(
    loader=FileSystemLoader('./')
)

with open("index.html", "w") as html:
    output = ENVIRONMENT.get_template('template.html').render(yaml.load(open('configs.yml'),Loader=yaml.Loader))
    html.write(output)
