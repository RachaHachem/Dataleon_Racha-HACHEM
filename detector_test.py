import pytest
from detector import Detector
import os

@pytest.fixture
def detector():
    return Detector()

def test_successful_table_detection(detector):
    image_path = "./test_data/valid-invoice.jpeg"
    tables = detector.predict(image_path)
    assert len(tables) > 0  # ensure tables are detected
    assert all('box' in table for table in tables)
    assert all('score' in table for table in tables)
    assert all('label' in table for table in tables)

def test_no_table_detection(detector):
    image_path = "./test_data/random-image.jpeg"
    with pytest.raises(ValueError, match="No tables detected"):
        detector.predict(image_path)

def test_invalid_image_path(detector):
    image_path = "./test_data/invalid-path.jpg"
    with pytest.raises(ValueError, match="Could not open image"):
        detector.predict(image_path)
