# Libs
import math  # Math

from fastmcp import FastMCP  # MCP Server

app = FastMCP(
    name="Math MCP Server",
    version="0.1.0",
    instructions="Provides math calculations in your Agent, Assistant or local LLM",
    website_url="https://math.amirhossein.info",
)


# Trigonometric


@app.tool(title="Sine", tags={"trig"})
def sin(x: float) -> float:
    """Return the sine of x"""

    return math.sin(x)


@app.tool(title="Cosine", tags={"trig"})
def cos(x: float) -> float:
    """Return the cosine of x"""

    return math.cos(x)


@app.tool(title="Tangent", tags={"trig"})
def tan(x: float) -> float:
    """Return the tangent of x"""

    return math.tan(x)


@app.tool(title="Arc Sine", tags={"trig"})
def asin(x: float) -> float:
    """Return the arc sine of x in radians. x ∈ [-1, 1]"""

    return math.asin(x)


@app.tool(title="Arc Cosine", tags={"trig"})
def acos(x: float) -> float:
    """Return the arc cosine of x in radians. x ∈ [-1, 1]"""

    if not -1 <= x <= 1:
        raise ValueError("x must be in the range -1 to 1")

    return math.acos(x)


@app.tool(title="Arc Tangent", tags={"trig"})
def atan(x: float) -> float:
    """Return the arc tangent of x in radians, in (-π/2, π/2)"""

    return math.atan(x)


@app.tool(title="Arc Tangent of y/x")
def atan2(y: float, x: float) -> float:
    """Return atan2(y, x) in radians, in (-π, π]"""

    return math.atan2(y, x)


# Hyperbolic


@app.tool(title="Hyperbolic Sine", tags={"hyperbolic"})
def sinh(x: float) -> float:
    """Return the hyperbolic sine of x"""

    return math.sinh(x)


@app.tool(title="Hyperbolic Cosine", tags={"hyperbolic"})
def cosh(x: float) -> float:
    """Return the hyperbolic cosine of x"""

    return math.cosh(x)


@app.tool(title="Hyperbolic Tangent", tags={"hyperbolic"})
def tanh(x: float) -> float:
    """Return the hyperbolic tangent of x"""

    return math.tanh(x)


@app.tool(title="Inverse Hyperbolic Sine", tags={"hyperbolic"})
def asinh(x: float) -> float:
    """Return the inverse hyperbolic sine of x"""

    return math.asinh(x)


@app.tool(title="Inverse Hyperbolic Cosine", tags={"hyperbolic"})
def acosh(x: float) -> float:
    """Return the inverse hyperbolic cosine of x. x ≥ 1"""

    return math.acosh(x)


@app.tool(title="Inverse Hyperbolic Tangent", tags={"hyperbolic"})
def atanh(x: float) -> float:
    """Return the inverse hyperbolic tangent of x. x ∈ (-1, 1)"""

    return math.atanh(x)


# Angle conversion


@app.tool(title="Degrees to Radians", tags={"angle"})
def radians(x: float) -> float:
    """Convert angle x from degrees to radians"""

    return math.radians(x)


@app.tool(title="Radians to Degrees", tags={"angle"})
def degrees(x: float) -> float:
    """Convert angle x from radians to degrees"""

    return math.degrees(x)


# Log / Exp


@app.tool(title="Exponential (e^x)", tags={"log_exp"})
def exp(x: float) -> float:
    """Return e raised to the power of x"""

    return math.exp(x)


@app.tool(title="Exp2 (2^x)", tags={"log_exp"})
def exp2(x: float) -> float:
    """Return 2 raised to the power of x"""

    return math.exp2(x)


@app.tool(title="Exp Minus 1", tags={"log_exp"})
def expm1(x: float) -> float:
    """Return e^x - 1, accurate for small x"""

    return math.expm1(x)


@app.tool(title="Base Logarithm", tags={"log_exp"})
def log(x: float, base: float) -> float:
    """Return the logarithm of x with the given base"""

    return math.log(x, base)


@app.tool(title="Base-10 Logarithm", tags={"log_exp"})
def log10(x: float) -> float:
    """Return the base-10 logarithm of x"""

    return math.log10(x)


@app.tool(title="Base-2 Logarithm", tags={"log_exp"})
def log2(x: float) -> float:
    """Return the base-2 logarithm of x"""

    return math.log2(x)


@app.tool(title="Log of 1+x", tags={"log_exp"})
def log1p(x: float) -> float:
    """Return log(1 + x), accurate for small x"""

    return math.log1p(x)


# Power / Root


@app.tool(title="Power (x^y)", tags={"power"})
def power(x: float, y: float) -> float:
    """Return x raised to the power y"""

    return math.pow(x, y)


@app.tool(title="Square Root", tags={"power"})
def sqrt(x: float) -> float:
    """Return the square root of x"""

    return math.sqrt(x)


@app.tool(title="Cube Root", tags={"power"})
def cbrt(x: float) -> float:
    """Return the cube root of x"""

    return math.cbrt(x)


@app.tool(title="Integer Square Root", tags={"power"})
def isqrt(x: int) -> int:
    """Return the integer square root of x"""

    return math.isqrt(x)


# Rounding


@app.tool(title="Round Up (Ceil)", tags={"rounding"})
def ceil(x: float) -> float:
    """Round x up to the nearest integer"""

    return math.ceil(x)


@app.tool(title="Round Down (Floor)", tags={"rounding"})
def floor(x: float) -> float:
    """Round x down to the nearest integer"""

    return math.floor(x)


@app.tool(title="Truncate", tags={"rounding"})
def trunc(x: float) -> int:
    """Return the truncated integer part of x (toward zero)"""

    return math.trunc(x)


@app.tool(title="Modf", tags={"rounding"})
def modf(x: float) -> tuple[float, float]:
    """Return (fractional_part, integer_part) of x. Both keep the sign of x"""

    return math.modf(x)


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


@app.tool(title="Absolute Value", tags={"number"})
def fabs(x: float) -> float:
    """Return the absolute value of x as a float"""

    return math.fabs(x)


@app.tool(title="Copy Sign", tags={"number"})
def copysign(x: float, y: float) -> float:
    """Return a float with the magnitude of x and the sign of y"""

    return math.copysign(x, y)


@app.tool(title="Float Modulo", tags={"number"})
def fmod(x: float, y: float) -> float:
    """Return the remainder of x/y, with the sign of x (platform C fmod)"""

    return math.fmod(x, y)


@app.tool(title="Remainder", tags={"number"})
def remainder(x: float, y: float) -> float:
    """Return the IEEE 754-style remainder of x with respect to y"""

    return math.remainder(x, y)


@app.tool(title="Greatest Common Divisor", tags={"number"})
def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of a and b"""

    return math.gcd(a, b)


@app.tool(title="Least Common Multiple", tags={"number"})
def lcm(a: int, b: int) -> int:
    """Return the least common multiple of a and b"""

    return math.lcm(a, b)


@app.tool(title="Fused Multiply-Add", tags={"number"})
def fma(x: float, y: float, z: float) -> float:
    """Return (x * y) + z with a single rounding (fused multiply-add)"""

    return math.fma(x, y, z)


# Distance / Norm


@app.tool(title="Euclidean Norm", tags={"geometry"})
def hypot(x: float, y: float) -> float:
    """Return the Euclidean norm sqrt(x² + y²)"""

    return math.hypot(x, y)


@app.tool(title="Euclidean Distance", tags={"geometry"})
def dist(p: list[float], q: list[float]) -> float:
    """Return the Euclidean distance between points p and q"""

    return math.dist(p, q)


# Special functions


@app.tool(title="Error Function", tags={"special"})
def erf(x: float) -> float:
    """Return the error function of x"""

    return math.erf(x)


@app.tool(title="Complementary Error Function", tags={"special"})
def erfc(x: float) -> float:
    """Return the complementary error function of x"""

    return math.erfc(x)


@app.tool(title="Gamma", tags={"special"})
def gamma(x: float) -> float:
    """Return the gamma function at x"""

    return math.gamma(x)


@app.tool(title="Log Gamma", tags={"special"})
def lgamma(x: float) -> float:
    """Return the natural logarithm of the absolute value of gamma(x)"""

    return math.lgamma(x)


# Float checks


@app.tool(title="Is Finite", tags={"check"})
def isfinite(x: float) -> bool:
    """Return True if x is finite (not inf and not NaN)"""

    return math.isfinite(x)


@app.tool(title="Is Infinite", tags={"check"})
def isinf(x: float) -> bool:
    """Return True if x is positive or negative infinity"""

    return math.isinf(x)


@app.tool(title="Is NaN", tags={"check"})
def isnan(x: float) -> bool:
    """Return True if x is NaN (Not a Number)"""

    return math.isnan(x)


@app.tool(title="Is Close", tags={"check"})
def isclose(a: float, b: float) -> bool:
    """Return True if a and b are close within a relative/absolute tolerance"""

    return math.isclose(a, b)


# Aggregate / Misc


@app.tool(title="Accurate Sum", tags={"misc"})
def fsum(values: list[float]) -> float:
    """Return an accurate floating-point sum of the values"""

    return math.fsum(values)


@app.tool(title="Product", tags={"misc"})
def prod(values: list[float]) -> float:
    """Return the product of all values, multiplied by start"""

    return math.prod(values)


@app.tool(title="Sum of Products", tags={"misc"})
def sumprod(p: list[float], q: list[float]) -> float:
    """Return the sum of products Σ p[i] * q[i]"""

    return math.sumprod(p, q)


@app.tool(title="Mantissa and Exponent", tags={"misc"})
def frexp(x: float) -> tuple[float, int]:
    """Return (m, e) such that x == m * 2**e, with 0.5 <= abs(m) < 1 (or zero)"""

    return math.frexp(x)


@app.tool(title="Load Exponent", tags={"misc"})
def ldexp(x: float, i: int) -> float:
    """Return x * (2**i). Inverse of frexp"""

    return math.ldexp(x, i)


@app.tool(title="Unit in Last Place", tags={"misc"})
def ulp(x: float) -> float:
    """Return the value of the least significant bit of x (unit in the last place)"""

    return math.ulp(x)


@app.tool(title="Next After", tags={"misc"})
def nextafter(x: float, y: float, steps: int = 1) -> float:
    """Return the float steps steps after x toward y"""

    return math.nextafter(x, y, steps=steps)
