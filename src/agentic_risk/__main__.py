"""Run the offline scripted pilot: python -m agentic_risk --help."""

import argparse

from .engine import run_experiment


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a deterministic synthetic authority/verification experiment.")
    parser.add_argument("--config", required=True, help="Path to a TOML experiment configuration")
    parser.add_argument("--output", required=True, help="New output directory (existing directories are refused)")
    arguments = parser.parse_args()
    try:
        output = run_experiment(arguments.config, arguments.output)
    except (ValueError, OSError) as error:
        parser.error(str(error))
    print(f"Results written to {output}")


if __name__ == "__main__":
    main()
