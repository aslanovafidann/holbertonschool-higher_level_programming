#!/usr/bin/env python3
import os
import logging

# Set up logging
logging.basicConfig(level=logging.ERROR, format='%(message)s')

def generate_invitations(template, attendees):
    # Input validation
    if not isinstance(template, str):
        logging.error("Invalid input: template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid input: attendees should be a list of dictionaries.")
        return

    # Check if template is empty
    if template.strip() == "":
        logging.error("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        # Create a copy of template
        filled_template = template
        # Replace placeholders
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            filled_template = filled_template.replace(f'{{{key}}}', str(value))
        
        # Output file name
        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, 'w') as f:
                f.write(filled_template)
        except Exception as e:
            logging.error(f"Failed to write file {output_filename}: {e}")

