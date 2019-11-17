#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/DetectedIssue) on 2019-11-17.
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


@dataclass
class DetectedIssueMitigation(BackboneElement):
    """ Step taken to address.

    Indicates an action that has been taken or is committed to to reduce or
    eliminate the likelihood of the risk identified by the detected issue from
    manifesting.  Can also reflect an observation of known mitigating factors
    that may reduce/eliminate the need for any action.
    """
    resource_type: ClassVar[str] = "DetectedIssueMitigation"

    action: CodeableConcept = None
    date: Optional[FHIRDate] = None
    author: Optional[FHIRReference] = None


@dataclass
class DetectedIssue(DomainResource):
    """ Clinical issue with action.

    Indicates an actual or potential clinical issue with or between one or more
    active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition conflict,
    etc.
    """
    resource_type: ClassVar[str] = "DetectedIssue"

    identifier: Optional[Identifier] = None
    status: str = None
    category: Optional[CodeableConcept] = None
    severity: Optional[str] = None
    patient: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    author: Optional[FHIRReference] = None
    implicated: Optional[List[FHIRReference]] = None
    detail: Optional[str] = None
    reference: Optional[str] = None
    mitigation: Optional[List[DetectedIssueMitigation]] = None