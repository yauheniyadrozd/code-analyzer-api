# Code Clarity Analyzer API

Simple Flask REST API for analyzing Python code quality. Checks code for common clarity issues and stores results in a database.

## Features

- Analyzes Python code for clarity issues
- Scoring system (0-100 points)
- Stores analysis results in SQLite database
- Simple REST API
- Upload files or send raw code

## Quick Start

### Prerequisites

- Python 3.11+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/code-analyzer-api.git
cd code-analyzer-api
```

2. Create virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install Flask
```

4. Run the application:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### `GET /health`
Health check endpoint.

**Example:**
```bash
curl http://localhost:5000/health
```

**Response:**
```json
{
  "status": "ok"
}
```

### `POST /analyze`
Analyze code from file or JSON.

**Example (file upload):**
```bash
curl -X POST http://localhost:5000/analyze -F "file=@data/example.py"
```

**Example (JSON):**
```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"code": "def hello():\n    print(\"hi\")"}'
```

**Response:**
```json
{
  "score": 85,
  "issues": [
    "Line 4 too long",
    "Has TODO"
  ]
}
```

### `GET /reviews`
Get all stored analysis results.

**Example:**
```bash
curl http://localhost:5000/reviews
```

**Response:**
```json
{
  "reviews": [
    {
      "score": 85,
      "issues": ["Line 4 too long", "Has TODO"]
    },
    {
      "score": 100,
      "issues": []
    }
  ]
}
```

## Code Analysis Rules

The analyzer checks for:

- **Long lines** (>80 characters): -5 points per line
- **TODO comments**: -10 points
- **Base score**: 100 points

Higher score = better code clarity.

## Project Structure

```
code-analyzer-api/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── data/
│   └── example.py     # Sample code for testing
└── analyzer.db        # SQLite database (created automatically)
```

## Test

Test with the provided example file:
```bash
curl -X POST http://localhost:5000/analyze -F "file=@data/example.py"
```

Expected output:
```json
{
  "score": 85,
  "issues": ["Line 4 too long", "Has TODO"]
}
```

## Docker Support (Optional)

If you prefer to use Docker:

1. Install Docker and Docker Compose
2. Use the provided `docker-compose.yml`
3. Run: `docker-compose up -d`

## Development

To add more code checks, modify the `check_code()` function in `app.py`:

```python
def check_code(code):
    score = 100
    issues = []
    
    # Add your custom checks here
    
    return max(score, 0), issues
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## Author

Yauheniya Drozd

---

⭐ Star this repo if you find it helpful!
