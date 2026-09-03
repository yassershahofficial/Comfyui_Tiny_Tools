#pass through 2 int as inputs and output

class IntOrganizer:
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("INT", {"default": 0, "min": -9999, "max":9999}),
                "a": ("INT", {"default": 0, "min": -9999, "max":9999}),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("a", "b")
    FUNCTION = "organize"
    CATEGORY = "tiny_tools"

    def organize(self, a, b):
        return (a, b)
