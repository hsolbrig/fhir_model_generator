#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/CapabilityStatement2) on 2019-11-18.
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
class CapabilityStatement2RestResourceInteraction(BackboneElement):
    """ What operations are supported?.

    Identifies a restful operation supported by the solution.
    """
    resource_type: ClassVar[str] = "CapabilityStatement2RestResourceInteraction"

    code: str = None
    documentation: Optional[str] = None


@dataclass
class CapabilityStatement2RestResourceSearchParam(BackboneElement):
    """ Search parameters supported by implementation.

    Search parameters for implementations to support and/or make use of -
    either references to ones defined in the specification, or additional ones
    defined for/by the implementation.
    """
    resource_type: ClassVar[str] = "CapabilityStatement2RestResourceSearchParam"

    name: str = None
    definition: Optional[str] = None
    type: str = None
    documentation: Optional[str] = None


@dataclass
class CapabilityStatement2RestResourceOperation(BackboneElement):
    """ Definition of a resource operation.

    Definition of an operation or a named query together with its parameters
    and their meaning and type. Consult the definition of the operation for
    details about how to invoke the operation, and the parameters.
    """
    resource_type: ClassVar[str] = "CapabilityStatement2RestResourceOperation"

    name: str = None
    definition: str = None
    documentation: Optional[str] = None


@dataclass
class CapabilityStatement2RestResource(BackboneElement):
    """ Resource served on the REST interface.

    A specification of the restful capabilities of the solution for a specific
    resource type.
    """
    resource_type: ClassVar[str] = "CapabilityStatement2RestResource"

    type: str = None
    profile: Optional[str] = None
    supportedProfile: Optional[List[str]] = None
    documentation: Optional[str] = None
    interaction: Optional[List[CapabilityStatement2RestResourceInteraction]] = None
    searchParam: Optional[List[CapabilityStatement2RestResourceSearchParam]] = None
    operation: Optional[List[CapabilityStatement2RestResourceOperation]] = None


@dataclass
class CapabilityStatement2RestInteraction(BackboneElement):
    """ What operations are supported?.

    A specification of restful operations supported by the system.
    """
    resource_type: ClassVar[str] = "CapabilityStatement2RestInteraction"

    code: str = None
    documentation: Optional[str] = None


@dataclass
class CapabilityStatement2Software(BackboneElement):
    """ Software that is covered by this capability statement.

    Software that is covered by this capability statement.  It is used when the
    capability statement describes the capabilities of a particular software
    version, independent of an installation.
    """
    resource_type: ClassVar[str] = "CapabilityStatement2Software"

    name: str = None
    version: Optional[str] = None
    releaseDate: Optional[FHIRDate] = None


@dataclass
class CapabilityStatement2Implementation(BackboneElement):
    """ If this describes a specific instance.

    Identifies a specific implementation instance that is described by the
    capability statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """
    resource_type: ClassVar[str] = "CapabilityStatement2Implementation"

    description: str = None
    url: Optional[str] = None
    custodian: Optional[FHIRReference] = None


@dataclass
class CapabilityStatement2Rest(BackboneElement):
    """ If the endpoint is a RESTful one.

    A definition of the restful capabilities of the solution, if any.
    """
    resource_type: ClassVar[str] = "CapabilityStatement2Rest"

    mode: str = None
    documentation: Optional[str] = None
    resource: Optional[List[CapabilityStatement2RestResource]] = None
    interaction: Optional[List[CapabilityStatement2RestInteraction]] = None
    searchParam: Optional[List[CapabilityStatement2RestResourceSearchParam]] = None
    operation: Optional[List[CapabilityStatement2RestResourceOperation]] = None
    compartment: Optional[List[str]] = None


@dataclass
class CapabilityStatement2(DomainResource):
    """ A statement of system capabilities.

    A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server for a particular version of FHIR that may be used as a
    statement of actual server functionality or a statement of required or
    desired server implementation.
    """
    resource_type: ClassVar[str] = "CapabilityStatement2"

    url: Optional[str] = None
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: FHIRDate = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    purpose: Optional[str] = None
    copyright: Optional[str] = None
    kind: str = None
    instantiates: Optional[List[str]] = None
    imports: Optional[List[str]] = None
    software: Optional[CapabilityStatement2Software] = None
    implementation: Optional[CapabilityStatement2Implementation] = None
    fhirVersion: str = None
    format: List[str] = field(default_factory=list)
    patchFormat: Optional[List[str]] = None
    implementationGuide: Optional[List[str]] = None
    rest: Optional[List[CapabilityStatement2Rest]] = None