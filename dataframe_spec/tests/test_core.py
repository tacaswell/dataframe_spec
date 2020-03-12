import numpy as np
import pytest

_test_slices = [
    slice(None),
    slice(2),
    slice(-3, -2),
    # slice(None, None, -1),   # reverse slicing is a bit goofy?
    slice(0, 3, 2),
]


class TestDictLike:
    def test_list(self, df_factory, baseline):
        "This tests that iteration on the ProtoFrame behaves like a dict"
        df = df_factory(baseline)
        assert set(df) == set(baseline)

    def test_contains(self, df_factory, baseline):
        "This tests that contains on the ProtoFrame behaves like a dict"
        df = df_factory(baseline)
        for n in df:
            assert n in df
            assert n in baseline

    def test_items(self, df_factory, baseline, col_convert):
        "This tests that .items() works as expected"
        df = df_factory(baseline)
        for (tk, tv) in df.items():
            assert np.all(col_convert(tv) == baseline[tk])

    def test_values(self, df_factory, baseline, col_convert):
        "This tests that .values() works as expected"
        df = df_factory(baseline)
        for tv in df.values():
            # so far just a smoke test
            col_convert(tv)

    def test_keys(self, df_factory, baseline, col_convert):
        "This tests that .keys() works as expected"
        df = df_factory(baseline)
        assert set(df.keys()) == set(baseline.keys())

    def test_len(self, df_factory, baseline):
        "This tests that length follows abc.Mapping semantics"
        df = df_factory(baseline)
        assert len(df) == len(baseline)
        assert len(df) == len(list(df))

    @pytest.mark.xfail(reason="Equality is hard")
    def test_eq(self, df_factory, baseline):
        df1 = df_factory(baseline)
        df2 = df_factory(baseline)
        assert df1 == df2
        assert not df1 != df2


class TestCols:
    def test_col_len(self, df_factory, baseline):
        "This tests that all columns are the same length"
        df = df_factory(baseline)
        first_col_len = None
        for n in df:
            if first_col_len is None:
                first_col_len = len(df[n])
            assert len(df[n]) == len(baseline[n])
            assert len(df[n]) == first_col_len

    @pytest.mark.parametrize("slc", _test_slices)
    def test_slicing(self, df_factory, baseline, slc, col_convert):
        "Test that basic slicing works "
        df = df_factory(baseline)
        for n in df:
            test = col_convert(df[n][slc])
            assert test.ndim == 1
            assert np.all(test == baseline[n][slc])

    @pytest.mark.level(1)
    def test_binary_mask(self, df_factory, baseline, col_convert):
        "Test that bool mask selection works."
        df = df_factory(baseline)
        for n in df:
            col = baseline[n]
            slc = np.zeros_like(col, dtype=bool)
            slc[::2] = True
            test = col_convert(df[n][slc])
            assert np.all(test == baseline[n][slc])
