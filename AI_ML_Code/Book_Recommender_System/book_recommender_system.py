from flask import Flask,render_template,request
import pickle
import numpy as np

popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values.round(2))
                           )
#<h4 class="text-white">Rating - {{ rating[i]|round(2)}}</h4> incase of html changes

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input', '').strip().lower()
    pt.index = pt.index.astype(str).str.strip().str.lower()

    if user_input not in pt.index:
        from difflib import get_close_matches
        matches = get_close_matches(user_input, pt.index, n=5, cutoff=0.6)
        if matches:
            return f"Book '{user_input}' not found. Did you mean: {', '.join(matches)}?", 400
        else:
            return f"Book '{user_input}' not found in recommendation index.", 400

    index = pt.index.get_loc(user_input)
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for i in similar_items:
        book_title = pt.index[i[0]]
        temp_df = books[books['Book-Title'].str.lower().str.strip() == book_title]
        temp_df = temp_df.drop_duplicates(subset='Book-Title')

        item = {
            'title': temp_df['Book-Title'].values[0],
            'author': temp_df['Book-Author'].values[0],
            'image': temp_df['Image-URL-M'].values[0],
            'votes': int(temp_df['num_ratings'].values[0]),
            'rating': round(float(temp_df['avg_rating'].values[0]), 2)
        }

        data.append(item)

    return render_template('recommend.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)