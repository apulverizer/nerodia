import six

from .html_element import HTMLElement
from ..meta_elements import MetaHTMLElement


@six.add_metaclass(MetaHTMLElement)
class Area(HTMLElement):
    _attr_href = (str, 'href')
