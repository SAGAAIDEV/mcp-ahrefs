"""Main module for MCP Ahrefs MCP server.

This module allows the server to be run as a Python module using:
python -m mcp_ahrefs

It delegates to the server application's main function.
"""

from mcp_ahrefs.server.app import main

if __name__ == "__main__":
    main()