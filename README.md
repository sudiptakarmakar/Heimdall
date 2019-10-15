# Heimdall

Heimdall is a template for easy to start flask application

## Installation

No installation required so far. Clone and install dependencies with python3

```bash
pip3 install -r requirements.txt
```

## Usage

```python
from heimdall import create_app

app = create_app(env='dev')  # build a flask app suitable for dev environment
app.run(port=5000, debug=True)  # run with desired flags
```

## Contributing

Not open for now. Need some cleanup first.

## License
[MIT](https://choosealicense.com/licenses/mit/)
