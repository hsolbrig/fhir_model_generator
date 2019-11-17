#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/SpecimenDefinition) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .duration import Duration
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range
from .usagecontext import UsageContext


@dataclass
class SpecimenDefinitionTypeTestedContainerAdditive(BackboneElement):
    """ Additive associated with container.

    Substance introduced in the kind of container to preserve, maintain or
    enhance the specimen. Examples: Formalin, Citrate, EDTA.
    """
    resource_type: ClassVar[str] = "SpecimenDefinitionTypeTestedContainerAdditive"

    additiveCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='additive',))
    additiveReference: FHIRReference = field(default=None, metadata=dict(one_of_many='additive',))


@dataclass
class SpecimenDefinitionTypeTestedContainer(BackboneElement):
    """ The specimen's container.
    """
    resource_type: ClassVar[str] = "SpecimenDefinitionTypeTestedContainer"

    material: Optional[CodeableConcept] = None
    type: Optional[CodeableConcept] = None
    cap: Optional[CodeableConcept] = None
    description: Optional[str] = None
    capacity: Optional[Quantity] = None
    minimumVolumeQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='minimumVolume',))
    minimumVolumeString: Optional[str] = field(default=None, metadata=dict(one_of_many='minimumVolume',))
    additive: Optional[List[SpecimenDefinitionTypeTestedContainerAdditive]] = None
    preparation: Optional[str] = None


@dataclass
class SpecimenDefinitionTypeTestedHandling(BackboneElement):
    """ Specimen handling before testing.

    Set of instructions for preservation/transport of the specimen at a defined
    temperature interval, prior the testing process.
    """
    resource_type: ClassVar[str] = "SpecimenDefinitionTypeTestedHandling"

    temperatureQualifier: Optional[CodeableConcept] = None
    temperatureRange: Optional[Range] = None
    maxDuration: Optional[Duration] = None
    instruction: Optional[str] = None


@dataclass
class SpecimenDefinitionTypeTested(BackboneElement):
    """ Specimen in container intended for testing by lab.

    Specimen conditioned in a container as expected by the testing laboratory.
    """
    resource_type: ClassVar[str] = "SpecimenDefinitionTypeTested"

    isDerived: Optional[bool] = None
    type: Optional[CodeableConcept] = None
    preference: str = None
    container: Optional[SpecimenDefinitionTypeTestedContainer] = None
    requirement: Optional[str] = None
    retentionTime: Optional[Duration] = None
    singleUse: Optional[bool] = None
    rejectionCriterion: Optional[List[CodeableConcept]] = None
    handling: Optional[List[SpecimenDefinitionTypeTestedHandling]] = None
    testingDestination: Optional[List[CodeableConcept]] = None


@dataclass
class SpecimenDefinition(DomainResource):
    """ Kind of specimen.

    A kind of specimen with associated set of requirements.
    """
    resource_type: ClassVar[str] = "SpecimenDefinition"

    url: Optional[str] = None
    identifier: Optional[Identifier] = None
    version: Optional[str] = None
    title: Optional[str] = None
    derivedFromCanonical: Optional[List[str]] = None
    derivedFromUri: Optional[List[str]] = None
    status: str = None
    experimental: Optional[bool] = None
    subjectCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='subject',))
    subjectReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='subject',))
    date: Optional[FHIRDate] = None
    publisher: Optional[FHIRReference] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    purpose: Optional[str] = None
    copyright: Optional[str] = None
    approvalDate: Optional[FHIRDate] = None
    lastReviewDate: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    typeCollected: Optional[CodeableConcept] = None
    patientPreparation: Optional[List[CodeableConcept]] = None
    timeAspect: Optional[str] = None
    collection: Optional[List[CodeableConcept]] = None
    typeTested: Optional[List[SpecimenDefinitionTypeTested]] = None