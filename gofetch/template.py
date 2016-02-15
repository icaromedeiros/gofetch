from jinja2 import Environment, PackageLoader

jinja_env = Environment(loader=PackageLoader('gofetch', 'templates'))


def render(template_string_or_file, param_dict):
    pass
