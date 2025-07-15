# Bodywash Review Labeling

## Approach

This project aims to automatically assign hierarchical labels (parent and child categories) to product reviews for bodywash products. The workflow is as follows:

- **Data Preparation:** The raw Excel data is processed to extract reviews and their associated parent/child labels. The dataset is split into training and validation sets, ensuring no overlap.
- **Prompt Engineering:** A few-shot prompt template is constructed using LangChain, where each example consists of a review and its corresponding labels. The prompt instructs the model to output only the relevant labels in JSON format.
- **Example Selection:** Instead of using all examples, an example selector is used to dynamically select the most relevant examples for each new review, improving the quality and relevance of the prompt.
- **Model Inference:** A large language model (LLM) is used to generate label predictions for new reviews, guided by the selected examples and the prompt.
- **Evaluation:** The predicted labels are compared to the ground truth using Jaccard accuracy and ROUGE metrics.

## Example Selectors

- **Relevance:** Example selectors ensure that only the most relevant examples are included in the prompt, making the LLM's output more accurate and context-aware.
- **Efficiency:** By limiting the number of examples, prompts remain concise and within token limits.
- **Generalization:** Dynamic selection of examples helps the model adapt to a wider variety of inputs, improving robustness.


## Models Considered and Selection Rationale

- **HuggingFace Embeddings (all-MiniLM-L6-v2):** Chosen for its strong performance in semantic similarity tasks and ease of use without API restrictions.
- **LLM (Groq Llama-3.1-8b-instant):** Selected for its balance of speed and accuracy in text generation and classification tasks.

**Reason for Model Selection:**  
The HuggingFace embedding model provides efficient and accurate semantic similarity, which is crucial for selecting relevant examples. The Llama-3.1-8b-instant model is used for its ability to follow complex prompts and generate structured outputs, making it suitable for few-shot learning scenarios.

## Output Accuracy

- **Jaccard Accuracy:** The average Jaccard accuracy between predicted and true labels is reported (`📊 Average Jaccard Accuracy: 25.50%`).
- **ROUGE Scores:** ROUGE-1 and ROUGE-2 F1 scores are also computed to evaluate the overlap between predicted and true label sets.
`📊 ROUGE-1 F1: 40.67%
📊 ROUGE-2 F1: 30.29%`
