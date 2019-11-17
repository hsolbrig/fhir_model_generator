#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Library) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .contributor import Contributor
from .datarequirement import DataRequirement
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .identifier import Identifier
from .parameterdefinition import ParameterDefinition
from .period import Period
from .relatedartifact import RelatedArtifact
from .usagecontext import UsageContext


@dataclass
class Library(DomainResource):
    """ Represents a library of quality improvement components.

    The Library resource is a general-purpose container for knowledge asset
    definitions. It can be used to describe and expose existing knowledge
    assets such as logic libraries and information model descriptions, as well
    as to describe a collection of knowledge assets.
    """
    resource_type: ClassVar[str] = "Library"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    type: CodeableConcept = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    description: Optional[str] = None
    purpose: Optional[str] = None
    usage: Optional[str] = None
    approvalDate: Optional[FHIRDate] = None
    lastReviewDate: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    topic: Optional[List[CodeableConcept]] = None
    contributor: Optional[List[Contributor]] = None
    contact: Optional[List[ContactDetail]] = None
    copyright: Optional[str] = None
    relatedArtifact: Optional[List[RelatedArtifact]] = None
    parameter: Optional[List[ParameterDefinition]] = None
    dataRequirement: Optional[List[DataRequirement]] = None
    content: Optional[List[Attachment]] = None