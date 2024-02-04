from utils import scores_file_name
from os import path
from pathlib import Path


def score_server():
    if not path.exists(scores_file_name):
        html_content = f"""
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>ERROR:</h1>
                    <div id="score" style="color:red">ERROR</div>
                </body>
            </html>
            """
    else:
        file = open(scores_file_name, 'r')
        score = file.read()
        file.close()
        html_content = f"""
                <html>
                    <head>
                        <title>Scores Game</title>
                    </head>
                    <body>
                        <h1>The score is:</h1>
                        <div id="score">{score}</div>
                    </body>
                </html>
                """
    return html_content


html = score_server()
print(html)
