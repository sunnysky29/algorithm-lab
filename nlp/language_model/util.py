import torch
from torch.utils.data import Dataset, DataLoader
from vocab import Vocab
from utils import datapath
import jieba

# Constants
BOS_TOKEN = "<bos>"
EOS_TOKEN = "<eos>"
PAD_TOKEN = "<pad>"
BOW_TOKEN = "<bow>"
EOW_TOKEN = "<eow>"

WEIGHT_INIT_RANGE = 0.1

def load_reuters():
    from nltk.corpus import reuters
    text = reuters.sents()
    # lowercase (optional)
    text = [[word.lower() for word in sentence] for sentence in text]
    vocab = Vocab.build(text, reserved_tokens=[PAD_TOKEN, BOS_TOKEN, EOS_TOKEN])
    corpus = [vocab.convert_tokens_to_ids(sentence) for sentence in text]

    return corpus, vocab



def save_pretrained(vocab, embeds, save_path):
    """auto --client 127.0.0.1 --port 52556 --file /Users/dufy/code/algorithm-lab/nlp/language_model/fnn_lm.py
Connected to pydev debugger (buil
    Save pretrained token vectors in a unified format, where the first line
    specifies the `number_of_tokens` and `embedding_dim` followed with all
    token vectors, one token per line.
    """
    with open(save_path, "w") as writer:
        writer.write(f"{embeds.shape[0]} {embeds.shape[1]}\n")
        for idx, token in enumerate(vocab.idx_to_token):
            vec = " ".join(["{:.4f}".format(x) for x in embeds[idx]])
            writer.write(f"{token} {vec}\n")
    print(f"Pretrained embeddings saved to: {save_path}")

def load_pretrained(load_path):
    with open(load_path, "r") as fin:
        # Optional: depending on the specific format of pretrained vector file
        n, d = map(int, fin.readline().split())
        tokens = []
        embeds = []
        for line in fin:
            line = line.rstrip().split(' ')
            token, embed = line[0], list(map(float, line[1:]))
            tokens.append(token)
            embeds.append(embed)
        vocab = Vocab(tokens)
        embeds = torch.tensor(embeds, dtype=torch.float)
    return vocab, embeds

def get_loader(dataset, batch_size, shuffle=True):
    data_loader = DataLoader(
        dataset,
        batch_size=batch_size,
        collate_fn=dataset.collate_fn,
        shuffle=shuffle
    )
    return data_loader

def init_weights(model):
    for name, param in model.named_parameters():
        if "embedding" not in name:
            torch.nn.init.uniform_(
                param, a=-WEIGHT_INIT_RANGE, b=WEIGHT_INIT_RANGE
            )


def load_corpus():
    path = datapath('data/cnews.val.txt')
    f= open(path, 'r', encoding='utf-8')
    text = []
    for line in f:
        text.extend(line.split('。'))
    print(text[:10])
    print(f'text 长度：{len(text)}')
    # text = reuters.sents()
    # lowercase (optional)
    exclude_chars = {'：',
                     '”',
                     ' ',
                     '？',
                     '。',
                     '、',
                     '，',
                     '\t',
                     '“',
                     '-',
                     '\n',
                     '(',
                     ')'}
    text = [[word.lower() for word in jieba.cut(sentence) if word not in exclude_chars] for sentence in text]
    print(f'text ：{text}')
    vocab = Vocab.build(text, reserved_tokens=[PAD_TOKEN, BOS_TOKEN, EOS_TOKEN])
    print(f'vocab:{vocab}')
    # corpus = [vocab.convert_tokens_to_ids(sentence) for sentence in text]
    corpus = []
    for sentence in text:
        corpus.append(vocab.convert_tokens_to_ids(sentence))

    return corpus, vocab


if __name__ == "__main__":
    pass
    load_corpus()