#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/CompartmentDefinition) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .usagecontext import UsageContext


@dataclass
class CompartmentDefinitionResource(BackboneElement):
    """ How a resource is related to the compartment.

    Information about how a resource is related to the compartment.
    """
    resource_type: ClassVar[str] = "CompartmentDefinitionResource"

    code: str = None
    param: Optional[List[str]] = None
    documentation: Optional[str] = None


@dataclass
class CompartmentDefinition(DomainResource):
    """ Compartment Definition for a resource.

    A compartment definition that defines how resources are accessed on a
    server.
    """
    resource_type: ClassVar[str] = "CompartmentDefinition"

    url: str = None
    name: str = None
    title: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    purpose: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    code: str = None
    search: bool = None
    resource: Optional[List[CompartmentDefinitionResource]] = None