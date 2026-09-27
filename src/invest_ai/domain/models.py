"""Contratos de dominio do Assistente Invest Ae.

Estes modelos representam necessidade, evidencias e resultado da analise.
Eles nao substituem o contrato financeiro do Invest Ae e nao sao uma
segunda fonte de verdade para dados de mercado.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class AnalysisStatus(str, Enum):
    READY = "READY"
    PARTIAL_ANALYSIS = "PARTIAL_ANALYSIS"
    NEEDS_MORE_USER_INFORMATION = "NEEDS_MORE_USER_INFORMATION"
    INSUFFICIENT_MARKET_DATA = "INSUFFICIENT_MARKET_DATA"
    NO_COMPATIBLE_OPTIONS = "NO_COMPATIBLE_OPTIONS"
    DATA_QUALITY_FAILURE = "DATA_QUALITY_FAILURE"


class Compatibility(str, Enum):
    COMPATIBLE = "COMPATIBLE"
    PARTIALLY_COMPATIBLE = "PARTIALLY_COMPATIBLE"
    INCOMPATIBLE = "INCOMPATIBLE"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"


@dataclass(frozen=True)
class InvestorNeed:
    available_capital: float | None = None
    objective: str | None = None
    risk_tolerance: str | None = None
    investment_horizon_months: int | None = None
    liquidity_need: str | None = None
    periodic_income: bool | None = None
    income_frequency: str | None = None
    experience_level: str | None = None
    restrictions: tuple[str, ...] = ()


@dataclass(frozen=True)
class NeedAssessment:
    sufficient: bool
    missing_fields: tuple[str, ...] = ()


@dataclass(frozen=True)
class EvidenceReference:
    """Referencia rastreavel a um dado fornecido pela camada do Invest Ae."""

    asset_id: str
    metric: str
    value: Any
    source_name: str | None = None
    data_source_type: str | None = None
    reference_date: str | None = None
    methodology: str | None = None


@dataclass(frozen=True)
class CandidateAnalysis:
    asset_id: str
    compatibility: Compatibility
    matched_criteria: tuple[str, ...] = ()
    unmatched_criteria: tuple[str, ...] = ()
    evidence: tuple[EvidenceReference, ...] = ()
    warnings: tuple[str, ...] = ()


@dataclass(frozen=True)
class InvestmentAnalysis:
    status: AnalysisStatus
    user_need: InvestorNeed
    candidates: tuple[CandidateAnalysis, ...] = ()
    excluded_candidates: tuple[CandidateAnalysis, ...] = ()
    supported_criteria: tuple[str, ...] = ()
    unsupported_criteria: tuple[str, ...] = ()
    missing_information: tuple[str, ...] = ()
    warnings: tuple[str, ...] = ()
    evidence: tuple[EvidenceReference, ...] = field(default_factory=tuple)
