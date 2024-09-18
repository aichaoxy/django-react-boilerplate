import os

from split_settings.tools import include, optional

ENV = os.getenv("ENV") or 'development'

settings_pipeline = [
    "components/common.py",
    optional(f"environments/{ENV}.py"),
    optional("environments/local.py"),
]

include(*settings_pipeline)