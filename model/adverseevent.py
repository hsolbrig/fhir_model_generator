#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/AdverseEvent) on 2019-11-17.
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
from .timing import Timing


@dataclass
class AdverseEventSuspectEntityCausality(BackboneElement):
    """ Information on the possible cause of the event.
    """
    resource_type: ClassVar[str] = "AdverseEventSuspectEntityCausality"

    assessmentMethod: Optional[CodeableConcept] = None
    entityRelatedness: Optional[CodeableConcept] = None
    author: Optional[FHIRReference] = None


@dataclass
class AdverseEventParticipant(BackboneElement):
    """ Who was involved in the adverse event or the potential adverse event and
    what they did.

    Indicates who or what participated in the adverse event and how they were
    involved.
    """
    resource_type: ClassVar[str] = "AdverseEventParticipant"

    function: Optional[CodeableConcept] = None
    actor: FHIRReference = None


@dataclass
class AdverseEventSuspectEntity(BackboneElement):
    """ The suspected agent causing the adverse event.

    Describes the entity that is suspected to have caused the adverse event.
    """
    resource_type: ClassVar[str] = "AdverseEventSuspectEntity"

    instanceCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='instance',))
    instanceReference: FHIRReference = field(default=None, metadata=dict(one_of_many='instance',))
    causality: Optional[AdverseEventSuspectEntityCausality] = None


@dataclass
class AdverseEventContributingFactor(BackboneElement):
    """ Contributing factors suspected to have increased the probability or
    severity of the adverse event.

    The contributing factors suspected to have increased the probability or
    severity of the adverse event.
    """
    resource_type: ClassVar[str] = "AdverseEventContributingFactor"

    itemReference: FHIRReference = field(default=None, metadata=dict(one_of_many='item',))
    itemCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='item',))


@dataclass
class AdverseEventPreventiveAction(BackboneElement):
    """ Preventive actions that contributed to avoiding the adverse event.
    """
    resource_type: ClassVar[str] = "AdverseEventPreventiveAction"

    itemReference: FHIRReference = field(default=None, metadata=dict(one_of_many='item',))
    itemCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='item',))


@dataclass
class AdverseEventMitigatingAction(BackboneElement):
    """ Ameliorating actions taken after the adverse event occured in order to
    reduce the extent of harm.

    The ameliorating action taken after the adverse event occured in order to
    reduce the extent of harm.
    """
    resource_type: ClassVar[str] = "AdverseEventMitigatingAction"

    itemReference: FHIRReference = field(default=None, metadata=dict(one_of_many='item',))
    itemCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='item',))


@dataclass
class AdverseEventSupportingInfo(BackboneElement):
    """ Supporting information relevant to the event.
    """
    resource_type: ClassVar[str] = "AdverseEventSupportingInfo"

    itemReference: FHIRReference = field(default=None, metadata=dict(one_of_many='item',))
    itemCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='item',))


@dataclass
class AdverseEvent(DomainResource):
    """ Medical care, research study or other healthcare event causing physical
    injury.

    An event (i.e. any change to current patient status) that may be related to
    unintended effects on a patient or research subject.  The unintended
    effects may require additional monitoring, treatment or hospitalization or
    may result in death.  The AdverseEvent resource also extends to potential
    or avoided events that could have had such effects.
    """
    resource_type: ClassVar[str] = "AdverseEvent"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    actuality: str = None
    category: Optional[List[CodeableConcept]] = None
    code: Optional[CodeableConcept] = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    occurrenceDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrencePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrenceTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='occurrence',))
    detected: Optional[FHIRDate] = None
    recordedDate: Optional[FHIRDate] = None
    resultingCondition: Optional[List[FHIRReference]] = None
    location: Optional[FHIRReference] = None
    seriousness: Optional[CodeableConcept] = None
    outcome: Optional[CodeableConcept] = None
    recorder: Optional[FHIRReference] = None
    participant: Optional[List[AdverseEventParticipant]] = None
    suspectEntity: Optional[List[AdverseEventSuspectEntity]] = None
    contributingFactor: Optional[List[AdverseEventContributingFactor]] = None
    preventiveAction: Optional[List[AdverseEventPreventiveAction]] = None
    mitigatingAction: Optional[List[AdverseEventMitigatingAction]] = None
    supportingInfo: Optional[List[AdverseEventSupportingInfo]] = None
    study: Optional[List[FHIRReference]] = None