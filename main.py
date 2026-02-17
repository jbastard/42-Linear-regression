from pathlib import Path
import sys


def _bootstrap_path() -> None:
    src_path = Path(__file__).resolve().parent / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))


def main() -> None:
    _bootstrap_path()
    from linear_regression.app.cli import main as cli_main

    cli_main()


if __name__ == "__main__":
    main()
