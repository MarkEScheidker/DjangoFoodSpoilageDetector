from django.http import HttpResponse

def basic_view(request):
    # Get the 'freshness' value from the URL query parameters
    freshness = request.GET.get('freshness', None)

    # Default to fresh if no value is provided
    if freshness is not None:
        try:
            freshness = int(freshness)
        except ValueError:
            freshness = None

    # Set conditions for freshness, spoiling, and spoiled
    if freshness is not None and freshness < 50:
        message = "Spoiled"
        background_color = "red"
    elif freshness is not None and 50 <= freshness < 75:
        message = "Spoiling"
        background_color = "orange"
    else:
        message = "Fresh"
        background_color = "green"

    # Display the message and the freshness value
    return HttpResponse(f'''
    <html>
    <head>
        <style>
            body {{
                background-color: {background_color};
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: Arial, sans-serif;
                color: white;
                flex-direction: column;
            }}
            h1 {{
                font-size: 100px;
            }}
            p {{
                font-size: 40px;
            }}
        </style>
    </head>
    <body>
        <h1>{message}</h1>
        {f"<p>Freshness value: {freshness}</p>" if freshness is not None else ""}
    </body>
    </html>
    ''')
