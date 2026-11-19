import pathlib
import shutil


def main():
    base_dir = pathlib.Path(__file__).resolve().parent
    art_path = base_dir / "art.jpg"
    output_dir_env = shutil.os.environ.get("MAKEFUN_OUTPUT_DIR")
    output_dir = pathlib.Path(output_dir_env if output_dir_env else "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(art_path, output_dir / "entry.png")


if __name__ == "__main__":
    main()
