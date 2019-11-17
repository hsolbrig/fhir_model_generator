#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/OperationDefinition) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .usagecontext import UsageContext


@dataclass
class OperationDefinitionParameterBinding(BackboneElement):
    """ ValueSet details if this is coded.

    Binds to a value set if this parameter is coded (code, Coding,
    CodeableConcept).
    """
    resource_type: ClassVar[str] = "OperationDefinitionParameterBinding"

    strength: str = None
    valueSetUri: str = field(default=None, metadata=dict(one_of_many='valueSet',))
    valueSetReference: FHIRReference = field(default=None, metadata=dict(one_of_many='valueSet',))


@dataclass
class OperationDefinitionParameter(BackboneElement):
    """ Parameters for the operation/query.

    The parameters for the operation/query.
    """
    resource_type: ClassVar[str] = "OperationDefinitionParameter"

    name: str = None
    use: str = None
    min: int = None
    max: str = None
    documentation: Optional[str] = None
    type: Optional[str] = None
    searchType: Optional[str] = None
    profile: Optional[FHIRReference] = None
    binding: Optional[OperationDefinitionParameterBinding] = None
    part: Optional[List["OperationDefinitionParameter"]] = None


@dataclass
class OperationDefinitionOverload(BackboneElement):
    """ Define overloaded variants for when  generating code.

    Defines an appropriate combination of parameters to use when invoking this
    operation, to help code generators when generating overloaded parameter
    sets for this operation.
    """
    resource_type: ClassVar[str] = "OperationDefinitionOverload"

    parameterName: Optional[List[str]] = None
    comment: Optional[str] = None


@dataclass
class OperationDefinition(DomainResource):
    """ Definition of an operation or a named query.

    A formal computable definition of an operation (on the RESTful interface)
    or a named query (using the search interaction).
    """
    resource_type: ClassVar[str] = "OperationDefinition"

    url: Optional[str] = None
    version: Optional[str] = None
    name: str = None
    status: str = None
    kind: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    purpose: Optional[str] = None
    idempotent: Optional[bool] = None
    code: str = None
    comment: Optional[str] = None
    base: Optional[FHIRReference] = None
    resource: Optional[List[str]] = None
    system: bool = None
    type: bool = None
    instance: bool = None
    parameter: Optional[List[OperationDefinitionParameter]] = None
    overload: Optional[List[OperationDefinitionOverload]] = None