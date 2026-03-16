from typing import Any, Dict

from jsonschema import validate

from src.utils.logger import get_logger


logger = get_logger(__name__)


def validate_schema(data: Dict[str, Any], schema: Dict[str, Any]) -> None:
    logger.info("Validating response schema")
    validate(instance=data, schema=schema)
    logger.info("Schema validation passed")