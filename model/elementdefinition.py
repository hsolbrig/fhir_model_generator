#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/ElementDefinition) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .address import Address
from .age import Age
from .annotation import Annotation
from .attachment import Attachment
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactpoint import ContactPoint
from .count import Count
from .distance import Distance
from .duration import Duration
from .element import Element
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .humanname import HumanName
from .identifier import Identifier
from .meta import Meta
from .money import Money
from .period import Period
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .sampleddata import SampledData
from .signature import Signature
from .timing import Timing


@dataclass
class ElementDefinitionSlicingDiscriminator(Element):
    """ Element values that are used to distinguish the slices.

    Designates which child elements are used to discriminate between the slices
    when processing an instance. If one or more discriminators are provided,
    the value of the child elements in the instance data SHALL completely
    distinguish which slice the element in the resource matches based on the
    allowed values for those elements in each of the slices.
    """
    resource_type: ClassVar[str] = "ElementDefinitionSlicingDiscriminator"

    type: str = None
    path: str = None


@dataclass
class ElementDefinitionSlicing(Element):
    """ This element is sliced - slices follow.

    Indicates that the element is sliced into a set of alternative definitions
    (i.e. in a structure definition, there are multiple different constraints
    on a single element in the base resource). Slicing can be used in any
    resource that has cardinality ..* on the base resource, or any resource
    with a choice of types. The set of slices is any elements that come after
    this in the element sequence that have the same path, until a shorter path
    occurs (the shorter path terminates the set).
    """
    resource_type: ClassVar[str] = "ElementDefinitionSlicing"

    discriminator: Optional[List[ElementDefinitionSlicingDiscriminator]] = None
    description: Optional[str] = None
    ordered: Optional[bool] = None
    rules: str = None


@dataclass
class ElementDefinitionBase(Element):
    """ Base definition information for tools.

    Information about the base definition of the element, provided to make it
    unnecessary for tools to trace the deviation of the element through the
    derived and related profiles. This information is provided when the element
    definition is not the original definition of an element - i.g. either in a
    constraint on another type, or for elements from a super type in a snap
    shot.
    """
    resource_type: ClassVar[str] = "ElementDefinitionBase"

    path: str = None
    min: int = None
    max: str = None


@dataclass
class ElementDefinitionType(Element):
    """ Data type and Profile for this element.

    The data type or resource that the value of this element is permitted to
    be.
    """
    resource_type: ClassVar[str] = "ElementDefinitionType"

    code: str = None
    profile: Optional[str] = None
    targetProfile: Optional[str] = None
    aggregation: Optional[List[str]] = None
    versioning: Optional[str] = None


@dataclass
class ElementDefinitionExample(Element):
    """ Example value (as defined for type).

    A sample value for this element demonstrating the type of information that
    would typically be found in the element.
    """
    resource_type: ClassVar[str] = "ElementDefinitionExample"

    label: str = None
    valueBase64Binary: str = field(default=None, metadata=dict(one_of_many='value',))
    valueBoolean: bool = field(default=None, metadata=dict(one_of_many='value',))
    valueCode: str = field(default=None, metadata=dict(one_of_many='value',))
    valueDate: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueDateTime: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueDecimal: float = field(default=None, metadata=dict(one_of_many='value',))
    valueId: str = field(default=None, metadata=dict(one_of_many='value',))
    valueInstant: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueInteger: int = field(default=None, metadata=dict(one_of_many='value',))
    valueMarkdown: str = field(default=None, metadata=dict(one_of_many='value',))
    valueOid: str = field(default=None, metadata=dict(one_of_many='value',))
    valuePositiveInt: int = field(default=None, metadata=dict(one_of_many='value',))
    valueString: str = field(default=None, metadata=dict(one_of_many='value',))
    valueTime: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueUnsignedInt: int = field(default=None, metadata=dict(one_of_many='value',))
    valueUri: str = field(default=None, metadata=dict(one_of_many='value',))
    valueAddress: Address = field(default=None, metadata=dict(one_of_many='value',))
    valueAge: Age = field(default=None, metadata=dict(one_of_many='value',))
    valueAnnotation: Annotation = field(default=None, metadata=dict(one_of_many='value',))
    valueAttachment: Attachment = field(default=None, metadata=dict(one_of_many='value',))
    valueCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='value',))
    valueCoding: Coding = field(default=None, metadata=dict(one_of_many='value',))
    valueContactPoint: ContactPoint = field(default=None, metadata=dict(one_of_many='value',))
    valueCount: Count = field(default=None, metadata=dict(one_of_many='value',))
    valueDistance: Distance = field(default=None, metadata=dict(one_of_many='value',))
    valueDuration: Duration = field(default=None, metadata=dict(one_of_many='value',))
    valueHumanName: HumanName = field(default=None, metadata=dict(one_of_many='value',))
    valueIdentifier: Identifier = field(default=None, metadata=dict(one_of_many='value',))
    valueMoney: Money = field(default=None, metadata=dict(one_of_many='value',))
    valuePeriod: Period = field(default=None, metadata=dict(one_of_many='value',))
    valueQuantity: Quantity = field(default=None, metadata=dict(one_of_many='value',))
    valueRange: Range = field(default=None, metadata=dict(one_of_many='value',))
    valueRatio: Ratio = field(default=None, metadata=dict(one_of_many='value',))
    valueReference: FHIRReference = field(default=None, metadata=dict(one_of_many='value',))
    valueSampledData: SampledData = field(default=None, metadata=dict(one_of_many='value',))
    valueSignature: Signature = field(default=None, metadata=dict(one_of_many='value',))
    valueTiming: Timing = field(default=None, metadata=dict(one_of_many='value',))
    valueMeta: Meta = field(default=None, metadata=dict(one_of_many='value',))


@dataclass
class ElementDefinitionConstraint(Element):
    """ Condition that must evaluate to true.

    Formal constraints such as co-occurrence and other constraints that can be
    computationally evaluated within the context of the instance.
    """
    resource_type: ClassVar[str] = "ElementDefinitionConstraint"

    key: str = None
    requirements: Optional[str] = None
    severity: str = None
    human: str = None
    expression: str = None
    xpath: Optional[str] = None
    source: Optional[str] = None


@dataclass
class ElementDefinitionBinding(Element):
    """ ValueSet details if this is coded.

    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept, Quantity), or the data types (string, uri).
    """
    resource_type: ClassVar[str] = "ElementDefinitionBinding"

    strength: str = None
    description: Optional[str] = None
    valueSetUri: Optional[str] = field(default=None, metadata=dict(one_of_many='valueSet',))
    valueSetReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='valueSet',))


@dataclass
class ElementDefinitionMapping(Element):
    """ Map element to another set of definitions.

    Identifies a concept from an external specification that roughly
    corresponds to this element.
    """
    resource_type: ClassVar[str] = "ElementDefinitionMapping"

    identity: str = None
    language: Optional[str] = None
    map: str = None
    comment: Optional[str] = None


@dataclass
class ElementDefinition(Element):
    """ Definition of an element in a resource or extension.

    Captures constraints on each element within the resource, profile, or
    extension.
    """
    resource_type: ClassVar[str] = "ElementDefinition"

    path: str = None
    representation: Optional[List[str]] = None
    sliceName: Optional[str] = None
    label: Optional[str] = None
    code: Optional[List[Coding]] = None
    slicing: Optional[ElementDefinitionSlicing] = None
    short: Optional[str] = None
    definition: Optional[str] = None
    comment: Optional[str] = None
    requirements: Optional[str] = None
    alias: Optional[List[str]] = None
    min: Optional[int] = None
    max: Optional[str] = None
    base: Optional[ElementDefinitionBase] = None
    contentReference: Optional[str] = None
    type: Optional[List[ElementDefinitionType]] = None
    defaultValueBase64Binary: Optional[str] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueCode: Optional[str] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueDecimal: Optional[float] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueId: Optional[str] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueInstant: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueInteger: Optional[int] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueMarkdown: Optional[str] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueOid: Optional[str] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValuePositiveInt: Optional[int] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueString: Optional[str] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueUnsignedInt: Optional[int] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueUri: Optional[str] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueAddress: Optional[Address] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueAge: Optional[Age] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueAnnotation: Optional[Annotation] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueCoding: Optional[Coding] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueContactPoint: Optional[ContactPoint] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueCount: Optional[Count] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueDistance: Optional[Distance] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueDuration: Optional[Duration] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueHumanName: Optional[HumanName] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueIdentifier: Optional[Identifier] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueMoney: Optional[Money] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValuePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueRatio: Optional[Ratio] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueSampledData: Optional[SampledData] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueSignature: Optional[Signature] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueMeta: Optional[Meta] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    meaningWhenMissing: Optional[str] = None
    orderMeaning: Optional[str] = None
    fixedBase64Binary: Optional[str] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedCode: Optional[str] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedDecimal: Optional[float] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedId: Optional[str] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedInstant: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedInteger: Optional[int] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedMarkdown: Optional[str] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedOid: Optional[str] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedPositiveInt: Optional[int] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedString: Optional[str] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedUnsignedInt: Optional[int] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedUri: Optional[str] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedAddress: Optional[Address] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedAge: Optional[Age] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedAnnotation: Optional[Annotation] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedCoding: Optional[Coding] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedContactPoint: Optional[ContactPoint] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedCount: Optional[Count] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedDistance: Optional[Distance] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedDuration: Optional[Duration] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedHumanName: Optional[HumanName] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedIdentifier: Optional[Identifier] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedMoney: Optional[Money] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedRatio: Optional[Ratio] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedSampledData: Optional[SampledData] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedSignature: Optional[Signature] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='fixed',))
    fixedMeta: Optional[Meta] = field(default=None, metadata=dict(one_of_many='fixed',))
    patternBase64Binary: Optional[str] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternCode: Optional[str] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternDecimal: Optional[float] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternId: Optional[str] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternInstant: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternInteger: Optional[int] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternMarkdown: Optional[str] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternOid: Optional[str] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternPositiveInt: Optional[int] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternString: Optional[str] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternUnsignedInt: Optional[int] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternUri: Optional[str] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternAddress: Optional[Address] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternAge: Optional[Age] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternAnnotation: Optional[Annotation] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternCoding: Optional[Coding] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternContactPoint: Optional[ContactPoint] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternCount: Optional[Count] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternDistance: Optional[Distance] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternDuration: Optional[Duration] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternHumanName: Optional[HumanName] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternIdentifier: Optional[Identifier] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternMoney: Optional[Money] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternRatio: Optional[Ratio] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternSampledData: Optional[SampledData] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternSignature: Optional[Signature] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='pattern',))
    patternMeta: Optional[Meta] = field(default=None, metadata=dict(one_of_many='pattern',))
    example: Optional[List[ElementDefinitionExample]] = None
    minValueDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='minValue',))
    minValueDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='minValue',))
    minValueInstant: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='minValue',))
    minValueTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='minValue',))
    minValueDecimal: Optional[float] = field(default=None, metadata=dict(one_of_many='minValue',))
    minValueInteger: Optional[int] = field(default=None, metadata=dict(one_of_many='minValue',))
    minValuePositiveInt: Optional[int] = field(default=None, metadata=dict(one_of_many='minValue',))
    minValueUnsignedInt: Optional[int] = field(default=None, metadata=dict(one_of_many='minValue',))
    minValueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='minValue',))
    maxValueDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='maxValue',))
    maxValueDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='maxValue',))
    maxValueInstant: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='maxValue',))
    maxValueTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='maxValue',))
    maxValueDecimal: Optional[float] = field(default=None, metadata=dict(one_of_many='maxValue',))
    maxValueInteger: Optional[int] = field(default=None, metadata=dict(one_of_many='maxValue',))
    maxValuePositiveInt: Optional[int] = field(default=None, metadata=dict(one_of_many='maxValue',))
    maxValueUnsignedInt: Optional[int] = field(default=None, metadata=dict(one_of_many='maxValue',))
    maxValueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='maxValue',))
    maxLength: Optional[int] = None
    condition: Optional[List[str]] = None
    constraint: Optional[List[ElementDefinitionConstraint]] = None
    mustSupport: Optional[bool] = None
    isModifier: Optional[bool] = None
    isSummary: Optional[bool] = None
    binding: Optional[ElementDefinitionBinding] = None
    mapping: Optional[List[ElementDefinitionMapping]] = None