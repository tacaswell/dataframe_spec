import pytest
from .test_core import *  # noqa


def _h5_factory(inp):
    h5py = pytest.importorskip("h5py")
    import io

    fh = io.BytesIO()
    f = h5py.File(fh, mode="w")
    for k, v in inp.items():
        try:
            f[k] = v
        except TypeError:
            raise pytest.skip("type not supported by h5py")
    return f["/"]


@pytest.fixture
def df_factory(request):
    def __dataframe__(inp):
        return inp

    def factory(inp):
        return __dataframe__(_h5_factory(inp))

    return factory
