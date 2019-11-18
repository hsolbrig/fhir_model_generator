#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-f80db8871 (http://hl7.org/fhir/StructureDefinition/Topic) on 2019-11-18.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .usagecontext import UsageContext


@dataclass
class TopicResourceTriggerQueryCriteria(BackboneElement):
    """ Query based trigger rule.

    The FHIR query based rules that the server should use to determine when to
    trigger a notification for this topic.
    """
    resource_type: ClassVar[str] = "TopicResourceTriggerQueryCriteria"

    previous: Optional[str] = None
    current: Optional[str] = None
    requireBoth: Optional[bool] = None


@dataclass
class TopicResourceTrigger(BackboneElement):
    """ Criteria for including a resource update in the topic.

    The criteria for including updates to a nominated resource in the topic.
    Thie criteria may be just a human readable description and/or a full FHIR
    search string or FHIRPath expression.
    """
    resource_type: ClassVar[str] = "TopicResourceTrigger"

    description: Optional[str] = None
    resourceType: Optional[List[str]] = None
    methodCriteria: Optional[List[str]] = None
    queryCriteria: Optional[TopicResourceTriggerQueryCriteria] = None
    fhirPathCriteria: Optional[str] = None


@dataclass
class TopicCanFilterBy(BackboneElement):
    """ Properties by which the topic can be filtered.

    List of properties by which messages on the topic can be filtered.
    """
    resource_type: ClassVar[str] = "TopicCanFilterBy"

    name: Optional[str] = None
    matchType: Optional[List[str]] = None
    documentation: Optional[str] = None


@dataclass
class Topic(DomainResource):
    """ Definition Pattern.

    Describes a stream of resource state changes identified by trigger criteria
    and annotated with labels useful to filter projections from this topic.
    """
    resource_type: ClassVar[str] = "Topic"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    title: Optional[str] = None
    derivedFromCanonical: Optional[List[str]] = None
    derivedFromUri: Optional[List[str]] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[FHIRReference] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    purpose: Optional[str] = None
    copyright: Optional[str] = None
    approvalDate: Optional[FHIRDate] = None
    lastReviewDate: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    resourceTrigger: Optional[TopicResourceTrigger] = None
    canFilterBy: Optional[List[TopicCanFilterBy]] = None