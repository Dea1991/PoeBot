



def read_lines_from_big_file(path):
    with open(path) as fp:
        for line in fp:
            parts = line.split()
            yield parts  # -> ['1.', '27.01.1957', '8,12,31,39,43,45']

for split_line in read_lines_from_big_file(path):
    # do something with split_line