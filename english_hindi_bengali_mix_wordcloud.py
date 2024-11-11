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


text_input = """The Bhagavad Gita, also referred to as Gita is a Hindu scripture comprising of 700 verses.
 Gita is a conversation between Lord Shri Krishna and Pandava prince Arjuna during
 the onset of Mahabharata war,भगवद गीता, जिसे गीता भी कहा जाता है, एक हिंदू धर्मग्रंथ है जिसमें 700 श्लोक हैं।
गीता महाभारत युद्ध की शुरुआत के दौरान भगवान श्री कृष्ण और पांडव राजकुमार अर्जुन के बीच एक वार्तालाप है।
ভগবদ গীতা, গীতা নামেও পরিচিত, একটি হিন্দু ধর্মগ্রন্থ যা 700টি শ্লোক নিয়ে গঠিত।
গীতা হল মহাভারত যুদ্ধের শুরুতে ভগবান শ্রী কৃষ্ণ এবং পান্ডব রাজপুত্র অর্জুনের মধ্যে একটি কথোপকথন।"
. """
tokens,comment_words = process_text(text_input)

wordcloud = WordCloud(font_path='/content/arialuni.ttf',width=800, height=800,
                      background_color='white',
                      stopwords=STOPWORDS,regexp = r"[a-zA-Z0-9\u0900-\u097F\u0900-\u097F\u0980-\u09FF]+",min_font_size=10).generate(comment_words)


plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

word_counts = Counter(tokens)

sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

for word, count in sorted_word_counts.items():
    print(f"{word}: {count}")