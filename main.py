# Libs
import math  # Math

from fastmcp import FastMCP  # MCP Server

# Application
from math_types import Number  # Types

app = FastMCP(
    name="Math MCP Server",
    version="0.1.0",
    instructions="Provides math calculations in your Agent, Assistant or local LLM",
    website_url="https://math.amirhossein.info",
)


# Trigonometric


@app.tool(title="Sine", tags={"trig"})
def sin(x: Number) -> float:
    """Return the sine of x"""

    return math.sin(x)


@app.tool(title="Cosine", tags={"trig"})
def cos(x: Number) -> float:
    """Return the cosine of x"""

    return math.cos(x)


@app.tool(title="Tangent", tags={"trig"})
def tan(x: Number) -> float:
    """Return the tangent of x"""

    return math.tan(x)


@app.tool(title="Arc Sine", tags={"trig"})
def asin(x: Number) -> float:
    """Return the arc sine of x in radians. x ∈ [-1, 1]"""

    return math.asin(x)


@app.tool(title="Arc Cosine", tags={"trig"})
def acos(x: Number) -> float:
    """Return the arc cosine of x in radians. x ∈ [-1, 1]"""

    if not -1 <= x <= 1:
        raise ValueError("x must be in the range -1 to 1")

    return math.acos(x)


@app.tool(title="Arc Tangent", tags={"trig"})
def atan(x: Number) -> float:
    """Return the arc tangent of x in radians, in (-π/2, π/2)"""

    return math.atan(x)


@app.tool(title="Arc Tangent of y/x")
def atan2(y: Number, x: Number) -> float:
    """Return atan2(y, x) in radians, in (-π, π]"""

    return math.atan2(y, x)


# Hyperbolic


@app.tool(title="Hyperbolic Sine", tags={"hyperbolic"})
def sinh(x: Number) -> float:
    """Return the hyperbolic sine of x"""

    return math.sinh(x)


@app.tool(title="Hyperbolic Cosine", tags={"hyperbolic"})
def cosh(x: Number) -> float:
    """Return the hyperbolic cosine of x"""

    return math.cosh(x)


@app.tool(title="Hyperbolic Tangent", tags={"hyperbolic"})
def tanh(x: Number) -> float:
    """Return the hyperbolic tangent of x"""

    return math.tanh(x)


@app.tool(title="Inverse Hyperbolic Sine", tags={"hyperbolic"})
def asinh(x: Number) -> float:
    """Return the inverse hyperbolic sine of x"""

    return math.asinh(x)


@app.tool(title="Inverse Hyperbolic Cosine", tags={"hyperbolic"})
def acosh(x: Number) -> float:
    """Return the inverse hyperbolic cosine of x. x ≥ 1"""

    return math.acosh(x)


@app.tool(title="Inverse Hyperbolic Tangent", tags={"hyperbolic"})
def atanh(x: Number) -> float:
    """Return the inverse hyperbolic tangent of x. x ∈ (-1, 1)"""

    return math.atanh(x)


# Angle conversion


@app.tool(title="Degrees to Radians", tags={"angle"})
def radians(x: Number) -> float:
    """Convert angle x from degrees to radians"""

    return math.radians(x)


@app.tool(title="Radians to Degrees", tags={"angle"})
def degrees(x: Number) -> float:
    """Convert angle x from radians to degrees"""

    return math.degrees(x)


# Log / Exp


@app.tool(title="Exponential (e^x)", tags={"log_exp"})
def exp(x: Number) -> float:
    """Return e raised to the power of x"""

    return math.exp(x)


@app.tool(title="Exp Minus 1", tags={"log_exp"})
def expm1(x: Number) -> float:
    """Return e^x - 1, accurate for small x"""

    return math.expm1(x)


@app.tool(title="Base Logarithm", tags={"log_exp"})
def log(x: Number, base: Number) -> float:
    """Return the logarithm of x with the given base"""

    return math.log(x, base)


@app.tool(title="Base-10 Logarithm", tags={"log_exp"})
def log10(x: Number) -> float:
    """Return the base-10 logarithm of x"""

    return math.log10(x)


@app.tool(title="Base-2 Logarithm", tags={"log_exp"})
def log2(x: Number) -> float:
    """Return the base-2 logarithm of x"""

    return math.log2(x)


@app.tool(title="Log of 1+x", tags={"log_exp"})
def log1p(x: Number) -> float:
    """Return log(1 + x), accurate for small x"""

    return math.log1p(x)


# Power / Root


@app.tool(title="Power (x^y)", tags={"power"})
def power(x: Number, y: Number) -> float:
    """Return x raised to the power y"""

    return math.pow(x, y)


@app.tool(title="Square Root", tags={"power"})
def sqrt(x: Number) -> float:
    """Return the square root of x"""

    return math.sqrt(x)


@app.tool(title="Integer Square Root", tags={"power"})
def isqrt(x: int) -> int:
    """Return the integer square root of x"""

    return math.isqrt(x)


# Rounding


@app.tool(title="Round Up (Ceil)", tags={"rounding"})
def ceil(x: Number) -> float:
    """Round x up to the nearest integer"""

    return math.ceil(x)


@app.tool(title="Round Down (Floor)", tags={"rounding"})
def floor(x: Number) -> float:
    """Round x down to the nearest integer"""

    return math.floor(x)


@app.tool(title="Truncate", tags={"rounding"})
def trunc(x: Number) -> int:
    """Return the truncated integer part of x (toward zero)"""

    return math.trunc(x)


# Combinatorics


@app.tool(title="Factorial", tags={"combinatorics"})
def factorial(n: int) -> int:
    """Return n! (factorial of n). n must be >= 0"""

    return math.factorial(n)


@app.tool(title="Combinations", tags={"combinatorics"})
def comb(n: int, k: int) -> int:
    """Return the number of ways to choose k items from n without order (n choose k)"""

    return math.comb(n, k)


@app.tool(title="Permutations", tags={"combinatorics"})
def perm(n: int, k: int) -> int:
    """Return the number of ways to choose k items from n with order (P(n, k))"""

    return math.perm(n, k)


# Number ops

# Distance / Norm


@app.tool(title="Euclidean Norm", tags={"geometry"})
def hypot(x: Number, y: Number) -> float:
    """Return the Euclidean norm sqrt(x² + y²)"""

    return math.hypot(x, y)


@app.tool(title="Euclidean Distance", tags={"geometry"})
def dist(p: list[float], q: list[float]) -> float:
    """Return the Euclidean distance between points p and q"""

    return math.dist(p, q)


# Float checks

# Aggregate / Misc
