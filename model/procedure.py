#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Procedure) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class ProcedurePerformer(BackboneElement):
    """ The people who performed the procedure.

    Limited to 'real' people rather than equipment.
    """
    resource_type: ClassVar[str] = "ProcedurePerformer"

    role: Optional[CodeableConcept] = None
    actor: FHIRReference = None
    onBehalfOf: Optional[FHIRReference] = None


@dataclass
class ProcedureFocalDevice(BackboneElement):
    """ Device changed in procedure.

    A device that is implanted, removed or otherwise manipulated (calibration,
    battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as
    a focal portion of the Procedure.
    """
    resource_type: ClassVar[str] = "ProcedureFocalDevice"

    action: Optional[CodeableConcept] = None
    manipulated: FHIRReference = None


@dataclass
class Procedure(DomainResource):
    """ An action that is being or was performed on a patient.

    An action that is or was performed on a patient. This can be a physical
    intervention like an operation, or less invasive like counseling or
    hypnotherapy.
    """
    resource_type: ClassVar[str] = "Procedure"

    identifier: Optional[List[Identifier]] = None
    definition: Optional[List[FHIRReference]] = None
    basedOn: Optional[List[FHIRReference]] = None
    partOf: Optional[List[FHIRReference]] = None
    status: str = None
    notDone: Optional[bool] = None
    notDoneReason: Optional[CodeableConcept] = None
    category: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None
    subject: FHIRReference = None
    context: Optional[FHIRReference] = None
    performedDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='performed',))
    performedPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='performed',))
    performer: Optional[List[ProcedurePerformer]] = None
    location: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    bodySite: Optional[List[CodeableConcept]] = None
    outcome: Optional[CodeableConcept] = None
    report: Optional[List[FHIRReference]] = None
    complication: Optional[List[CodeableConcept]] = None
    complicationDetail: Optional[List[FHIRReference]] = None
    followUp: Optional[List[CodeableConcept]] = None
    note: Optional[List[Annotation]] = None
    focalDevice: Optional[List[ProcedureFocalDevice]] = None
    usedReference: Optional[List[FHIRReference]] = None
    usedCode: Optional[List[CodeableConcept]] = None