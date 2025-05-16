from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory “database”
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title', '').strip()
    if title:
        todos.append({'id': len(todos) + 1, 'title': title})
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
