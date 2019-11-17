#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Bundle) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .fhirdate import FHIRDate
from .identifier import Identifier
from .resource import Resource
from .signature import Signature


@dataclass
class BundleEntrySearch(BackboneElement):
    """ Search related information.

    Information about the search process that lead to the creation of this
    entry.
    """
    resource_type: ClassVar[str] = "BundleEntrySearch"

    mode: Optional[str] = None
    score: Optional[float] = None


@dataclass
class BundleEntryRequest(BackboneElement):
    """ Transaction Related Information.

    Additional information about how this entry should be processed as part of
    a transaction.
    """
    resource_type: ClassVar[str] = "BundleEntryRequest"

    method: str = None
    url: str = None
    ifNoneMatch: Optional[str] = None
    ifModifiedSince: Optional[FHIRDate] = None
    ifMatch: Optional[str] = None
    ifNoneExist: Optional[str] = None


@dataclass
class BundleEntryResponse(BackboneElement):
    """ Transaction Related Information.

    Additional information about how this entry should be processed as part of
    a transaction.
    """
    resource_type: ClassVar[str] = "BundleEntryResponse"

    status: str = None
    location: Optional[str] = None
    etag: Optional[str] = None
    lastModified: Optional[FHIRDate] = None
    outcome: Optional[Resource] = None


@dataclass
class BundleLink(BackboneElement):
    """ Links related to this Bundle.

    A series of links that provide context to this bundle.
    """
    resource_type: ClassVar[str] = "BundleLink"

    relation: str = None
    url: str = None


@dataclass
class BundleEntry(BackboneElement):
    """ Entry in the bundle - will have a resource, or information.

    An entry in a bundle resource - will either contain a resource, or
    information about a resource (transactions and history only).
    """
    resource_type: ClassVar[str] = "BundleEntry"

    link: Optional[List[BundleLink]] = None
    fullUrl: Optional[str] = None
    resource: Optional[Resource] = None
    search: Optional[BundleEntrySearch] = None
    request: Optional[BundleEntryRequest] = None
    response: Optional[BundleEntryResponse] = None


@dataclass
class Bundle(Resource):
    """ Contains a collection of resources.

    A container for a collection of resources.
    """
    resource_type: ClassVar[str] = "Bundle"

    identifier: Optional[Identifier] = None
    type: str = None
    total: Optional[int] = None
    link: Optional[List[BundleLink]] = None
    entry: Optional[List[BundleEntry]] = None
    signature: Optional[Signature] = None