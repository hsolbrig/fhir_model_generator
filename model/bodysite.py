#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/BodySite) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class BodySite(DomainResource):
    """ Specific and identified anatomical location.

    Record details about the anatomical location of a specimen or body part.
    This resource may be used when a coded concept does not provide the
    necessary detail needed for the use case.
    """
    resource_type: ClassVar[str] = "BodySite"

    identifier: Optional[List[Identifier]] = None
    active: Optional[bool] = None
    code: Optional[CodeableConcept] = None
    qualifier: Optional[List[CodeableConcept]] = None
    description: Optional[str] = None
    image: Optional[List[Attachment]] = None
    patient: FHIRReference = None