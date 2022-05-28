"""Tests for Image Sequence object."""

from image_sequence import __version__
from image_sequence.image_sequence import sequence


def test_version():
    """Test module version."""
    assert __version__ == "0.1.0"


def test_sequence():
    """Test pytest"""
    assert sequence() == [1, 2, 3]
