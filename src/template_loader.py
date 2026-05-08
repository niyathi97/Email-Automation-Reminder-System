def load_template(template_path):

    with open(template_path, "r") as file:
        template = file.read()

    return template