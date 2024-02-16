from flask import Flask
from DBstorage import storage
app = Flask(__name__)
@app.route("/create", METHOD=["POST"])
def create():
    storage.new(form.data.name)
@app.route("/update",METHOD=["PUT"])
def update():
    #update task
@app.route("/delete",METHOD=["DELETE"]):
def delete():
    #delete task
@app.route("/all",METHOD=["GET"]):
def all():
    "return all tast"
if __name__ == "__main__":
  app.run()
