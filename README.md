# Table Detector

This project uses the `TahaDouaji/detr-doc-table-detection` model to detect tables in invoice and bank document images.
https://huggingface.co/TahaDouaji/detr-doc-table-detection

## Setup

### Docker

1. Build the Docker image:

    ```bash
    docker build -t table-detector .
    ```

2. Run the Docker container:

    ```bash
    docker run --rm table-detector
    ```

### Local

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
2. Unzip test_data:

    ```bash
    bash data.sh
    ```

3. Run tests:

    ```bash
    pytest
    ```

## Usage

To use the `Detector` class:

```python
from detector import Detector

detector = Detector()
tables = detector.predict("path/to/your/image.jpeg")
print(tables)
```

## Test data

To test differents scenarios success extraction or error extraction table on bank document or invoice , I use an image of an invoice, an image of a random text (with no tables), and an invalid path.


