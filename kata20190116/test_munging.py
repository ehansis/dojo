from kata20190116 import munging


class TestWeather:

    def test_loader(self):
        df = munging.weather()
        assert len(df) == 30
        assert df['MxT'].dtype == float
        assert df['MxT'].isnull().sum() == 0
        assert df['MnT'].dtype == float
        assert df['MnT'].isnull().sum() == 0

    def test_analyze(self):
        d = munging.analyze(munging.weather())
        assert d == 9
