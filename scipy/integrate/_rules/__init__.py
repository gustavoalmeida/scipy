"""Numerical cubature algorithms"""

from ._base import (
    Rule, FixedRule,
    NestedFixedRule, NestedRule,
    ProductFixed, ProductNestedFixed
)
from ._genz_malik import GenzMalikCub
from ._newton_cotes import NewtonCotesQuad
from ._gauss_kronrod import GaussKronrodQuad
from ._gauss_legendre import GaussLegendreQuad

__all__ = [s for s in dir() if not s.startswith('_')]
