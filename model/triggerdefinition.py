#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/TriggerDefinition) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .datarequirement import DataRequirement
from .element import Element
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .timing import Timing


@dataclass
class TriggerDefinition(Element):
    """ Defines an expected trigger for a module.

    A description of a triggering event.
    """
    resource_type: ClassVar[str] = "TriggerDefinition"

    type: str = None
    eventName: Optional[str] = None
    eventTimingTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='eventTiming',))
    eventTimingReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='eventTiming',))
    eventTimingDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='eventTiming',))
    eventTimingDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='eventTiming',))
    eventData: Optional[DataRequirement] = None