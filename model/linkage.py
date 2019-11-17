#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Linkage) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .domainresource import DomainResource
from .fhirreference import FHIRReference


@dataclass
class LinkageItem(BackboneElement):
    """ Item to be linked.

    Identifies one of the records that is considered to refer to the same real-
    world occurrence as well as how the items hould be evaluated within the
    collection of linked items.
    """
    resource_type: ClassVar[str] = "LinkageItem"

    type: str = None
    resource: FHIRReference = None


@dataclass
class Linkage(DomainResource):
    """ Links records for 'same' item.

    Identifies two or more records (resource instances) that are referring to
    the same real-world "occurrence".
    """
    resource_type: ClassVar[str] = "Linkage"

    active: Optional[bool] = None
    author: Optional[FHIRReference] = None
    item: List[LinkageItem] = field(default_factory=list)