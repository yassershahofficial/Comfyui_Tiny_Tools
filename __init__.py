from .nodes.hello import IntAdd
from .nodes.organizer import IntOrganizer

NODE_CLASS_MAPPINGS = {
        "IntAdd": IntAdd,
        "IntOrganizer": IntOrganizer,
}

NODE_DISPLAY_NAME_MAPPINGS = {
        "IntAdd": "Int Add",
        "IntOrganizer": "Int Organizer",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
