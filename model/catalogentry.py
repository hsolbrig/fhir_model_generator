#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/CatalogEntry) on 2019-11-18.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .duration import Duration
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class CatalogEntryRelatedEntry(BackboneElement):
    """ Another entry of the catalog related to this one.

    Used for example, to point to a substance, or to a device used to
    administer a medication.
    """
    resource_type: ClassVar[str] = "CatalogEntryRelatedEntry"

    relationship: str = None
    target: FHIRReference = None


@dataclass
class CatalogEntry(DomainResource):
    """ An entry in a catalog.

    Catalog entries are wrappers that contextualize items included in a
    catalog.
    """
    resource_type: ClassVar[str] = "CatalogEntry"

    identifier: Optional[List[Identifier]] = None
    name: Optional[str] = None
    type: Optional[str] = None
    status: Optional[str] = None
    effectivePeriod: Optional[Period] = None
    orderable: bool = None
    referencedItem: FHIRReference = None
    relatedEntry: Optional[List[CatalogEntryRelatedEntry]] = None
    updatedBy: Optional[FHIRReference] = None
    note: Optional[List[Annotation]] = None
    estimatedDuration: Optional[Duration] = None
    billingCode: Optional[List[CodeableConcept]] = None
    billingSummary: Optional[str] = None
    scheduleSummary: Optional[str] = None
    limitationSummary: Optional[str] = None
    regulatorySummary: Optional[str] = None