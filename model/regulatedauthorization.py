#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/RegulatedAuthorization) on 2019-11-18.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class RegulatedAuthorizationRelatedDate(BackboneElement):
    """ Other dates associated with the authorization. It is common for an
    authorization to have renewal dates, initial time limited phases and so on.
    """
    resource_type: ClassVar[str] = "RegulatedAuthorizationRelatedDate"

    datePeriod: Period = field(default=None, metadata=dict(one_of_many='date',))
    dateDateTime: FHIRDate = field(default=None, metadata=dict(one_of_many='date',))
    type: CodeableConcept = None


@dataclass
class RegulatedAuthorizationCase(BackboneElement):
    """ The case or regulatory procedure for granting or amending a marketing
    authorization.
    """
    resource_type: ClassVar[str] = "RegulatedAuthorizationCase"

    identifier: Optional[Identifier] = None
    type: Optional[CodeableConcept] = None
    status: Optional[CodeableConcept] = None
    datePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='date',))
    dateDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='date',))
    application: Optional[List["RegulatedAuthorizationCase"]] = None


@dataclass
class RegulatedAuthorization(DomainResource):
    """ The regulatory authorization of a medicinal product.
    """
    resource_type: ClassVar[str] = "RegulatedAuthorization"

    identifier: Optional[List[Identifier]] = None
    subject: Optional[FHIRReference] = None
    type: Optional[CodeableConcept] = None
    description: Optional[str] = None
    region: Optional[List[CodeableConcept]] = None
    status: Optional[CodeableConcept] = None
    statusDate: Optional[FHIRDate] = None
    validityPeriod: Optional[Period] = None
    basis: Optional[List[CodeableConcept]] = None
    relatedDate: Optional[List[RegulatedAuthorizationRelatedDate]] = None
    jurisdictionalAuthorization: Optional[List[FHIRReference]] = None
    holder: Optional[FHIRReference] = None
    regulator: Optional[FHIRReference] = None
    case: Optional[RegulatedAuthorizationCase] = None