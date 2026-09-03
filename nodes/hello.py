
class IntAdd:
    """Add two integers together"""

    @classmethod
    def INPUT_TYPES(cls):
        return {
                "required": {
                    "a": ("INT", {"default": 1, "min": -9999, "max":9999}), 
                    "b": ("INT", {"default": 1, "min": -9999, "max":9999}),
                }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("sum",)
    FUNCTION = "sum"
    CATEGORY = "tiny_tools"

    def sum(self, a, b):
        return (a + b,)



