from flask import Flask, render_template

app = Flask(__name__)

# Dummy data (replace this with a database)
posts = [
   # {
       # 'author': 'John Doe',
       # 'image_url': 'https://via.placeholder.com/150',
        #'caption': 'Hello, this is a sample post!'
   # },
    # Add more posts here
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
