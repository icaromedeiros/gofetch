def render():
    pass

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('gofetch', 'templates'))
