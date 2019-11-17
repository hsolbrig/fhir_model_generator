#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/ServiceDefinition) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .contributor import Contributor
from .datarequirement import DataRequirement
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .relatedartifact import RelatedArtifact
from .triggerdefinition import TriggerDefinition
from .usagecontext import UsageContext


@dataclass
class ServiceDefinition(DomainResource):
    """ A description of decision support service functionality.

    The ServiceDefinition describes a unit of decision support functionality
    that is made available as a service, such as immunization modules or drug-
    drug interaction checking.
    """
    resource_type: ClassVar[str] = "ServiceDefinition"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
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
    trigger: Optional[List[TriggerDefinition]] = None
    dataRequirement: Optional[List[DataRequirement]] = None
    operationDefinition: Optional[FHIRReference] = None