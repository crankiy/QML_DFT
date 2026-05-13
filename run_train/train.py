import argparse
import os
import sys
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]

from qml_dft_core import load_runtime_config

def main():
    parser = argparse.ArgumentParser(description="Train a model using the specified configuration.")
    parser.add_argument("config_path", type=str, help="Path to the runtime configuration file.")
    args = parser.parse_args()

    config_path = Path(args.config_path)
    if not config_path.is_file():
        print(f"Error: Configuration file '{config_path}' does not exist.")
        sys.exit(1)

    runtime_config = load_runtime_config(config_path)

    # Here you would add the code to initialize and train your model using the runtime_config
    print("Runtime configuration loaded successfully:")
    print(runtime_config)

if __name__ == "__main__":
    main()