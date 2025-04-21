from flask import Flask, render_template_string
import random

app = Flask(__name__)

@app.route("/")
def random_number():
    number = random.randint(1, 100)
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Random Number 🎲</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(135deg, #fceabb 0%, #f8b500 100%);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            .card {
                padding: 2rem;
                border-radius: 1.5rem;
                box-shadow: 0 0 30px rgba(0,0,0,0.2);
                background-color: #ffffffaa;
                text-align: center;
            }
            .number {
                font-size: 4rem;
                font-weight: bold;
                color: #ff6f00;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1 class="mb-3">🎲 Your Lucky Number</h1>
            <div class="number">{{ number }}</div>
            <p class="mt-3"><a href="/" class="btn btn-outline-dark">Try Again</a></p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, number=number)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
