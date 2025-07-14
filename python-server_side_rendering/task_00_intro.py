from os.path import exists

def generate_invitations (template, attendees):
    if not isinstance(template, str):
