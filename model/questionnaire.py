#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Questionnaire) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .usagecontext import UsageContext


@dataclass
class QuestionnaireItemEnableWhen(BackboneElement):
    """ Only allow data when.

    A constraint indicating that this item should only be enabled
    (displayed/allow answers to be captured) when the specified condition is
    true.
    """
    resource_type: ClassVar[str] = "QuestionnaireItemEnableWhen"

    question: str = None
    hasAnswer: Optional[bool] = None
    answerBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='answer',))
    answerDecimal: Optional[float] = field(default=None, metadata=dict(one_of_many='answer',))
    answerInteger: Optional[int] = field(default=None, metadata=dict(one_of_many='answer',))
    answerDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='answer',))
    answerDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='answer',))
    answerTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='answer',))
    answerString: Optional[str] = field(default=None, metadata=dict(one_of_many='answer',))
    answerUri: Optional[str] = field(default=None, metadata=dict(one_of_many='answer',))
    answerAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='answer',))
    answerCoding: Optional[Coding] = field(default=None, metadata=dict(one_of_many='answer',))
    answerQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='answer',))
    answerReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='answer',))


@dataclass
class QuestionnaireItemOption(BackboneElement):
    """ Permitted answer.

    One of the permitted answers for a "choice" or "open-choice" question.
    """
    resource_type: ClassVar[str] = "QuestionnaireItemOption"

    valueInteger: int = field(default=None, metadata=dict(one_of_many='value',))
    valueDate: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueTime: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueString: str = field(default=None, metadata=dict(one_of_many='value',))
    valueCoding: Coding = field(default=None, metadata=dict(one_of_many='value',))


@dataclass
class QuestionnaireItem(BackboneElement):
    """ Questions and sections within the Questionnaire.

    A particular question, question grouping or display text that is part of
    the questionnaire.
    """
    resource_type: ClassVar[str] = "QuestionnaireItem"

    linkId: str = None
    definition: Optional[str] = None
    code: Optional[List[Coding]] = None
    prefix: Optional[str] = None
    text: Optional[str] = None
    type: str = None
    enableWhen: Optional[List[QuestionnaireItemEnableWhen]] = None
    required: Optional[bool] = None
    repeats: Optional[bool] = None
    readOnly: Optional[bool] = None
    maxLength: Optional[int] = None
    options: Optional[FHIRReference] = None
    option: Optional[List[QuestionnaireItemOption]] = None
    initialBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='initial',))
    initialDecimal: Optional[float] = field(default=None, metadata=dict(one_of_many='initial',))
    initialInteger: Optional[int] = field(default=None, metadata=dict(one_of_many='initial',))
    initialDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='initial',))
    initialDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='initial',))
    initialTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='initial',))
    initialString: Optional[str] = field(default=None, metadata=dict(one_of_many='initial',))
    initialUri: Optional[str] = field(default=None, metadata=dict(one_of_many='initial',))
    initialAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='initial',))
    initialCoding: Optional[Coding] = field(default=None, metadata=dict(one_of_many='initial',))
    initialQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='initial',))
    initialReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='initial',))
    item: Optional[List["QuestionnaireItem"]] = None


@dataclass
class Questionnaire(DomainResource):
    """ A structured set of questions.

    A structured set of questions intended to guide the collection of answers
    from end-users. Questionnaires provide detailed control over order,
    presentation, phraseology and grouping to allow coherent, consistent data
    collection.
    """
    resource_type: ClassVar[str] = "Questionnaire"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    description: Optional[str] = None
    purpose: Optional[str] = None
    approvalDate: Optional[FHIRDate] = None
    lastReviewDate: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    contact: Optional[List[ContactDetail]] = None
    copyright: Optional[str] = None
    code: Optional[List[Coding]] = None
    subjectType: Optional[List[str]] = None
    item: Optional[List[QuestionnaireItem]] = None