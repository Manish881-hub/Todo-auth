@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()

        if user:
            # In a real application, you would send an email here
            # For this demo, we'll just show a success message
            flash('If an account with that email exists, password reset instructions have been sent.', 'info')
            return redirect(url_for('login'))
        else:
            flash('If an account with that email exists, password reset instructions have been sent.', 'info')
            # We show the same message regardless to prevent email enumeration

    return render_template('forgot_password.html')

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form['email']
        new_password = request.form['new_password']

        user = User.query.filter_by(email=email).first()

        if user:
            user.set_password(new_password)
            db.session.commit()
            flash('Password reset successfully! Please log in with your new password.', 'success')
            return redirect(url_for('login'))
        else:
            flash('User not found.', 'danger')

    return render_template('reset_password.html')