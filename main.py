# Libs
from typing import Annotated  # Types
import math  # Math

from fastmcp import FastMCP  # MCP Server
from pydantic import Field  # Pydantic

# Create MCP Server
app = FastMCP(
    name="Math MCP Server",
    version="0.1.0",
    instructions="Provides math calculations in your Agent, Assistent or local LLM",
    website_url="math.amirhossein.info",
)


@app.tool(
    name="square_root",
    title="Square Root",
    description="Get square root of a number",
)
def square_root(
    x: Annotated[float, Field(description="A float number")],
) -> float:
    """The square_root tool returns the square root of a number

    Args:
        - x: A number to find the square root of
    """

    return math.sqrt(x)


@app.tool(
    title="Power",
)
def power(
    x: Annotated[float, Field(description="A float number")],
    y: Annotated[float, Field(description="A float number")],
) -> float:
    """The power tool returns the value of x raised to power y

    Args:
        - x: A number which represents the base
        - y: A number which represents the exponent
    """

    return math.pow(x, y)


@app.tool(title="arc cosine value of x")
def acos(
    x: Annotated[float, Field(description="A float number")],
) -> float:
    """
    The acos tool returns the arc cosine value of a number

    Args:
        - x: A number in the range -1 to 1
    """

    if not -1 <= x <= 1:
        raise ValueError("x must be in the range -1 to 1")

    return math.acos(x)


@app.tool(title="inverse hyperbolic cosine of x")
def acosh(
    x: Annotated[float, Field(description="A float number")],
) -> float:
    """
    The acosh tool returns the inverse hyperbolic cosine of a number

    Note: The parameter passed in acosh must be greater than or equal to 1.

    Args:
        - x: Required. A positive number >= 1
    """

    return math.acosh(x)


@app.tool(title="arc sine of a x")
def asin(
    x: Annotated[float, Field(description="A float number")],
) -> float:
    """
    The asin tool returns the arc sine of a number

    Note: The parameter passed in asin must lie between -1 to 1.
    Tip: asin will return the value of PI/2, and asin of -1 will return the value of -PI/2.

    Args:
        - x: Required. A number in the range -1 to 1
    """

    return math.asin(x)


@app.tool(title="inverse hyperbolic sine of x")
def asinh(
    x: Annotated[float, Field(description="A float number")],
) -> float:
    """
    The asinh tool returns the inverse hyperbolic sine of a number

    Args:
        - x: Required. A positive or negative number
    """

    return math.asinh(x)


@app.tool(title="arc tangent of x")
def atan(
    x: Annotated[float, Field(description="A float number")],
) -> float:
    """
    The atan tool returns the arc tangent of a number (x) as a numeric value between -PI/2 and PI/2 radians

    Arc tangent is also defined as an inverse tangent function of x, where x is the value of the arc tangent is to be calculated.

    Args:
        - x: Required. A positive or negative number
    """

    return math.atan(x)


@app.tool(title="arc tangent of x and y")
def atan2(
    y: Annotated[float, Field(description="A float number")],
    x: Annotated[float, Field(description="A float number")],
) -> float:
    """
    The atan2 tool returns the arc tangent of y/x, in radians. Where x and y are the coordinates of a point (x,y)

    The returned value is between PI and -PI.

    Args:
        - x: Required. Specifies a positive or negative number
        - y: Required. Specifies a positive or negative number
    """

    return math.atan2(x, y)


@app.tool(title="inverse hyperbolic tangent of x")
def atanh(
    x: Annotated[float, Field(description="A float number")],
) -> float:
    """
    The atanh tool returns the inverse hyperbolic tangent of a number

    Note: The parameter passed in atanh must lie between -0.99 to 0.99.

    Args:
        - x: Required. A positive or negative number between -0.99 and 0.99
    """

    return math.atanh(x)


@app.tool(title="round up x")
def ceil(
    x: Annotated[float, Field(description="A float number")],
) -> float:
    """
    The ceil tool rounds a number UP to the nearest integer, if necessary, and returns the result

    Tip: To round a number DOWN to the nearest integer, look at the floor tool.

    Args:
        - x: Required. Specifies the number to round up
    """

    return math.ceil(x)


@app.tool(title="round down x")
def floor(
    x: Annotated[float, Field(description="A float number")],
) -> float:
    """
    The floor tool rounds a number DOWN to the nearest integer, if necessary, and returns the result

    Tip: To round a number UP to the nearest integer, look at the ceil tool.

    Args:
        - x: Required. Specifies the number to round down
    """

    return math.floor(x)


@app.tool(title="cosine of x")
def cos(
    x: Annotated[float, Field(description="A float number")],
) -> float:
    """
    The cos tool returns the cosine of a number

    Args:
        - x: Required. A number to find the cosine of
    """

    return math.cos(x)


@app.tool(title="hyperbolic cosine of x")
def cosh(
    x: Annotated[float, Field(description="A float number")],
) -> float:
    """
    The cosh tool returns the hyperbolic cosine of a number (equivalent to (exp(number) + exp(-number)) / 2)

    Args:
        - x: Required. A number to find the hyperbolic cosine of
    """

    return math.cosh(x)
