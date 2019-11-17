#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/ImagingManifest) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class ImagingManifestStudySeriesInstance(BackboneElement):
    """ The selected instance.

    Identity and locating information of the selected DICOM SOP instances.
    """
    resource_type: ClassVar[str] = "ImagingManifestStudySeriesInstance"

    sopClass: str = None
    uid: str = None


@dataclass
class ImagingManifestStudySeries(BackboneElement):
    """ Series identity of the selected instances.

    Series identity and locating information of the DICOM SOP instances in the
    selection.
    """
    resource_type: ClassVar[str] = "ImagingManifestStudySeries"

    uid: str = None
    endpoint: Optional[List[FHIRReference]] = None
    instance: List[ImagingManifestStudySeriesInstance] = field(default_factory=list)


@dataclass
class ImagingManifestStudy(BackboneElement):
    """ Study identity of the selected instances.

    Study identity and locating information of the DICOM SOP instances in the
    selection.
    """
    resource_type: ClassVar[str] = "ImagingManifestStudy"

    uid: str = None
    imagingStudy: Optional[FHIRReference] = None
    endpoint: Optional[List[FHIRReference]] = None
    series: List[ImagingManifestStudySeries] = field(default_factory=list)


@dataclass
class ImagingManifest(DomainResource):
    """ Key Object Selection.

    A text description of the DICOM SOP instances selected in the
    ImagingManifest; or the reason for, or significance of, the selection.
    """
    resource_type: ClassVar[str] = "ImagingManifest"

    identifier: Optional[Identifier] = None
    patient: FHIRReference = None
    authoringTime: Optional[FHIRDate] = None
    author: Optional[FHIRReference] = None
    description: Optional[str] = None
    study: List[ImagingManifestStudy] = field(default_factory=list)