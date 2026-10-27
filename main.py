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


@app.tool(title="Arc Cosine")
def acos(x: Number) -> float:
    """Return the arc cosine of x in radians. x ∈ [-1, 1]"""

    if not -1 <= x <= 1:
        raise ValueError("x must be in the range -1 to 1")

    return math.acos(x)


@app.tool(title="Inverse Hyperbolic Cosine")
def acosh(x: Number) -> float:
    """Return the inverse hyperbolic cosine of x. x ≥ 1"""

    return math.acosh(x)


@app.tool(title="Arc Sine")
def asin(x: Number) -> float:
    """Return the arc sine of x in radians. x ∈ [-1, 1]"""

    return math.asin(x)


@app.tool(title="Inverse Hyperbolic Sine")
def asinh(x: Number) -> float:
    """Return the inverse hyperbolic sine of x"""

    return math.asinh(x)


@app.tool(title="Arc Tangent")
def atan(x: Number) -> float:
    """Return the arc tangent of x in radians, in (-π/2, π/2)"""

    return math.atan(x)


@app.tool(title="Arc Tangent of y/x")
def atan2(y: Number, x: Number) -> float:
    """Return atan2(y, x) in radians, in (-π, π]"""

    return math.atan2(y, x)


@app.tool(title="Inverse Hyperbolic Tangent")
def atanh(x: Number) -> float:
    """Return the inverse hyperbolic tangent of x. x ∈ (-1, 1)"""

    return math.atanh(x)


@app.tool(title="Round Up (Ceil)")
def ceil(x: Number) -> float:
    """Round x up to the nearest integer"""

    return math.ceil(x)


@app.tool(title="Cosine")
def cos(x: Number) -> float:
    """Return the cosine of x"""

    return math.cos(x)


@app.tool(title="Hyperbolic Cosine")
def cosh(x: Number) -> float:
    """Return the hyperbolic cosine of x"""

    return math.cosh(x)


@app.tool(title="Radians to Degrees")
def degrees(x: Number) -> float:
    """Convert angle x from radians to degrees"""

    return math.degrees(x)


@app.tool(title="Round Down (Floor)")
def floor(x: Number) -> float:
    """Round x down to the nearest integer"""

    return math.floor(x)


@app.tool(title="Base Logarithm")
def log(x: Number, base: Number) -> float:
    """Return log of x with base y (natural log if you document it that way)"""

    return math.log(x, base)


@app.tool(title="Base-10 Logarithm")
def log10(x: Number) -> float:
    """Return the base-10 logarithm of x"""

    return math.log10(x)


@app.tool(title="Log of 1+x")
def log1p(x: Number) -> float:
    """Return log(1 + x), accurate for small x"""

    return math.log1p(x)


@app.tool(title="Base-2 Logarithm")
def log2(x: Number) -> float:
    """Return the base-2 logarithm of x"""

    return math.log2(x)


@app.tool(title="Power (x^y)")
def power(x: Number, y: Number) -> float:
    """Return x raised to the power y"""

    return math.pow(x, y)


@app.tool(title="Degrees to Radians")
def radians(x: Number) -> float:
    """Convert angle x from degrees to radians"""

    return math.radians(x)


@app.tool(title="Sine")
def sin(x: Number) -> float:
    """Return the sine of x"""

    return math.sin(x)


@app.tool(title="Hyperbolic Sine")
def sinh(x: Number) -> float:
    """Return the hyperbolic sine of x"""

    return math.sinh(x)


@app.tool(title="Square Root")
def square_root(x: Number) -> float:
    """Return the square root of x"""

    return math.sqrt(x)


@app.tool(title="Tangent")
def tan(x: Number) -> float:
    """Return the tangent of x"""

    return math.tan(x)


@app.tool(title="Hyperbolic Tangent")
def tanh(x: Number) -> float:
    """Return the hyperbolic tangent of x"""

    return math.tanh(x)
