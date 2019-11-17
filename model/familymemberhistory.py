#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .age import Age
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .range import Range


@dataclass
class FamilyMemberHistoryCondition(BackboneElement):
    """ Condition that the related person had.

    The significant Conditions (or condition) that the family member had. This
    is a repeating section to allow a system to represent more than one
    condition per resource, though there is nothing stopping multiple resources
    - one per condition.
    """
    resource_type: ClassVar[str] = "FamilyMemberHistoryCondition"

    code: CodeableConcept = None
    outcome: Optional[CodeableConcept] = None
    onsetAge: Optional[Age] = field(default=None, metadata=dict(one_of_many='onset',))
    onsetRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='onset',))
    onsetPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='onset',))
    onsetString: Optional[str] = field(default=None, metadata=dict(one_of_many='onset',))
    note: Optional[List[Annotation]] = None


@dataclass
class FamilyMemberHistory(DomainResource):
    """ Information about patient's relatives, relevant for patient.

    Significant health events and conditions for a person related to the
    patient relevant in the context of care for the patient.
    """
    resource_type: ClassVar[str] = "FamilyMemberHistory"

    identifier: Optional[List[Identifier]] = None
    definition: Optional[List[FHIRReference]] = None
    status: str = None
    notDone: Optional[bool] = None
    notDoneReason: Optional[CodeableConcept] = None
    patient: FHIRReference = None
    date: Optional[FHIRDate] = None
    name: Optional[str] = None
    relationship: CodeableConcept = None
    gender: Optional[str] = None
    bornPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='born',))
    bornDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='born',))
    bornString: Optional[str] = field(default=None, metadata=dict(one_of_many='born',))
    ageAge: Optional[Age] = field(default=None, metadata=dict(one_of_many='age',))
    ageRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='age',))
    ageString: Optional[str] = field(default=None, metadata=dict(one_of_many='age',))
    estimatedAge: Optional[bool] = None
    deceasedBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='deceased',))
    deceasedAge: Optional[Age] = field(default=None, metadata=dict(one_of_many='deceased',))
    deceasedRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='deceased',))
    deceasedDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='deceased',))
    deceasedString: Optional[str] = field(default=None, metadata=dict(one_of_many='deceased',))
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None
    condition: Optional[List[FamilyMemberHistoryCondition]] = None