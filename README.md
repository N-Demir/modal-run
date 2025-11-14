# modal-run

Simple tool to run deployed Modal functions from the CLI. 

## Installation

```bash
pip install modal-run
```

## Usage

```bash
modal-run my_app.my_function
```

This will call `modal.Function.from_name("my_app", "my_function").spawn()` under the hood.

```bash
modal-run my_app.function_name --an-arg my_arg
```

This will call `modal.Function.from_name("my_app", "function_name").spawn(an_arg: "ny_arg")` under the hood.

## Requirements

- Python 3.8+
- Modal account and authentication configured
