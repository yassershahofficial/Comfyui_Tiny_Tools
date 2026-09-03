from .nodes.hello import IntAdd

NODE_CLASS_MAPPINGS = {
        "IntAdd": IntAdd,
}

NODE_DISPLAY_NAME_MAPPINGS = {
        "IntAdd": "Int Add",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
