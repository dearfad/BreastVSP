# Custom LLM for LangChain
# Qwen-1_8B-Chat

from typing import List, Optional, Any
from transformers import AutoTokenizer, AutoModelForCausalLM
from langchain_core.language_models.llms import LLM
from langchain_core.callbacks.manager import CallbackManagerForLLMRun


class Qwen(LLM):
    tokenizer: object = None
    model: object = None
    history: List = []

    @property
    def _llm_type(self) -> str:
        return "Qwen-1_8B-Chat"

    def load_model(self, local_path=None):
        self.tokenizer = AutoTokenizer.from_pretrained(
            local_path, trust_remote_code=True
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            local_path,
            device_map="auto",
            trust_remote_code=True,
            use_flash_attn=False,
        ).eval()

    def _call(
        self,
        query: str,
        system: str = "You are a helpful assistant.",
        stop_words_ids: Optional[List[List[int]]] = None,
        **kwargs,
    ) -> str:
        response, self.history = self.model.chat(
            self.tokenizer, query, history=self.history
        )
        return response
