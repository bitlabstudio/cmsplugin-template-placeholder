"""Templatetags for the pyconsg2 project."""
from django import template
from django.template import Template
from django.template.defaultfilters import safe

from classytags.arguments import Argument, MultiValueArgument
from cms.templatetags.cms_tags import Placeholder, PlaceholderOptions


register = template.Library()


class PlaceholderAs(Placeholder):
    """
    Assignment tag version of the original Placeholder tag.

    Also calls Django's templating engine on the placeholder content so that
    you can use any tag and filter in your placeholder content.

    Usage::

        {% load cmsplugin_template_placeholder_tags %}
        {% placeholder_as "placeholder_name" as output %}
        {{ output }}

    """
    name = 'placeholder_as'
    options = PlaceholderOptions(
        Argument('name', resolve=False),
        MultiValueArgument('extra_bits', required=False, resolve=False),
        'as',
        Argument('varname', resolve=False),
        blocks=[
            ('endplaceholder', 'nodelist'),
        ],
    )

    def render_tag(self, context, name, extra_bits, varname):
        output = super(PlaceholderAs, self).render_tag(
            context, name, extra_bits)
        output_template = Template(safe(output))
        output_rendered = output_template.render(context)
        if varname:
            context[varname] = output_rendered
            return ''
        return output_rendered
register.tag(PlaceholderAs)
