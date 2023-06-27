from PIL import Image
import numpy as np
import click


FFF = [255, 225, 225]


@click.command()
@click.option('--height', default=500, help='The height of the generated image.')
@click.option('--width', default=1000, help='The width of the generated image.')
@click.option('--columns', default=1000, help='The number of columns in the generated image.')
def generate(height, width, columns):
    """
    Generate the image using the provided parameters.
    """
    number_of_columns = columns
    shape = (height, width, 3)
    data = np.zeros(shape, dtype=np.uint8)

    column_width = int(width / number_of_columns)

    column_offset = 0

    for column_number in range(0, number_of_columns):

        if column_number == 0:
            continue

        is_even_column = column_number % 2 == 0

        column_offset += column_width

        shape_width = column_width * (column_number + 1)

        even = column_number % 2

        if is_even_column:
            y = int(height / column_number + 2)
        else:
            y = 0

        for section_number in range(even, column_number + 2):

            shape_height = int(height / column_number + 2) + y

            if section_number > 1:
                if not section_number % 2 == 0:
                    y += int(height / column_number + 2) * 2

            data[y:shape_height, column_offset:shape_width] = FFF

    img = Image.fromarray(data, 'RGB')
    img.save(f'samples/{number_of_columns}.jpg')


if __name__ == '__main__':
    generate()
