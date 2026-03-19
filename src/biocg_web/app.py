from __future__ import annotations
from typing import Literal

from pathlib import Path
import logging
import os

import fastapi
import nicegui
from dotenv import find_dotenv, dotenv_values

from . import pages

logger = logging.getLogger()


def create_app():
    title = "BioCG"

    VERBOSE = os.environ.get("BIOCG_WEB_VERBOSE")
    if VERBOSE:
        logging.getLogger().addHandler(logging.StreamHandler())
        logger.setLevel(logging.DEBUG)
        dotenv_path = find_dotenv()
        logger.debug(f"Env loaded from file: {dotenv_path}:")
        env = dotenv_values()
        for k, v in env.items():
            logger.debug(f"{k:>30}={v}")

    storage_secret = os.environ.get("BIOCG_WEB_STORAGE_SECRET")
    if storage_secret is None:
        logger.warning(
            "Using unsecure public secret for storage. Don\t use in production!"
        )
        storage_secret = "dev-unsecure-mode"

    app = fastapi.FastAPI(title=title)

    assets_path = Path(__file__) / ".." / "assets"
    assets_path = assets_path.resolve()
    nicegui.app.add_media_files("/assets", assets_path)
    nicegui.app.add_static_file(
        url_path="/favicon.ico", local_file=assets_path / "favicon" / "favicon.ico"
    )
    nicegui.ui.run_with(
        app,
        title=title,
        storage_secret=storage_secret,
        favicon="/favicon.ico",
    )
    return app


app = create_app()
