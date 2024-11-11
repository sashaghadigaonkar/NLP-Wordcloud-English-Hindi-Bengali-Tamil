from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from collections import Counter
import string

def process_text(text):
    comment_words = ''
    stopwords = set(STOPWORDS)


    translator = str.maketrans('  ','  ', string.punctuation)
    text = text.translate(translator)
    tokens = text.split()

    tokens = [token.lower() for token in tokens if token.lower() not in stopwords]

    comment_words += " ".join(tokens) + " "

    return tokens, comment_words


text_input = """
ভগবদ গীতা, গীতা নামেও পরিচিত, একটি হিন্দু ধর্মগ্রন্থ যা 700টি শ্লোক নিয়ে গঠিত।
গীতা হল মহাভারত যুদ্ধের শুরুতে ভগবান শ্রী কৃষ্ণ এবং পান্ডব রাজপুত্র অর্জুনের মধ্যে একটি কথোপকথন।"""
tokens,comment_words = process_text(text_input)

wordcloud = WordCloud(font_path='/content/Siyamrupali.ttf',width=800, height=800,
                      background_color='white',
                      stopwords=STOPWORDS,regexp=r"[\u0900-\u097F\u0980-\u09FF]+").generate(comment_words)


plt.figure(figsize=(5,5), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

word_counts = Counter(tokens)

sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

for word, count in sorted_word_counts.items():
    print(f"{word}: {count}")
