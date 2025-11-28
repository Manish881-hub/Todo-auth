from models import Todo

# Add these routes to app.py after the existing routes

@app.route('/dashboard')
@login_required
def dashboard():
    user_todos = Todo.query.filter_by(user_id=session['user_id']).order_by(Todo.created_at.desc()).all()
    return render_template('dashboard.html', todos=user_todos)

@app.route('/add_todo', methods=['POST'])
@login_required
def add_todo():
    title = request.form['title']
    description = request.form.get('description', '')

    if title:
        new_todo = Todo(
            title=title,
            description=description,
            user_id=session['user_id']
        )
        db.session.add(new_todo)
        db.session.commit()
        flash('Todo added successfully!', 'success')

    return redirect(url_for('dashboard'))

@app.route('/delete_todo/<int:todo_id>')
@login_required
def delete_todo(todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=session['user_id']).first()

    if todo:
        db.session.delete(todo)
        db.session.commit()
        flash('Todo deleted successfully!', 'success')
    else:
        flash('Todo not found or you do not have permission to delete it.', 'danger')

    return redirect(url_for('dashboard'))

@app.route('/toggle_todo/<int:todo_id>')
@login_required
def toggle_todo(todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=session['user_id']).first()

    if todo:
        todo.completed = not todo.completed
        db.session.commit()
        status = 'completed' if todo.completed else 'marked as incomplete'
        flash(f'Todo {status}!', 'success')
    else:
        flash('Todo not found.', 'danger')

    return redirect(url_for('dashboard'))