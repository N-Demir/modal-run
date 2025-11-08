# modal-run

CLI tool to run deployed Modal functions remotely.

## Installation

```bash
pip install modal-run
```

## Usage

Run a Modal function using the format `app_name.function_name`:

```bash
modal-run app_name.function_name
```

### Example

```bash
modal-run my_app.process_data
```

This will call `modal.Function.from_name("my_app", "process_data").remote()` under the hood.

## Requirements

- Python 3.8+
- Modal account and authentication configured
