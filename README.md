# Math MCP

I'll say what is this later...

## Run

Here is how to run the project.

### HTTP

Using **HTTTP** is like this:

```bash
uv run fastmcp run main.py:app --transport http
```

### STDIO

If you want to use **STDIO**:

```bash
uv run fastmcp run main.py:app --transport stdio
```

### Docker

Well, you are a pro:

```bash
docker build -t math-mcp:stdio .
```
