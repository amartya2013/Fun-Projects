

def get_response(text, image):
    from openai import OpenAI
    import base64
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    client = OpenAI(
        # This is the default and can be omitted
        api_key = ""
    )
    base64_image = encode_image(image)
    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": text},
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",
                    },
                ],
            },
        ]
    )

    return response.output_text




