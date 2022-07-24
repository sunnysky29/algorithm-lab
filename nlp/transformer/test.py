# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2022/6/26 21:10
File : test.py

参考哔站：[吃透Transformer！](https://www.bilibili.com/video/BV1Lt4y1h7hP?p=8&vd_source=abeb4ad4122e4eff23d97059cf088ab4)
==============================================================================
"""


class Encoder(nn.Module):
    "Core encoder is a stack of N layers"
    def __init__(self, layer, N):
        super(Encoder, self).__init__()
        self.layers = clones(layer, N)
        self.norm = LayerNorm(layer.size)
        
    def forward(self, x, mask):
        "Pass the input (and mask) through each layer in turn."
        for layer in self.layers:
            x = layer(x, mask)
        return self.norm(x)


# ## Encoder
# 结构图如下：
# <img src="https://tva1.sinaimg.cn/large/e6c9d24egy1h4i5wv3zfwj20qi0xkdik.jpg" alt="image-20220724175041623" style="zoom:67%;height:800px" />

class Embeddings(nn.Module):
    """
    实现文本嵌入层
    """
    def __init__(self, d_model, vocab):
        """

        :param d_model: 词嵌入维度
        :param vocab:   词表大小
        """
        pass
        super(Embeddings, self).__init__()
        # 定义Embedding层
        self.lut = nn.Embedding(vocab, d_model)
        self.d_model = d_model

    def forward(self, x):
        return self.lut(x) * math.sqrt(self.d_model)


class PositionalEnocoding(nn.Module):
    def __init__(self, d_model, dropout, max_len=5000):
        """
        注意，位置编码是固定的
        :param d_model:
        :param dropout:
        :param max_len:
        """
        super(PositionalEnocoding, self).__init__()

        # 实例化dropout层
        self.dropout = nn.Dropout(p=dropout)

        # 初始化一个位置编码矩阵, (max_len, d_model)
        pe =torch.zeros(max_len, d_model)

        # 初始化一个绝对位置矩阵, （max_len,1）
        position = torch.arange(0, max_len).unsqueeze(1)

        # 定义变化矩阵，跳跃式的初始化
        div_term = torch.exp(torch.arange(0, d_model, 2) \
                             * -(math.log(10000.0) / d_model)
                             )
        print(f'div_term 采样: {div_term[:10]}')
        print(f'div_term shape: {div_term.shape}')

        # 奇数、偶数分别处理
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)

        # 将二维张量扩充成三维
        pe= pe.unsqueeze(0)
        print(f'pe 扩充后：{pe.shape}')

        # 将位置编码矩阵注册成模型的 buffer, 这个 buffer 不是模型中的参数，不跟随优化器同步更新
        # 注册成 buffer 后，我们就可以在模型保存后，重新加载的时候，将这个位置编码器和模型参数加载进来
        self.register_buffer('pe', pe)

    def forward(self,x):
        """

        :param x: 词嵌入表示
        :return:
        """
        x =x + Variable(self.pe[:, :x.size(1)], requires_grad=False)
        return self.dropout(x)


if __name__ == "__main__":
    pass
    d_model = 512
    vocab= 1000
    dropout = 0.1
    max_len =60

    input_index = Variable(torch.LongTensor([[100, 24, 5, 6],
                                             [12, 4, 5, 6]]))
    emb = Embeddings(d_model, vocab)
    emb_res = emb(input_index)
    print(f'词嵌入向量: {emb_res}')
    print(f'shape:{emb_res.shape}')
    print(f'添加位置编码：============================')
    x = emb_res
    pe = PositionalEnocoding(d_model, dropout, max_len)
    pe_result = pe(x)
    print(pe_result)
    print(pe_result.shape)


