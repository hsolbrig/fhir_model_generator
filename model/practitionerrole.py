#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/PractitionerRole) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class PractitionerRoleAvailableTime(BackboneElement):
    """ Times the Service Site is available.

    A collection of times the practitioner is available or performing this role
    at the location and/or healthcareservice.
    """
    resource_type: ClassVar[str] = "PractitionerRoleAvailableTime"

    daysOfWeek: Optional[List[str]] = None
    allDay: Optional[bool] = None
    availableStartTime: Optional[FHIRDate] = None
    availableEndTime: Optional[FHIRDate] = None


@dataclass
class PractitionerRoleNotAvailable(BackboneElement):
    """ Not available during this time due to provided reason.

    The practitioner is not available or performing this role during this
    period of time due to the provided reason.
    """
    resource_type: ClassVar[str] = "PractitionerRoleNotAvailable"

    description: str = None
    during: Optional[Period] = None


@dataclass
class PractitionerRole(DomainResource):
    """ Roles/organizations the practitioner is associated with.

    A specific set of Roles/Locations/specialties/services that a practitioner
    may perform at an organization for a period of time.
    """
    resource_type: ClassVar[str] = "PractitionerRole"

    identifier: Optional[List[Identifier]] = None
    active: Optional[bool] = None
    period: Optional[Period] = None
    practitioner: Optional[FHIRReference] = None
    organization: Optional[FHIRReference] = None
    code: Optional[List[CodeableConcept]] = None
    specialty: Optional[List[CodeableConcept]] = None
    location: Optional[List[FHIRReference]] = None
    healthcareService: Optional[List[FHIRReference]] = None
    telecom: Optional[List[ContactPoint]] = None
    availableTime: Optional[List[PractitionerRoleAvailableTime]] = None
    notAvailable: Optional[List[PractitionerRoleNotAvailable]] = None
    availabilityExceptions: Optional[str] = None
    endpoint: Optional[List[FHIRReference]] = None