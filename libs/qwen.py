# Custom LLM for LangChain
# Qwen

from typing import List, Optional, Any
from modelscope import AutoTokenizer, AutoModelForCausalLM, AutoConfig
from langchain_core.language_models.llms import LLM
from langchain_core.callbacks.manager import CallbackManagerForLLMRun


class Qwen(LLM):
    tokenizer: object = None
    model: object = None
    history: List = []

    @property
    def _llm_type(self) -> str:
        return "Qwen"

    def load_model(self, local_path=None):
        # model_config = AutoConfig.from_pretrained(local_path, trust_remote_code=True)
        self.tokenizer = AutoTokenizer.from_pretrained(
            local_path, trust_remote_code=True
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            local_path, device_map="auto", trust_remote_code=True
        ).eval()

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any
    ) -> str:
        response, self.history = self.model.chat(
            self.tokenizer, prompt, history=self.history, max_length=8192
        )
        return response
