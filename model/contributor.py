#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/Contributor) on 2019-11-18.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .contactdetail import ContactDetail
from .element import Element


@dataclass
class Contributor(Element):
    """ Contributor information.

    A contributor to the content of a knowledge asset, including authors,
    editors, reviewers, and endorsers.
    """
    resource_type: ClassVar[str] = "Contributor"

    type: str = None
    name: str = None
    contact: Optional[List[ContactDetail]] = None