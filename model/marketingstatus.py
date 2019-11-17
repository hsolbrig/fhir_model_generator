#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/MarketingStatus) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .fhirdate import FHIRDate
from .period import Period


@dataclass
class MarketingStatus(BackboneElement):
    """ The marketing status describes the date when a medicinal product is
    actually put on the market or the date as of which it is no longer
    available.
    """
    resource_type: ClassVar[str] = "MarketingStatus"

    country: CodeableConcept = None
    jurisdiction: Optional[CodeableConcept] = None
    status: CodeableConcept = None
    dateRange: Period = None
    restoreDate: Optional[FHIRDate] = None