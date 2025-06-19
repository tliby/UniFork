from dataclasses import dataclass
from transformers import PretrainedConfig


@dataclass
class AttentionBlockConfig:
    embed_dim: int = 2560
    n_head: int = 40
    mlp_bias: bool = True
    attn_bias: bool = True
    attn_pdrop: float = 0.0
    resid_pdrop: float = 0.1


@dataclass
class AttentionStackConfig:
    n_layer: int = 6
    block: AttentionBlockConfig = AttentionBlockConfig()


class RQTransformerConfig(PretrainedConfig):
    model_type = "rqtransformer_model"
    def __init__(
        self,
        block_size=None,
        input_embed_dim_1=None,
        input_embed_dim_2=None,
        embed_dim=None,
        embed_dim_out=None,
        vocab_size=None,
        head=None,
        architectures=None,
        **kwargs,
    ):
        super().__init__()

        self.block_size = block_size
        self.input_embed_dim_1 = input_embed_dim_1
        self.input_embed_dim_2 = input_embed_dim_2
        self.embed_dim = embed_dim
        self.embed_dim_out = embed_dim_out
        self.vocab_size = vocab_size
        self.head = head
        self.architectures = architectures  