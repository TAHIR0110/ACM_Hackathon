# ACM_Hackathon

## How to run the project 

1. `pip install flask`
2. go to `main.py`
3. run it

## Where to make new html pages

1. Go to `templates->(create new html file)`
2. now go to main.py
3. ```
@app.route("/html-file-name")
def anynameyouwant():
    return render_template("html-file-name.html")
```
4. write this before `app.run(debug=True)`