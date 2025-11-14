"""CLI implementation for modal-run."""

import typer
from click import Context
from modal import Function

app = typer.Typer()


@app.command(
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def main(
    ctx: Context,
    function_path: str = typer.Argument(
        ..., help="Modal function path in format app_name.function_name"
    ),
):
    """Run a Modal function using spawn.

    Args:
        function_path: The function path in format app_name.function_name
        Additional kwargs can be passed as --key value (e.g., --data-str my_data_str)
    """
    if "." not in function_path:
        typer.echo(
            f"Error: Invalid format. Expected 'app_name.function_name', got '{function_path}'",
            err=True,
        )
        raise typer.Exit(1)

    parts = function_path.split(".", 1)
    if len(parts) != 2:
        typer.echo(
            f"Error: Invalid format. Expected 'app_name.function_name', got '{function_path}'",
            err=True,
        )
        raise typer.Exit(1)

    app_name, function_name = parts

    # Parse additional arguments from context
    kwargs = {}
    # Parse remaining args as key-value pairs
    remaining_args = ctx.args
    i = 0
    while i < len(remaining_args):
        arg = remaining_args[i]
        if arg.startswith("--"):
            key = arg[2:].replace("-", "_")  # Convert --data-str to data_str
            if i + 1 < len(remaining_args) and not remaining_args[i + 1].startswith(
                "--"
            ):
                value = remaining_args[i + 1]
                kwargs[key] = value
                i += 2
            else:
                # Boolean flag (no value)
                kwargs[key] = True
                i += 1
        else:
            i += 1

    try:
        func = Function.from_name(app_name, function_name)
        func.spawn(**kwargs) if kwargs else func.spawn()
        typer.echo("Function spawned")
    except Exception as e:
        typer.echo(f"Error executing function: {e}", err=True)
        raise typer.Exit(1)


def cli():
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    cli()
