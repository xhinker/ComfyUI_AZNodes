class HelloNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_text": ("STRING", {"multiline": False, "default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_text",)
    FUNCTION = "hello"
    CATEGORY = "AZNodes"

    def hello(self, input_text):
        return ("Hello" + input_text,)

# ComfyUI node registry
NODE_CLASS_MAPPINGS = {
    "AZ_HelloNode": HelloNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AZ_HelloNode": "AZ Hello Node",
}
