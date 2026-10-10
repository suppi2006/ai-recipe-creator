from flask import Flask, request, render_template_string
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


@app.route("/", methods=["GET", "POST"])
def home():
    recipe = None
    error = None

    if request.method == "POST":
        ingredients = request.form.get("ingredients", "").strip()

        if not ingredients:
            error = "Please enter some ingredients."
        else:
            try:
                prompt = f"""
                Create a simple and delicious recipe using these ingredients:

                {ingredients}

                Give the response in this format:

                Recipe Name:
                Required Ingredients:
                Cooking Steps:
                """

                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt
                )

                recipe = response.text

            except Exception as e:
                error = str(e)

    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <title>AI Recipe Creator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            margin: 0;
            padding: 40px;
        }

        .container {
            max-width: 700px;
            margin: auto;
            background: white;
            padding: 35px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        h1 {
            text-align: center;
        }

        textarea {
            width: 100%;
            height: 150px;
            padding: 15px;
            font-size: 16px;
            box-sizing: border-box;
            border-radius: 8px;
            border: 1px solid #ccc;
        }

        button {
            width: 100%;
            padding: 15px;
            margin-top: 20px;
            background: #f58220;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 18px;
            cursor: pointer;
        }

        .recipe {
            margin-top: 25px;
            padding: 20px;
            background: #f9f9f9;
            border-radius: 10px;
            white-space: pre-wrap;
        }

        .error {
            margin-top: 20px;
            padding: 15px;
            background: #ffe5e5;
            color: #c00;
            border-radius: 8px;
        }
    </style>
</head>

<body>
<div class="container">

    <h1>🍳 AI Recipe Creator</h1>

    <p style="text-align:center;">
        Enter the ingredients available at home and let AI create a recipe for you.
    </p>

    <form method="POST">

        <h2>Enter Available Ingredients:</h2>

        <textarea
            name="ingredients"
            placeholder="Example: egg, tomato, rice, onion"
            required>{{ request.form.get("ingredients", "") }}</textarea>

        <button type="submit">🍽️ Generate Recipe</button>

    </form>

    {% if error %}
        <div class="error">
            <strong>Error:</strong> {{ error }}
        </div>
    {% endif %}

    {% if recipe %}
        <div class="recipe">
            <h2>🍴 Your AI Recipe</h2>
            {{ recipe }}
        </div>
    {% endif %}

</div>
</body>
</html>
""", recipe=recipe, error=error)


if __name__ == "__main__":
    app.run(debug=True)