#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/DomainResource) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .extension import Extension
from .narrative import Narrative
from .resource import Resource


@dataclass
class DomainResource(Resource):
    """ A resource with narrative, extensions, and contained resources.

    A resource that includes narrative, extensions, and contained resources.
    """
    resource_type: ClassVar[str] = "DomainResource"

    text: Optional[Narrative] = None
    contained: Optional[List[Resource]] = None
    extension: Optional[List[Extension]] = None
    modifierExtension: Optional[List[Extension]] = None