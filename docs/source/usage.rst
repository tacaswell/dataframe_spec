=====
Usage
=====

To run the compliance tests in your pytest suite do the following:

.. code-block:: python

    import pytest
    from dataframe_spec.tests.test_core import *  # noqa
    from dataframe_spec.tests.conftest import (
        col_convert,       # fixture for conversion paths
        baseline           # fixture for the test data
        pytest_configure,  # define the level marker
        )

    # Define a fixture to inject a conversion function to
    # your type into the tests

    @pytest.fixture
    def df_factory(request):
        if level_marker is not None:
            (level,) = level_marker.args
        else:
            level = None

        def factory(inp: Dict[np.array]) -> YourType:
            return YourType(inp)

        return factory
