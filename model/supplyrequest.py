#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/SupplyRequest) on 2019-11-17.
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
from .quantity import Quantity
from .timing import Timing


@dataclass
class SupplyRequestOrderedItem(BackboneElement):
    """ The item being requested.
    """
    resource_type: ClassVar[str] = "SupplyRequestOrderedItem"

    quantity: Quantity = None
    itemCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='item',))
    itemReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='item',))


@dataclass
class SupplyRequestRequester(BackboneElement):
    """ Who/what is requesting service.

    The individual who initiated the request and has responsibility for its
    activation.
    """
    resource_type: ClassVar[str] = "SupplyRequestRequester"

    agent: FHIRReference = None
    onBehalfOf: Optional[FHIRReference] = None


@dataclass
class SupplyRequest(DomainResource):
    """ Request for a medication, substance or device.

    A record of a request for a medication, substance or device used in the
    healthcare setting.
    """
    resource_type: ClassVar[str] = "SupplyRequest"

    identifier: Optional[Identifier] = None
    status: Optional[str] = None
    category: Optional[CodeableConcept] = None
    priority: Optional[str] = None
    orderedItem: Optional[SupplyRequestOrderedItem] = None
    occurrenceDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrencePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrenceTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='occurrence',))
    authoredOn: Optional[FHIRDate] = None
    requester: Optional[SupplyRequestRequester] = None
    supplier: Optional[List[FHIRReference]] = None
    reasonCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='reason',))
    reasonReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='reason',))
    deliverFrom: Optional[FHIRReference] = None
    deliverTo: Optional[FHIRReference] = None