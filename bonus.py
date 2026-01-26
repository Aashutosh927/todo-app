contents = ["Municipality is organising the training session for their employees.",
            "The tutor is gonna present the slides of the training course.",
            "The report must be submitted by this Friday to the Ward Secretary of Municipality."]

filenames = ["doc.txt", 'presentation.txt', 'report.txt']

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)