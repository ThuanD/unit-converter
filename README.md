# Unit Converter Web Application

## Overview
This is a Python Flask-based web application that allows users to convert between different units of measurement, including length, weight, and temperature.

_Note: This project is part of the Roadmap Projects: https://roadmap.sh/projects/unit-converter_

## Features
- Convert units of length (mm, cm, m, km, inch, foot, yard, mile)
- Convert units of weight (mg, g, kg, ounce, pound)
- Convert temperature units (Celsius, Fahrenheit, Kelvin)
- Simple, user-friendly web interface
- No database required

## Prerequisites
- Python 3.8+
- Flask
- Pytest (for testing)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ThuanD/unit-converter.git
cd unit-converter
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install flask pytest
```

## Running the Application
```bash
python app.py
```

Open a web browser and navigate to `http://localhost:5000`

## Running Tests
```bash
pytest tests/
```

## License

This project is released under the MIT License.

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact & Support

Found an issue? Please open a GitHub issue with detailed information.

Project Link: [https://github.com/ThuanD/unit-converter](https://github.com/ThuanD/unit-converter)