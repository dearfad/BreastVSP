# Custom LLM for LangChain
# ChatGLM3

from typing import List, Optional, Any
from transformers import AutoTokenizer, AutoModel, AutoConfig
from langchain_core.language_models.llms import LLM
from langchain_core.callbacks.manager import CallbackManagerForLLMRun


class ChatGLM3(LLM):
    tokenizer: object = None
    model: object = None
    history: List = []

    @property
    def _llm_type(self) -> str:
        return "ChatGLM3"

    def load_model(self, local_path=None):
        model_config = AutoConfig.from_pretrained(local_path, trust_remote_code=True)
        self.tokenizer = AutoTokenizer.from_pretrained(
            local_path, trust_remote_code=True
        )
        self.model = (
            AutoModel.from_pretrained(
                local_path, config=model_config, trust_remote_code=True
            )
            .quantize(4)
            .cuda()
            .eval()
        )

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any
    ) -> str:
        response, self.history = self.model.chat(
            self.tokenizer, prompt, history=self.history
        )
        return response
