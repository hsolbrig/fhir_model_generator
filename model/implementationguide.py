#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/ImplementationGuide) on 2019-11-17.
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
class ImplementationGuidePackageResource(BackboneElement):
    """ Resource in the implementation guide.

    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """
    resource_type: ClassVar[str] = "ImplementationGuidePackageResource"

    example: bool = None
    name: Optional[str] = None
    description: Optional[str] = None
    acronym: Optional[str] = None
    sourceUri: str = field(default=None, metadata=dict(one_of_many='source',))
    sourceReference: FHIRReference = field(default=None, metadata=dict(one_of_many='source',))
    exampleFor: Optional[FHIRReference] = None


@dataclass
class ImplementationGuideDependency(BackboneElement):
    """ Another Implementation guide this depends on.

    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDependency"

    type: str = None
    uri: str = None


@dataclass
class ImplementationGuidePackage(BackboneElement):
    """ Group of resources as used in .page.package.

    A logical group of resources. Logical groups can be used when building
    pages.
    """
    resource_type: ClassVar[str] = "ImplementationGuidePackage"

    name: str = None
    description: Optional[str] = None
    resource: List[ImplementationGuidePackageResource] = field(default_factory=list)


@dataclass
class ImplementationGuideGlobal(BackboneElement):
    """ Profiles that apply globally.

    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """
    resource_type: ClassVar[str] = "ImplementationGuideGlobal"

    type: str = None
    profile: FHIRReference = None


@dataclass
class ImplementationGuidePage(BackboneElement):
    """ Page/Section in the Guide.

    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """
    resource_type: ClassVar[str] = "ImplementationGuidePage"

    source: str = None
    title: str = None
    kind: str = None
    type: Optional[List[str]] = None
    package: Optional[List[str]] = None
    format: Optional[str] = None
    page: Optional[List["ImplementationGuidePage"]] = None


@dataclass
class ImplementationGuide(DomainResource):
    """ A set of rules about how FHIR is used.

    A set of rules of how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide into a
    logical whole and to publish a computable definition of all the parts.
    """
    resource_type: ClassVar[str] = "ImplementationGuide"

    url: str = None
    version: Optional[str] = None
    name: str = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    copyright: Optional[str] = None
    fhirVersion: Optional[str] = None
    dependency: Optional[List[ImplementationGuideDependency]] = None
    package: Optional[List[ImplementationGuidePackage]] = None
    global_fhir: Optional[List[ImplementationGuideGlobal]] = field(default_factory=list, metadata=dict(orig_name='global'))
    binary: Optional[List[str]] = None
    page: Optional[ImplementationGuidePage] = None