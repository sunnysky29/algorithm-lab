

##  1.前馈神经网络lm

<img src="https://tva1.sinaimg.cn/large/e6c9d24egy1h28w7kmv3ij20ti0hu75e.jpg" alt="image-20220515104412577" style="zoom:50%;" />

根据马尔科夫假设对语言模型进行简化，即当前词只与前 n-1 个词相关
$$
P(w_t|w_{1:t-1}) = P(w_t|w_{t-n+1:t-1})
$$
模型结构代码：

~~~python
class FeedForwardNNLM(nn.Module):
    def __init__(self, vocab_size, embedding_dim, context_size, hidden_dim):
        super(FeedForwardNNLM, self).__init__()
        # 词嵌入层
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        # 线性变换：词嵌入层->隐含层
        self.linear1 = nn.Linear(context_size * embedding_dim, hidden_dim)
        # 线性变换：隐含层->输出层
        self.linear2 = nn.Linear(hidden_dim, vocab_size)
        # 使用ReLU激活函数
        self.activate = F.relu
        init_weights(self)

    def forward(self, inputs):
        embeds = self.embeddings(inputs).view((inputs.shape[0], -1))
        hidden = self.activate(self.linear1(embeds))
        output = self.linear2(hidden)
        # 根据输出层（logits）计算概率分布并取对数，以便于计算对数似然
        # 这里采用PyTorch库的log_softmax实现
        log_probs = F.log_softmax(output, dim=1)
        return log_probs
~~~



参考：
- https://github.com/HIT-SCIR/plm-nlp-code