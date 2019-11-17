#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/DataElement) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .elementdefinition import ElementDefinition
from .fhirdate import FHIRDate
from .identifier import Identifier
from .usagecontext import UsageContext


@dataclass
class DataElementMapping(BackboneElement):
    """ External specification mapped to.

    Identifies a specification (other than a terminology) that the elements
    which make up the DataElement have some correspondence with.
    """
    resource_type: ClassVar[str] = "DataElementMapping"

    identity: str = None
    uri: Optional[str] = None
    name: Optional[str] = None
    comment: Optional[str] = None


@dataclass
class DataElement(DomainResource):
    """ Resource data element.

    The formal description of a single piece of information that can be
    gathered and reported.
    """
    resource_type: ClassVar[str] = "DataElement"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    copyright: Optional[str] = None
    stringency: Optional[str] = None
    mapping: Optional[List[DataElementMapping]] = None
    element: List[ElementDefinition] = field(default_factory=list)