"""

Copy papers from one directory to another based on the Status given in the yaml frontmatter.
"""

import os
import re
import shutil
from asyncio.log import logger

import yaml

STATUS_KEY = "Status"
STATUS_VALUE = "Data coded"

databook_dir = "./Databook"
destination_dir = "./CodedPapers"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(content: str) -> dict:
    """Parse the YAML frontmatter block from a Databook .md file, if present."""
    m = FRONTMATTER_RE.match(content)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        logger.warning("Could not parse YAML frontmatter (%s)", e)
        return {}


def copy_coded_papers():
    """Copy coded papers from the databook directory to the destination directory. And logs total number of copied and skipped papers."""
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        logger.info("Created destination directory %s", destination_dir)
    else:
        logger.info("Destination directory %s already exists", destination_dir)

    copied_count = 0
    skipped_count = 0

    try:
        for filename in os.listdir(databook_dir):
            if not filename.endswith(".md"):
                continue
            filepath = os.path.join(databook_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            frontmatter = parse_frontmatter(content)
            if frontmatter.get(STATUS_KEY) == STATUS_VALUE:
                destination_path = os.path.join(destination_dir, filename)
                shutil.copy(filepath, destination_path)
                copied_count += 1
            else:
                skipped_count += 1
            logger.info(
                "Copied %d papers and skipped %d papers so far.",
                copied_count,
                skipped_count,
            )
        logger.info("Finished copying coded papers.")
        logger.info("Total copied: %d", copied_count)
        logger.info("Total skipped: %d", skipped_count)
    except OSError as e:
        logger.error("An error occurred: %s", str(e))


if __name__ == "__main__":
    copy_coded_papers()
