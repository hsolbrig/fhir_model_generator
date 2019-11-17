#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/ExpansionProfile) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .identifier import Identifier
from .usagecontext import UsageContext


@dataclass
class ExpansionProfileDesignationExcludeDesignation(BackboneElement):
    """ The designation to be excluded.

    A data group for each designation to be excluded.
    """
    resource_type: ClassVar[str] = "ExpansionProfileDesignationExcludeDesignation"

    language: Optional[str] = None
    use: Optional[Coding] = None


@dataclass
class ExpansionProfileDesignationIncludeDesignation(BackboneElement):
    """ The designation to be included.

    A data group for each designation to be included.
    """
    resource_type: ClassVar[str] = "ExpansionProfileDesignationIncludeDesignation"

    language: Optional[str] = None
    use: Optional[Coding] = None


@dataclass
class ExpansionProfileDesignationInclude(BackboneElement):
    """ Designations to be included.
    """
    resource_type: ClassVar[str] = "ExpansionProfileDesignationInclude"

    designation: Optional[List[ExpansionProfileDesignationIncludeDesignation]] = None


@dataclass
class ExpansionProfileDesignationExclude(BackboneElement):
    """ Designations to be excluded.
    """
    resource_type: ClassVar[str] = "ExpansionProfileDesignationExclude"

    designation: Optional[List[ExpansionProfileDesignationExcludeDesignation]] = None


@dataclass
class ExpansionProfileFixedVersion(BackboneElement):
    """ Fix use of a code system to a particular version.

    Fix use of a particular code system to a particular version.
    """
    resource_type: ClassVar[str] = "ExpansionProfileFixedVersion"

    system: str = None
    version: str = None
    mode: str = None


@dataclass
class ExpansionProfileExcludedSystem(BackboneElement):
    """ Systems/Versions to be exclude.

    Code system, or a particular version of a code system to be excluded from
    value set expansions.
    """
    resource_type: ClassVar[str] = "ExpansionProfileExcludedSystem"

    system: str = None
    version: Optional[str] = None


@dataclass
class ExpansionProfileDesignation(BackboneElement):
    """ When the expansion profile imposes designation contraints.

    A set of criteria that provide the constraints imposed on the value set
    expansion by including or excluding designations.
    """
    resource_type: ClassVar[str] = "ExpansionProfileDesignation"

    include: Optional[ExpansionProfileDesignationInclude] = None
    exclude: Optional[ExpansionProfileDesignationExclude] = None


@dataclass
class ExpansionProfile(DomainResource):
    """ Defines behaviour and contraints on the ValueSet Expansion operation.

    Resource to define constraints on the Expansion of a FHIR ValueSet.
    """
    resource_type: ClassVar[str] = "ExpansionProfile"

    url: Optional[str] = None
    identifier: Optional[Identifier] = None
    version: Optional[str] = None
    name: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    fixedVersion: Optional[List[ExpansionProfileFixedVersion]] = None
    excludedSystem: Optional[ExpansionProfileExcludedSystem] = None
    includeDesignations: Optional[bool] = None
    designation: Optional[ExpansionProfileDesignation] = None
    includeDefinition: Optional[bool] = None
    activeOnly: Optional[bool] = None
    excludeNested: Optional[bool] = None
    excludeNotForUI: Optional[bool] = None
    excludePostCoordinated: Optional[bool] = None
    displayLanguage: Optional[str] = None
    limitedExpansion: Optional[bool] = None