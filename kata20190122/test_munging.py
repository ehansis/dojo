from kata20190122 import munging


class TestWeather:

    def test_get_columns(self):
        groups = munging.get_cols()
        assert len(groups) == 17

        assert groups['Dy']['start'] == 0
        assert groups['Dy']['num'] == 4

        assert groups['AvT']['start'] == 14
        assert groups['AvT']['num'] == 6

        assert groups['AvSLP']['start'] == 83
        assert groups['AvSLP']['num'] == 6

