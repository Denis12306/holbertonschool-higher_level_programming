"""In this task, you will create a Python function that generates personalized
invitation files from a template with placeholders and a list of objects.
Each output file should be named sequentially, starting from 1.
You will also implement specific error handling for various edge
cases.def generate_invitations(template, attendees):"""
def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for i, person in enumerate(attendees, start=1):
        name = person.get("name") or "N/A"
        title = person.get("event_title") or "N/A"
        date = person.get("event_date") or "N/A"
        location = person.get("event_location") or "N/A"

        output = template
        output = output.replace("{name}", name)
        output = output.replace("{event_title}", title)
        output = output.replace("{event_date}", date)
        output = output.replace("{event_location}", location)

        filename = f"output_{i}.txt"
        try:
            with open(filename, "w") as file:
                file.write(output)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
