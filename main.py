import os
from openai import OpenAI
import base64





def process_image(image) -> str:
    client = OpenAI(
        api_key=os.getenv("OPEN_API_KEY"),
        organization= os.getenv("ORGANIZATION_ID"),
        project= os.getenv("PROJECT_ID")

    )
    response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
        {
          "role": "user",
          "content": [
            {"type": "text", "text": "Find all the medical code in this medical report?"},
            {
              "type": "image_url",
              "image_url": {
                "url": f"data:image/jpeg;base64,{image}",
              },
            },
          ],
        }
      ],
      max_tokens=100,
    )

    return response.choices[0].dict()


if(__name__ == "__main__"):
    pass