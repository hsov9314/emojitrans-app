import emoji
from gensim.models import Word2Vec
from janome.tokenizer import Tokenizer
#import MeCab


pos_list = """
    名詞 動詞 形容詞 副詞 助動詞
    """.split()

"""
def get_word_list_mecab(text: str)-> list:
    m = MeCab.Tagger('')
    m.parse('')
    nodes = m.parse(text)

    node_list = [
            [
                node.split("\t")[1].split(",")[6], node.split("\t")[1].split(",")[0]
            ] 
        for node in nodes.split("\n") 
            if len(node.split("\t")) >= 2
        ]
    
    node_list = [node[0] for node in node_list if node[1] in pos_list]
    
    return node_list
"""

def get_word_list_janome(text: str)-> list:
    t = Tokenizer(udic_enc="utf8")
    nodes = t.tokenize(text)

    node_list = [
        [
            node.base_form
        ] 
        for node in nodes
        if node.part_of_speech.split(",")[0] in pos_list
    ]

    return node_list

def wordlist2emoji(word_list: list, topn:int = 1000)-> str:
    model = Word2Vec.load("./static/word2vec_tweet.model")
    translated_text = ""

    for word in word_list:
        try:
            similar_word_list = [word for word in model.wv.most_similar(word, topn=topn)]
        except:
            continue
        
        for word in similar_word_list:
            if word[0] in emoji.UNICODE_EMOJI:
                translated_text += word[0]
                break
            
            else:
                continue
        
        
    
    return translated_text

"""
if __name__ == "__main__":
    text = "自分でサーバーくらい建てられるように"

    #print(get_word_list(text))
    print(get_word_list_janome(text))
"""