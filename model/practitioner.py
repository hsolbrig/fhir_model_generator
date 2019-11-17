#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Practitioner) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .address import Address
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .humanname import HumanName
from .identifier import Identifier
from .period import Period


@dataclass
class PractitionerQualification(BackboneElement):
    """ Qualifications obtained by training and certification.
    """
    resource_type: ClassVar[str] = "PractitionerQualification"

    identifier: Optional[List[Identifier]] = None
    code: CodeableConcept = None
    period: Optional[Period] = None
    issuer: Optional[FHIRReference] = None


@dataclass
class Practitioner(DomainResource):
    """ A person with a  formal responsibility in the provisioning of healthcare or
    related services.

    A person who is directly or indirectly involved in the provisioning of
    healthcare.
    """
    resource_type: ClassVar[str] = "Practitioner"

    identifier: Optional[List[Identifier]] = None
    active: Optional[bool] = None
    name: Optional[List[HumanName]] = None
    telecom: Optional[List[ContactPoint]] = None
    address: Optional[List[Address]] = None
    gender: Optional[str] = None
    birthDate: Optional[FHIRDate] = None
    photo: Optional[List[Attachment]] = None
    qualification: Optional[List[PractitionerQualification]] = None
    communication: Optional[List[CodeableConcept]] = None