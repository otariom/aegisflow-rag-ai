SYSTEM_PROMPT = """
You are AegisFlow, an AI regulatory analysis assistant.

Your job is to analyze documents and answer questions using ONLY the
information provided in the context.

Rules you must follow:

1. Do not guess or hallucinate.
2. If the answer is not present in the context, say:
   "I don't have knowledge about this in the provided documents."
3. Be concise and precise.
4. Explain complex regulations in clear language.
5. If possible, reference the relevant parts of the context.
"""


def build_prompt(question: str, context_chunks: list) -> str:
    """
    Build a grounded prompt using retrieved document context.
    """

    context = "\n\n".join(context_chunks)

    prompt = f"""
{SYSTEM_PROMPT}

Context:
{context}

User Question:
{question}

Provide a clear answer based only on the context.
"""

    return prompt


def followup_questions():
    """
    Default follow-up questions suggested to the user.
    """

    return [
        "Can you summarize the key compliance points?",
        "Which section of the regulation is most relevant?",
        "Are there potential compliance risks?",
    ]