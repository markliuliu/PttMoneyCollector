import logging

import torch
from transformers import pipeline

device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)
logger = logging.getLogger("QuestionAnswer")
logger.info(f"device={device}")


class QuestionAnswer:
    def __init__(self, model_name="ZYW/en-de-vi-zh-es-model"):
        self.question = "推文要推什麼文字?"
        self.pipe = pipeline("question-answering", model=model_name, device=device)

    def get_comment(self, context, question=None):
        if question is None:
            question = self.question
        return self.pipe(question=question, context=context)["answer"]
