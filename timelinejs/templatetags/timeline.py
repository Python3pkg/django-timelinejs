from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.inclusion_tag('timeline_template.html', takes_context=True)
def timeline(context, src=None, **config):
    if src is None:
        src = context['timeline'].pk
    if isinstance(src, int):
        config['src'] = '%s?format=json' % reverse('timelineview', kwargs={'pk':src})
    else:
        try:
            # `src` might be a string that can be coerced into a long
            config['src'] = '%s?format=json' % reverse('timelineview', kwargs={'pk': int(src)})
        except ValueError:
            config['src'] = src
    if 'options' in context:
        options = context['options']
        options.__dict__.update(config)
    else:
        options = config
    return {'context': context, 'config': options}
