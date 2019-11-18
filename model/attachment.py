#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/Attachment) on 2019-11-18.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .element import Element
from .fhirdate import FHIRDate


@dataclass
class Attachment(Element):
    """ Content in a format defined elsewhere.

    For referring to data content defined in other formats.
    """
    resource_type: ClassVar[str] = "Attachment"

    contentType: Optional[str] = None
    language: Optional[str] = None
    data: Optional[str] = None
    url: Optional[str] = None
    size: Optional[int] = None
    hash: Optional[str] = None
    title: Optional[str] = None
    creation: Optional[FHIRDate] = None
    height: Optional[int] = None
    width: Optional[int] = None
    frames: Optional[int] = None
    duration: Optional[float] = None
    pages: Optional[int] = None