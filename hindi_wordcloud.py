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


text_input = """भगवद गीता, जिसे गीता भी कहा जाता है, एक हिंदू धर्मग्रंथ है जिसमें 700 श्लोक हैं।
गीता महाभारत युद्ध की शुरुआत के दौरान भगवान श्री कृष्ण और पांडव राजकुमार अर्जुन के बीच एक वार्तालाप है।
भगवान कृष्ण ने अपने चचेरे भाइयों के साथ पराजय के कारण अर्जुन द्वारा दिखाए गए नैतिक भ्रम का जवाब देने का बीड़ा उठाया और राजकुमार
और योद्धा के रूप में राजकुमार अर्जुन को उनके आदेशों और भूमिकाओं के बारे में बताया,
जिसमें सांख्य, कर्म योग, योग, मोक्ष और इनान योग की शिक्षाओं के बारे में विस्तार से बताया गया है, जो भगवद गीता में स्पष्ट रूप से मौजूद हैं।"""
tokens,comment_words = process_text(text_input)

wordcloud = WordCloud(font_path='/content/arialuni.ttf',width=800, height=800,
                      background_color='white',
                      stopwords=STOPWORDS,regexp=r"[\u0900-\u097F]+").generate(comment_words)


plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

word_counts = Counter(tokens)

sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

for word, count in sorted_word_counts.items():
    print(f"{word}: {count}")
