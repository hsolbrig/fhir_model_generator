#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/ProcessRequest) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class ProcessRequestItem(BackboneElement):
    """ Items to re-adjudicate.

    List of top level items to be re-adjudicated, if none specified then the
    entire submission is re-adjudicated.
    """
    resource_type: ClassVar[str] = "ProcessRequestItem"

    sequenceLinkId: int = None


@dataclass
class ProcessRequest(DomainResource):
    """ Request to perform some action on or in regards to an existing resource.

    This resource provides the target, request and response, and action details
    for an action to be performed by the target on or about existing resources.
    """
    resource_type: ClassVar[str] = "ProcessRequest"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    action: Optional[str] = None
    target: Optional[FHIRReference] = None
    created: Optional[FHIRDate] = None
    provider: Optional[FHIRReference] = None
    organization: Optional[FHIRReference] = None
    request: Optional[FHIRReference] = None
    response: Optional[FHIRReference] = None
    nullify: Optional[bool] = None
    reference: Optional[str] = None
    item: Optional[List[ProcessRequestItem]] = None
    include: Optional[List[str]] = None
    exclude: Optional[List[str]] = None
    period: Optional[Period] = None