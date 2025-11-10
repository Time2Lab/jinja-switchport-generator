import csv
import os
from jinja2 import Template

# Jinja template file name
interface_template_file = "Cisco-switchport-interface-template.j2"

# Load the Jinja template
with open(interface_template_file) as f:
    interface_template = Template(f.read(), keep_trailing_newline=True)

# Make sure we have an output directory
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Read the CSV and build configs per device
with open("switch-ports.csv", newline="") as f:
    reader = csv.DictReader(f)

    # Dictionary to hold all configs per device
    device_configs = {}

    for row in reader:
        # Strip whitespace from CSV fields just in case
        device = row["Device"].strip()
        interface = row["Interface"].strip()
        vlan = row["VLAN"].strip()
        server = row["Server"].strip()
        link = row["Link"].strip()
        purpose = row["Purpose"].strip()

        # Make sure the device key exists
        if device not in device_configs:
            device_configs[device] = ""

        # Render the template for this interface
        interface_config = interface_template.render(
            interface=interface,
            vlan=vlan,
            server=server,
            link=link,
            purpose=purpose,
        )

        # Append to this device's config text
        device_configs[device] += interface_config

# Write one file per device
for device, config in device_configs.items():
    output_path = os.path.join(output_dir, f"{device}-interface_configs.txt")
    with open(output_path, "w") as out_f:
        out_f.write(config)

print("Config files generated in ./output")
