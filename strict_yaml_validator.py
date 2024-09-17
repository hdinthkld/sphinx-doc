from yaml import safe_load
from pprint import pprint
from jinja2 import Template

with open("data/site1.yaml", "r") as yaml_file:
    parsed = safe_load(yaml_file)

with open("templates/sphinx_template.j2", "r") as template_file:
    template = template_file.read()

#template = """
#hostname {{site.id}}
#"""

data = parsed

#pprint(str(parsed["site"]["id"]))

j2_template = Template(template)
rendered_template = j2_template.render(data)

with open("docs/index.rst", "w") as sphinx_file:
    sphinx_file.write(rendered_template)

