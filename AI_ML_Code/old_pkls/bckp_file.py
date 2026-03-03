

@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    #index = np.where(pt.index == user_input)[0][0] # Original line that may cause error if book not foundsn
    """ if user_input not in pt.index:
        return f"Book '{user_input}' not found in recommendation index.", 400 """
    matches = np.where(pt.index == user_input)[0]
    if len(matches) == 0:
        # Handle “book not found”
        # For Flask:
        return f"Book '{user_input}' not found in recommendation index.", 400
    index = matches[0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    print(data)

    return render_template('recommend.html',data=data)