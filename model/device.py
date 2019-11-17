#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Device) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class DeviceUdi(BackboneElement):
    """ Unique Device Identifier (UDI) Barcode string.

    [Unique device identifier (UDI)](device.html#5.11.3.2.2) assigned to device
    label or package.
    """
    resource_type: ClassVar[str] = "DeviceUdi"

    deviceIdentifier: Optional[str] = None
    name: Optional[str] = None
    jurisdiction: Optional[str] = None
    carrierHRF: Optional[str] = None
    carrierAIDC: Optional[str] = None
    issuer: Optional[str] = None
    entryType: Optional[str] = None


@dataclass
class Device(DomainResource):
    """ Item used in healthcare.

    This resource identifies an instance or a type of a manufactured item that
    is used in the provision of healthcare without being substantially changed
    through that activity. The device may be a medical or non-medical device.
    Medical devices include durable (reusable) medical equipment, implantable
    devices, as well as disposable equipment used for diagnostic, treatment,
    and research for healthcare and public health.  Non-medical devices may
    include items such as a machine, cellphone, computer, application, etc.
    """
    resource_type: ClassVar[str] = "Device"

    identifier: Optional[List[Identifier]] = None
    udi: Optional[DeviceUdi] = None
    status: Optional[str] = None
    type: Optional[CodeableConcept] = None
    lotNumber: Optional[str] = None
    manufacturer: Optional[str] = None
    manufactureDate: Optional[FHIRDate] = None
    expirationDate: Optional[FHIRDate] = None
    model: Optional[str] = None
    version: Optional[str] = None
    patient: Optional[FHIRReference] = None
    owner: Optional[FHIRReference] = None
    contact: Optional[List[ContactPoint]] = None
    location: Optional[FHIRReference] = None
    url: Optional[str] = None
    note: Optional[List[Annotation]] = None
    safety: Optional[List[CodeableConcept]] = None