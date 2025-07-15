"""
Data storage and caching utilities for efficient data management.
"""

import pandas as pd
import os
import pickle
import h5py
from typing import Optional, Any, Dict
from pathlib import Path


class DataStorage:
    """Handle data storage operations."""
    
    def __init__(self, base_path: str = "data"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(exist_ok=True)
    
    def save_csv(self, data: pd.DataFrame, filename: str, subfolder: str = "processed") -> None:
        """Save DataFrame to CSV."""
        path = self.base_path / subfolder
        path.mkdir(exist_ok=True)
        data.to_csv(path / f"{filename}.csv")
    
    def load_csv(self, filename: str, subfolder: str = "processed") -> pd.DataFrame:
        """Load DataFrame from CSV."""
        path = self.base_path / subfolder / f"{filename}.csv"
        return pd.read_csv(path, index_col=0, parse_dates=True)
    
    def save_hdf5(self, data: pd.DataFrame, filename: str, key: str = "data", subfolder: str = "processed") -> None:
        """Save DataFrame to HDF5 format."""
        path = self.base_path / subfolder
        path.mkdir(exist_ok=True)
        data.to_hdf(path / f"{filename}.h5", key=key, mode='w')
    
    def load_hdf5(self, filename: str, key: str = "data", subfolder: str = "processed") -> pd.DataFrame:
        """Load DataFrame from HDF5 format."""
        path = self.base_path / subfolder / f"{filename}.h5"
        return pd.read_hdf(path, key=key)


class CacheManager:
    """Manage data caching for improved performance."""
    
    def __init__(self, cache_dir: str = ".cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
    
    def get(self, key: str) -> Optional[Any]:
        """Get cached data."""
        cache_file = self.cache_dir / f"{key}.pkl"
        if cache_file.exists():
            with open(cache_file, 'rb') as f:
                return pickle.load(f)
        return None
    
    def set(self, key: str, data: Any) -> None:
        """Cache data."""
        cache_file = self.cache_dir / f"{key}.pkl"
        with open(cache_file, 'wb') as f:
            pickle.dump(data, f)
    
    def clear(self, key: Optional[str] = None) -> None:
        """Clear cache."""
        if key:
            cache_file = self.cache_dir / f"{key}.pkl"
            if cache_file.exists():
                cache_file.unlink()
        else:
            # Clear all cache
            for cache_file in self.cache_dir.glob("*.pkl"):
                cache_file.unlink()