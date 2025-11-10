import csv
import os
from jinja2 import Template

# ask user which csv to use
csv_file = input("Enter CSV filename (default: switch-ports-example.csv): ").strip()
if not csv_file:
    csv_file = "switch-ports-example.csv"

# ask user which Jinja2 Template to use
template_file = input("Enter J2 filename (default: Cisco-switchport-interface-template.j2): ").strip()
if not csv_file:
    csv_file = "Cisco-switchport-interface-template.j2"

# load template
with open(template_file) as f:
    interface_template = Template(f.read(), keep_trailing_newline=True)

# make output dir
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

device_configs = {}

with open(csv_file, newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        device = row["Device"].strip()
        interface = row["Interface"].strip()
        vlan = row["VLAN"].strip()
        server = row["Server"].strip()
        link = row["Link"].strip()
        purpose = row["Purpose"].strip()

        if device not in device_configs:
            device_configs[device] = ""

        interface_config = interface_template.render(
            interface=interface,
            vlan=vlan,
            server=server,
            link=link,
            purpose=purpose,
        )

        device_configs[device] += interface_config

# write per-device files
for device, config in device_configs.items():
    out_path = os.path.join(output_dir, f"{device}-interface_configs.txt")
    with open(out_path, "w") as f:
        f.write(config)

print(f"Configs written to {output_dir}/")
