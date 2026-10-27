# Libs
import math  # Math

from fastmcp import FastMCP  # MCP Server

# Application
from .types import Number  # Types

app = FastMCP(
    name="Math MCP Server",
    version="0.1.0",
    instructions="Provides math calculations in your Agent, Assistent or local LLM",
    website_url="math.amirhossein.info",
)


@app.tool(title="Arc Cosine")
def acos(x: Number) -> float:
    """The acos tool returns the arc cosine value of a number"""

    if not -1 <= x <= 1:
        raise ValueError("x must be in the range -1 to 1")

    return math.acos(x)


@app.tool(title="Inverse Hyperbolic Cosine")
def acosh(x: Number) -> float:
    """The acosh tool returns the inverse hyperbolic cosine of a number"""

    return math.acosh(x)


@app.tool(title="Arc Sine")
def asin(x: Number) -> float:
    """The asin tool returns the arc sine of a number"""

    return math.asin(x)


@app.tool(title="Inverse Hyperbolic Sine")
def asinh(x: Number) -> float:
    """The asinh tool returns the inverse hyperbolic sine of a number"""

    return math.asinh(x)


@app.tool(title="Arc Tangent")
def atan(x: Number) -> float:
    """The atan tool returns the arc tangent of a number (x) as a numeric value between -PI/2 and PI/2 radians"""

    return math.atan(x)


@app.tool(title="Arc Tangent of y/x")
def atan2(y: Number, x: Number) -> float:
    """The atan2 tool returns the arc tangent of y/x, in radians. Where x and y are the coordinates of a point (x,y)"""

    return math.atan2(y, x)


@app.tool(title="Inverse Hyperbolic Tangent")
def atanh(x: Number) -> float:
    """The atanh tool returns the inverse hyperbolic tangent of a number"""

    return math.atanh(x)


@app.tool(title="Ceil")
def ceil(x: Number) -> float:
    """The ceil tool rounds a number UP to the nearest integer, if necessary, and returns the result"""

    return math.ceil(x)


@app.tool(title="Cosine")
def cos(x: Number) -> float:
    """The cos tool returns the cosine of a number"""

    return math.cos(x)


@app.tool(title="Hyperbolic Cosine")
def cosh(x: Number) -> float:
    """The cosh tool returns the hyperbolic cosine of a number (equivalent to (exp(number) + exp(-number)) / 2)"""

    return math.cosh(x)


@app.tool(title="Degrees")
def degrees(x: Number) -> float:
    """The degrees method converts an angle from radians to degrees"""

    return math.degrees(x)


@app.tool(title="Floor")
def floor(x: Number) -> float:
    """The floor tool rounds a number DOWN to the nearest integer, if necessary, and returns the result"""

    return math.floor(x)


@app.tool(title="Logarithm")
def log(x: Number, y: Number) -> float:
    """The log tool returns the natural logarithm of a number, or the logarithm of number to base"""

    return math.log(x, y)


@app.tool(title="Logarithm")
def log10(x: Number) -> float:
    """The log10 tool returns the base-10 logarithm of a number"""

    return math.log10(x)


@app.tool(title="Logarithm")
def log1p(x: Number) -> float:
    """The log1p tool returns log(1+number), computed in a way that is accurate even when the value of number is close to zero"""

    return math.log1p(x)


@app.tool(title="Logarithm")
def log2(x: Number) -> float:
    """The log2 tool returns the base-2 logarithm of a number"""

    return math.log2(x)


@app.tool(title="Power")
def power(x: Number, y: Number) -> float:
    """The power tool returns the value of x raised to power y"""

    return math.pow(x, y)


@app.tool(title="Radians")
def radians(x: Number) -> float:
    """The radians tool converts a degree value into radians"""

    return math.radians(x)


@app.tool(title="Sine")
def sin(x: Number) -> float:
    """The sin tool returns the sine of a number"""

    return math.sin(x)


@app.tool(title="Hyperbolic Sine")
def sinh(x: Number) -> float:
    """The sinh tool returns the hyperbolic sine of a number"""

    return math.sinh(x)


@app.tool(title="Square Root")
def square_root(x: Number) -> float:
    """The square_root tool returns the square root of a number"""

    return math.sqrt(x)


@app.tool(title="Tangent")
def tan(x: Number) -> float:
    """The tan tool returns the tangent of a number"""

    return math.tan(x)


@app.tool(title="Hyperbolic Tangent")
def tanh(x: Number) -> float:
    """The tanh tool returns the hyperbolic tangent of a number"""

    return math.tanh(x)
