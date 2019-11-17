#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.2.11917 (http://hl7.org/fhir/StructureDefinition/Sequence) on 2019-11-17.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity


@dataclass
class SequenceReferenceSeq(BackboneElement):
    """ A sequence used as reference.

    A sequence that is used as a reference to describe variants that are
    present in a sequence analyzed.
    """
    resource_type: ClassVar[str] = "SequenceReferenceSeq"

    chromosome: Optional[CodeableConcept] = None
    genomeBuild: Optional[str] = None
    referenceSeqId: Optional[CodeableConcept] = None
    referenceSeqPointer: Optional[FHIRReference] = None
    referenceSeqString: Optional[str] = None
    strand: Optional[int] = None
    windowStart: int = None
    windowEnd: int = None


@dataclass
class SequenceVariant(BackboneElement):
    """ Variant in sequence.

    The definition of variant here originates from Sequence ontology ([variant_
    of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)).
    This element can represent amino acid or nucleic sequence change(including
    insertion,deletion,SNP,etc.)  It can represent some complex mutation or
    segment variation with the assist of CIGAR string.
    """
    resource_type: ClassVar[str] = "SequenceVariant"

    start: Optional[int] = None
    end: Optional[int] = None
    observedAllele: Optional[str] = None
    referenceAllele: Optional[str] = None
    cigar: Optional[str] = None
    variantPointer: Optional[FHIRReference] = None


@dataclass
class SequenceQuality(BackboneElement):
    """ An set of value as quality of sequence.

    An experimental feature attribute that defines the quality of the feature
    in a quantitative way, such as a phred quality score ([SO:0001686](http://w
    ww.sequenceontology.org/browser/current_svn/term/SO:0001686)).
    """
    resource_type: ClassVar[str] = "SequenceQuality"

    type: str = None
    standardSequence: Optional[CodeableConcept] = None
    start: Optional[int] = None
    end: Optional[int] = None
    score: Optional[Quantity] = None
    method: Optional[CodeableConcept] = None
    truthTP: Optional[float] = None
    queryTP: Optional[float] = None
    truthFN: Optional[float] = None
    queryFP: Optional[float] = None
    gtFP: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None
    fScore: Optional[float] = None


@dataclass
class SequenceRepository(BackboneElement):
    """ External repository which contains detailed report related with observedSeq
    in this resource.

    Configurations of the external repository. The repository shall store
    target's observedSeq or records related with target's observedSeq.
    """
    resource_type: ClassVar[str] = "SequenceRepository"

    type: str = None
    url: Optional[str] = None
    name: Optional[str] = None
    datasetId: Optional[str] = None
    variantsetId: Optional[str] = None
    readsetId: Optional[str] = None


@dataclass
class Sequence(DomainResource):
    """ Information about a biological sequence.

    Raw data describing a biological sequence.
    """
    resource_type: ClassVar[str] = "Sequence"

    identifier: Optional[List[Identifier]] = None
    type: Optional[str] = None
    coordinateSystem: int = None
    patient: Optional[FHIRReference] = None
    specimen: Optional[FHIRReference] = None
    device: Optional[FHIRReference] = None
    performer: Optional[FHIRReference] = None
    quantity: Optional[Quantity] = None
    referenceSeq: Optional[SequenceReferenceSeq] = None
    variant: Optional[List[SequenceVariant]] = None
    observedSeq: Optional[str] = None
    quality: Optional[List[SequenceQuality]] = None
    readCoverage: Optional[int] = None
    repository: Optional[List[SequenceRepository]] = None
    pointer: Optional[List[FHIRReference]] = None