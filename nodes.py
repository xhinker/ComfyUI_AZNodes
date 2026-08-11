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


class AZ_SplitAVLatent:
    """
    Split a H3 AV NestedTensor latent back into video and audio latents.
    Input latent is expected to be a NestedTensor with [video_tensor, audio_tensor].
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "av_latent": ("LATENT",),
            }
        }

    RETURN_TYPES = ("LATENT", "LATENT")
    RETURN_NAMES = ("video_latent", "audio_latent")
    FUNCTION = "split"
    CATEGORY = "AZNodes/H3"

    def split(self, av_latent):
        samples = av_latent.get("samples")
        # Handle NestedTensor
        try:
            from comfy import nested_tensor
            if isinstance(samples, nested_tensor.NestedTensor):
                tensors = list(samples)
                if len(tensors) < 2:
                    raise ValueError("NestedTensor does not contain both video and audio tensors")
                video_tensor = tensors[0]
                audio_tensor = tensors[1]
            else:
                # Fallback: assume it's a single tensor, return as is
                video_tensor = samples
                audio_tensor = samples
        except Exception:
            # If nested_tensor import fails or not a NestedTensor, just pass through
            video_tensor = samples
            audio_tensor = samples

        return ({"samples": video_tensor}, {"samples": audio_tensor})


# ComfyUI node registry
NODE_CLASS_MAPPINGS = {
    "AZ_HelloNode": HelloNode,
    "AZ_SplitAVLatent": AZ_SplitAVLatent,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AZ_HelloNode": "AZ Hello Node",
    "AZ_SplitAVLatent": "AZ Split AV Latent",
}
