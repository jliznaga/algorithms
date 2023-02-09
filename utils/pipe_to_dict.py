import csv
csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)

FILE_PATH = './inputs/pipe_to_dict'


def pipe_to_dict(file_path):
    with open(file_path, "r") as csvfile:
        for row in csv.DictReader(csvfile, dialect='piper'):
            print(row['name'])


# assert pipe_to_dict(FILE_PATH) == ''
pipe_to_dict(FILE_PATH)
