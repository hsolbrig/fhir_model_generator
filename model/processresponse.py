#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/ProcessResponse) on 2019-11-17.
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


@dataclass
class ProcessResponseProcessNote(BackboneElement):
    """ Processing comments or additional requirements.

    Suite of processing notes or additional requirements if the processing has
    been held.
    """
    resource_type: ClassVar[str] = "ProcessResponseProcessNote"

    type: Optional[CodeableConcept] = None
    text: Optional[str] = None


@dataclass
class ProcessResponse(DomainResource):
    """ ProcessResponse resource.

    This resource provides processing status, errors and notes from the
    processing of a resource.
    """
    resource_type: ClassVar[str] = "ProcessResponse"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    created: Optional[FHIRDate] = None
    organization: Optional[FHIRReference] = None
    request: Optional[FHIRReference] = None
    outcome: Optional[CodeableConcept] = None
    disposition: Optional[str] = None
    requestProvider: Optional[FHIRReference] = None
    requestOrganization: Optional[FHIRReference] = None
    form: Optional[CodeableConcept] = None
    processNote: Optional[List[ProcessResponseProcessNote]] = None
    error: Optional[List[CodeableConcept]] = None
    communicationRequest: Optional[List[FHIRReference]] = None