#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/DiagnosticReport) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class DiagnosticReportPerformer(BackboneElement):
    """ Participants in producing the report.

    Indicates who or what participated in producing the report.
    """
    resource_type: ClassVar[str] = "DiagnosticReportPerformer"

    role: Optional[CodeableConcept] = None
    actor: FHIRReference = None


@dataclass
class DiagnosticReportImage(BackboneElement):
    """ Key images associated with this report.

    A list of key images associated with this report. The images are generally
    created during the diagnostic process, and may be directly of the patient,
    or of treated specimens (i.e. slides of interest).
    """
    resource_type: ClassVar[str] = "DiagnosticReportImage"

    comment: Optional[str] = None
    link: FHIRReference = None


@dataclass
class DiagnosticReport(DomainResource):
    """ A Diagnostic report - a combination of request information, atomic results,
    images, interpretation, as well as formatted reports.

    The findings and interpretation of diagnostic  tests performed on patients,
    groups of patients, devices, and locations, and/or specimens derived from
    these. The report includes clinical context such as requesting and provider
    information, and some mix of atomic results, images, textual and coded
    interpretations, and formatted representation of diagnostic reports.
    """
    resource_type: ClassVar[str] = "DiagnosticReport"

    identifier: Optional[List[Identifier]] = None
    basedOn: Optional[List[FHIRReference]] = None
    status: str = None
    category: Optional[CodeableConcept] = None
    code: CodeableConcept = None
    subject: Optional[FHIRReference] = None
    context: Optional[FHIRReference] = None
    effectiveDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='effective',))
    effectivePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='effective',))
    issued: Optional[FHIRDate] = None
    performer: Optional[List[DiagnosticReportPerformer]] = None
    specimen: Optional[List[FHIRReference]] = None
    result: Optional[List[FHIRReference]] = None
    imagingStudy: Optional[List[FHIRReference]] = None
    image: Optional[List[DiagnosticReportImage]] = None
    conclusion: Optional[str] = None
    codedDiagnosis: Optional[List[CodeableConcept]] = None
    presentedForm: Optional[List[Attachment]] = None