import pytest
import numpy as np

_test_cases = [
    {
        "a": np.array([1, 2, 3]),
        "b": np.array(["a", "b", "c"], dtype="S"),
        "c": np.array([1.0, 2.0, 3.0]),
    },
    {
        "a": np.array([1, 2, 3]),
        "b": np.array(["a", "b", "c"]),
        "c": np.array([1.0, 2.0, 3.0]),
    },
    {"a": np.array([1, 2, 3]), "c": np.array([1.0, 2.0, 3.0])},
]


def _echo_factory(inp):
    return inp


def _pandas_factory(inp):
    pd = pytest.importorskip("pandas")
    df = pd.DataFrame(inp)
    return {k: df[k] for k in df}


@pytest.fixture(params=[_echo_factory, _pandas_factory], ids=["echo", "pandas"])
def df_factory(request):
    def __dataframe__(inp):
        return inp

    def factory(inp):
        return __dataframe__(request.param(inp))

    return factory


@pytest.fixture(params=_test_cases)
def baseline(request):
    return request.param


def _try_to_numpy(x):
    try:
        return x.to_numpy()
    except AttributeError:
        pytest.xfail(f"{type(x)} does not support obj.to_numpy yet")


_test_converters = [
    lambda x: np.asarray(x),
    # assume we can put `to_numpy` on numpy
    _try_to_numpy,
]


@pytest.fixture(params=_test_converters, ids=["arrayprotocol", "to_numpy"])
def col_convert(request):
    return request.param


def pytest_configure(config):
    for key, value in [
        ("markers", "level: The spec level the test is testing"),
    ]:
        config.addinivalue_line(key, value)
