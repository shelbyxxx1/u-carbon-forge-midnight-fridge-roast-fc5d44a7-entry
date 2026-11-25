import os
import shutil
from pathlib import Path


ROAST = (
    "My smart fridge won't open after midnight. "
    "Its support bot asked if I'd tried being hungry earlier."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    for stale_path in output_dir.iterdir():
        if stale_path.is_symlink() or not stale_path.is_dir():
            stale_path.unlink()
        else:
            shutil.rmtree(stale_path)

    (output_dir / "entry.txt").write_bytes(ROAST.encode("utf-8"))


if __name__ == "__main__":
    main()
