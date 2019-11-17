#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/DocumentReference) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class DocumentReferenceContextRelated(BackboneElement):
    """ Related identifiers or resources.

    Related identifiers or resources associated with the DocumentReference.
    """
    resource_type: ClassVar[str] = "DocumentReferenceContextRelated"

    identifier: Optional[Identifier] = None
    ref: Optional[FHIRReference] = None


@dataclass
class DocumentReferenceRelatesTo(BackboneElement):
    """ Relationships to other documents.

    Relationships that this document has with other document references that
    already exist.
    """
    resource_type: ClassVar[str] = "DocumentReferenceRelatesTo"

    code: str = None
    target: FHIRReference = None


@dataclass
class DocumentReferenceContent(BackboneElement):
    """ Document referenced.

    The document and format referenced. There may be multiple content element
    repetitions, each with a different format.
    """
    resource_type: ClassVar[str] = "DocumentReferenceContent"

    attachment: Attachment = None
    format: Optional[Coding] = None


@dataclass
class DocumentReferenceContext(BackboneElement):
    """ Clinical context of document.

    The clinical context in which the document was prepared.
    """
    resource_type: ClassVar[str] = "DocumentReferenceContext"

    encounter: Optional[FHIRReference] = None
    event: Optional[List[CodeableConcept]] = None
    period: Optional[Period] = None
    facilityType: Optional[CodeableConcept] = None
    practiceSetting: Optional[CodeableConcept] = None
    sourcePatientInfo: Optional[FHIRReference] = None
    related: Optional[List[DocumentReferenceContextRelated]] = None


@dataclass
class DocumentReference(DomainResource):
    """ A reference to a document.
    """
    resource_type: ClassVar[str] = "DocumentReference"

    masterIdentifier: Optional[Identifier] = None
    identifier: Optional[List[Identifier]] = None
    status: str = None
    docStatus: Optional[str] = None
    type: CodeableConcept = None
    class_fhir: Optional[CodeableConcept] = field(default=None, metadata=dict(orig_name='class'))
    subject: Optional[FHIRReference] = None
    created: Optional[FHIRDate] = None
    indexed: FHIRDate = None
    author: Optional[List[FHIRReference]] = None
    authenticator: Optional[FHIRReference] = None
    custodian: Optional[FHIRReference] = None
    relatesTo: Optional[List[DocumentReferenceRelatesTo]] = None
    description: Optional[str] = None
    securityLabel: Optional[List[CodeableConcept]] = None
    content: List[DocumentReferenceContent] = field(default_factory=list)
    context: Optional[DocumentReferenceContext] = None