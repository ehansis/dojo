from kata20190117 import munging


class TestWeather:

    def test_get_columns(self):
        start, num = munging.get_cols()
        assert len(start) == 17
        assert len(num) == 17

        assert start['Dy'] == 0
        assert num['Dy'] == 4

        assert start['AvT'] == 14
        assert num['AvT'] == 6

        assert start['AvSLP'] == 83
        assert num['AvSLP'] == 6

