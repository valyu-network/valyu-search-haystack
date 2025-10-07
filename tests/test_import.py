"""Basic import tests to verify package structure."""


def test_import_components():
    """Test that components can be imported."""
    from valyu_haystack import ValyuSearch, ValyuContentFetcher

    assert ValyuSearch is not None
    assert ValyuContentFetcher is not None


def test_version():
    """Test that version can be imported."""
    from valyu_haystack import __version__

    assert __version__ is not None
    assert isinstance(__version__, str)


def test_component_initialization():
    """Test that components can be instantiated."""
    from valyu_haystack import ValyuSearch, ValyuContentFetcher
    from haystack.utils import Secret

    # Should not raise errors
    search = ValyuSearch(api_key=Secret.from_token("test-key"))
    fetcher = ValyuContentFetcher(api_key=Secret.from_token("test-key"))

    assert search is not None
    assert fetcher is not None
