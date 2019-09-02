import textwrap


def wrap(string, max_width):
    data = textwrap.wrap(string, max_width)
    data = '\n'.join(data)

    return data
