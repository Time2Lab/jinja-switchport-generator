# Jinja Switchport Generator

This project generates switch interface configuration from a CSV file using a Jinja2 template. It’s meant for small labs or repeatable builds where you don’t want to hand-type every `interface` block.

## Features

- Read interface definitions from `switch-ports.csv`
- Render per-interface configs using a Jinja2 template
- Group interfaces by device and write **one config file per switch** (e.g. `Switch-1-interface_configs.txt`)
- Outputs to an `output/` directory so generated files don’t clutter the repo

## Requirements

- Python 3.x
- [Jinja2](https://palletsprojects.com/p/jinja/)
  
Install Jinja2:

```bash
python3 -m pip install jinja2
