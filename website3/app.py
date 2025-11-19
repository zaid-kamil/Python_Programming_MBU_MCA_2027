from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def show_user(username):
    return f"👤 User Profile: {username}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"📝 Post ID: {post_id}"

@app.route('/motivation/<int:desperation_score>')
def motivation(desperation_score):
    if desperation_score < 3:
        return "💪 You're doing great! Keep going!"
    elif desperation_score < 7:
        return "😅 Hang in there! Coffee break recommended."
    else:
        return "🆘 Emergency! Take a break. You've got this! 🫂"

if __name__ == '__main__':
    app.run(debug=True)