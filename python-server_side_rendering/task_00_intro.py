import os

def generate_invitations(template: str, attendees: list[dict]):
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: attendees should be a list of dictionaries.")
        return
    
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for index, item in enumerate(attendees, start=1):
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            placeholder = f"{{key}}"
            value = item.get(key)
            if value in None:
                value = "N/A"
            template = template.replace(placeholder, value)
            
            if not os.path.exists(f"output_{index}.txt"):
                try:
                    with open(f"output_{index}.txt", "w") as file:
                        file.write(template)
                        print("Succesfully written to the {}".format(f"output_{index}.txt)"))
                except Exception as e:
                    print("Error writen to file {}: {}".format(f"output_{index}.txt)", e))