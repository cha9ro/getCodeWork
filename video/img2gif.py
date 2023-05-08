import glob
from PIL import Image


def make_gif(folder_path: str) -> None:
    """This creates a gif from multiple pictures in the same directory.

    Args:
        folder_path (str): Absolute folder path in which the pictures are saved.
    """
    frames = [Image.open(img) for img in glob.glob(f"{folder_path}/*.JPG")]
    frames[0].save(
        f"{folder_path}/output.gif",
        format="GIF",
        append_images=frames,
        save_all=True,
        duration=500,
        loop=0,
    )


def main():
    FOLDER_PATH = "/Users/takuro/Documents/pics"
    make_gif(FOLDER_PATH)


if __name__ == "__main__":
    main()
