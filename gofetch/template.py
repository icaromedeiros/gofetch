from jinja2 import Environment, PackageLoader,\
    Template, TemplateNotFound

jinja_env = Environment(loader=PackageLoader('gofetch', 'templates'))


def render(template_str_or_file, param_dict):
    try:
        template = jinja_env.get_template()
        return _render_file_template(template, param_dict)
    except TemplateNotFound:
        # TODO valid template string?
        return _render_string_template(template_str_or_file, param_dict)


def _render_string_template(template_str, param_dict):
    # TODO log
    tmplt = Template(template_str)
    return _do_render(tmplt, param_dict)


def _render_file_template(template_obj, param_dict):
    # TODO log
    return _do_render(template_obj, param_dict)


def _do_render(template_obj, param_dict):
    return template_obj.render(**param_dict)
