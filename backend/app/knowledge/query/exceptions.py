class GraphQueryError(Exception):
    """Base exception for graph query failures."""

    pass


class GraphNodeNotFoundError(GraphQueryError):
    """Raised when a graph node cannot be found."""

    pass


class InvalidTraversalDepthError(GraphQueryError):
    """Raised when traversal depth is invalid."""

    pass
