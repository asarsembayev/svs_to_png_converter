import argparse
import os
from tqdm import tqdm

import matplotlib.pyplot as plt
import slideio


IMG_SIZE = 1200

def output_png_tiles(input_path: str, output_path: str):
    """
    Convert a whole slide image to a PNG tile.

    Args:
        input_path (str): Path to the whole slide image.
        output_path (str): Path to save the PNG tile.

    Raises:
        slideio.SlideioError: If there is an error converting the image.

    """
    try:
        # Load the slide file (svs) into an object.
        slide = slideio.open_slide(input_path, 'SVS')
        scene = slide.get_scene(0)
        # Objective used to capture the image
        image = scene.read_block(size=(IMG_SIZE, 0))
        plt.imsave(output_path, image)
    except slideio.SlideioError as e:
        print(f'Failed to convert image {input_path} to {output_path} due to {e}')


def main(src_dir: str, dst_dir: str, output_format: str = '.png'):
    
    """
    Convert all whole slide images in a directory to PNG tiles.

    Args:
        src_dir (str): Path to the directory containing the whole slide images.
        dst_dir (str): Path to the output directory to save the PNG tiles.

    """
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir, exist_ok=True)
        print('Created', dst_dir)

    image_names = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]

    for image_name in tqdm(image_names):
        assert image_name.endswith('.svs'), f'Invalid image format: {image_name}. Only SVS images are supported.'
        full_image_path = os.path.join(src_dir, image_name)
        image_name_without_extension = os.path.splitext(image_name)[0]
        output_path = os.path.join(dst_dir, image_name_without_extension + output_format)
        assert output_format in ['.png', '.jpeg'], f'Invalid output format: {output_format}. Only PNG and JPEG are supported.'
        output_png_tiles(full_image_path, output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert whole slide images to JPEG tiles")
    parser.add_argument("src_dir", type=str, help="Path to the whole slide image")
    parser.add_argument("dst_dir", type=str, help="Path to the output directory")
    parser.add_argument("--output_format", type=str, help="Output image format {png, jpeg}", default=".png")

    args = parser.parse_args()

    main(args.src_dir, args.dst_dir, args.output_format)
