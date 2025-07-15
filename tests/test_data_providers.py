"""
Test suite for data providers.
"""

import pytest
import pandas as pd
from quantpak.data.providers import YahooProvider, BaseProvider


class TestYahooProvider:
    """Test cases for Yahoo Finance data provider."""
    
    def test_yahoo_provider_initialization(self):
        """Test that YahooProvider can be initialized."""
        provider = YahooProvider()
        assert provider.name == "Yahoo Finance"
    
    def test_yahoo_provider_inheritance(self):
        """Test that YahooProvider inherits from BaseProvider."""
        provider = YahooProvider()
        assert isinstance(provider, BaseProvider)
    
    @pytest.mark.skip(reason="Requires internet connection")
    def test_get_data_single_symbol(self):
        """Test fetching data for a single symbol."""
        provider = YahooProvider()
        data = provider.get_data('AAPL', period='5d')
        
        assert isinstance(data, pd.DataFrame)
        assert not data.empty
        assert 'Close' in data.columns
        assert 'Volume' in data.columns
    
    @pytest.mark.skip(reason="Requires internet connection")  
    def test_get_data_multiple_symbols(self):
        """Test fetching data for multiple symbols."""
        provider = YahooProvider()
        data = provider.get_data(['AAPL', 'GOOGL'], period='5d')
        
        assert isinstance(data, pd.DataFrame)
        assert not data.empty


class TestBaseProvider:
    """Test cases for the base provider class."""
    
    def test_base_provider_is_abstract(self):
        """Test that BaseProvider cannot be instantiated directly."""
        with pytest.raises(TypeError):
            BaseProvider()