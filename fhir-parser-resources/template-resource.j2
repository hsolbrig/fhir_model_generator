#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR {{ info.version }} ({{ profile.url }}) on {{ info.date }}.
#  {{ info.year }}, SMART Health IT.

{%- set imported = {} %}
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list
{% set notspecial = 'Identifier' != classes[-1].name and 'Extension' != classes[-1].name and 'Element' != classes[-1].name %}{%- if notspecial %}{% for imp in imports %}{% if imp.module not in imported %}
from .{{ imp.module }} import {{ imp.name }}{% set _ = imported.update({imp.module: True}) %}
{%- endif %}{% endfor %}{%- endif %}

{%- for klass in classes[::-1] %}
{% if klass.superclass in imports and klass.superclass.module not in imported -%}
from .{{ klass.superclass.module }} import {{ klass.superclass.name }}
{% set _ = imported.update({klass.superclass.module: True}) %}
{% endif %}

@dataclass
class {{klass.name}}({{klass.superclass.name | default('object')}}):
    """ {{ klass.short|wordwrap(width=75, wrapstring="\n    ") }}.
{%- if klass.formal %}

    {{ klass.formal|wordwrap(width=75, wrapstring="\n    ") }}
{%- endif %}
    """
{%- if klass.resource_type %}
    resource_type: ClassVar[str] = "{{ klass.resource_type }}"
{%- endif %}


{%- for prop in klass.properties %}
{%- if notspecial and not prop.is_forward %}{% set pname = prop.class_name %}{% else %}{% set pname = '"' + prop.class_name + '"' %}{% endif %}
    {{prop.name}}:{%- if prop.is_array %}{%- if prop.nonoptional %} List[{{pname}}]{% else %} Optional[List[{{pname}}]]{%- endif %} = empty_list(){% else %}{%- if prop.nonoptional %} {{pname}}{% else %} Optional[{{pname}}]{%- endif %} = None{% endif %}

{%- endfor %}


{%- if klass.properties %}

    def elementProperties(self):
        {%- if not notspecial %}
        {%- for imp in imports %}{% if imp.module not in imported %}
        from .{{imp.module}} import {{imp.name}}{%- endif %}{% endfor %}
        {% endif %}
        js = super({{klass.name}}, self).elementProperties()
        js.extend([
        {%- for prop in klass.properties %}
            ("{{ prop.name }}", "{{ prop.orig_name }}", {{prop.class_name}}, {# #}
            {{- prop.is_array}},
            {%- if prop.one_of_many %} "{{ prop.one_of_many }}"{% else %} None{% endif %}, {# #}
            {{- prop.nonoptional}}),
        {%- endfor %}
        ])
        return js

{%- endif %}
{%- endfor %}
