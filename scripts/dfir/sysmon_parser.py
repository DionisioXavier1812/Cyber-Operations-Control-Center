import xml.etree.ElementTree as ET

tree = ET.parse("logs/sysmon.xml")
root = tree.getroot()

for event in root.findall(".//Event"):
    event_id = event.find(".//EventID").text
    if event_id == "1":  # Process creation
        process = event.find(".//Image").text
        parent = event.find(".//ParentImage").text
        print(f"Processo criado: {process} | Pai: {parent}")
