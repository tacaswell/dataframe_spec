import pytest
from .test_core import *  # noqa


def _list_factory(inp):
    return {k: list(v) for k, v in inp.items()}


@pytest.fixture
def df_factory(request):
    def __dataframe__(inp):
        return inp

    def factory(inp):
        return __dataframe__(_list_factory(inp))

    level_marker = request.node.get_closest_marker("level")
    if level_marker is not None:
        (level,) = level_marker.args
        if level > 0:
            pytest.skip("dict of lists only supports level 0 not " f"level {level}")
    return factory
