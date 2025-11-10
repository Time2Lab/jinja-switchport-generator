import csv
from jinja2 import Template

interface_template_file = "switchport-interface-template.j2"

with open(interface_template_file) as f:
    interface_template = Template(f.read(), keep_trailing_newline=True)

with open("switch-ports.csv") as f:
    reader = csv.DictReader(f)
    # Create a dictionary to store the interface configurations for each device
    device_configs = {}
    for row in reader:
        device = row["Device"]
        # Create a new entry in the dictionary for each device, if it doesn't exist already
        if device not in device_configs:
            device_configs[device] = ""
        # Generate the interface configuration for this row using the Jinja template
        interface_config = interface_template.render(
            interface=row["Interface"],
            vlan=row["VLAN"],
            server=row["Server"],
            link=row["Link"],
            purpose=row["Purpose"]
        )
        # Append this interface configuration to the configuration for this device
        device_configs[device] += interface_config

    # Save the interface configurations for each device to a separate file
    for device, config in device_configs.items():
        with open(f"{device}-interface_configs.txt", "w") as f:
            f.write(config)
