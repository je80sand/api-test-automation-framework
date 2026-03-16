LOGIN_SUCCESS_SCHEMA = {
    "type": "object",
    "properties": {
        "token": {"type": "string"}
    },
    "required": ["token"],
    "additionalProperties": True
}