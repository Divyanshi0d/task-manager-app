from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default="pending")

with app.app_context():
    db.create_all()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "title": t.title, "status": t.status} for t in tasks])

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    if not data.get("title"):
        return {"error": "Title required"}, 400

    new_task = Task(title=data['title'])
    db.session.add(new_task)
    db.session.commit()
    return {"message": "Task added"}

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)
    if not task:
        return {"error": "Not found"}, 404

    task.status = "done"
    db.session.commit()
    return {"message": "Updated"}

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if not task:
        return {"error": "Not found"}, 404

    db.session.delete(task)
    db.session.commit()
    return {"message": "Deleted"}

if __name__ == "__main__":
    app.run(debug=True)
