class Prompt:
    def __init__(self):
        pass
    
    def label_prompt(self):
        template = """
        You are a helpful assistant that labels text based on the user question and provided context.
        Your task is toassign parent and child labels to the user based on the context below

        # USER QUESTION:
        {review}

        # CONTEXT:
        {examples}

        # CRUCIAL NOTE:
        - The labels should contain both parent and child labels.\
        - The labels should be relevant to the user question and context provided.
        - The labels should be from the context strictly.
        - Do not make up labels that are not present in the context.
        - Parent labels should be broader categories, while child labels should be more specific subcategories.
        - Parent should be followedd by a child label that is a more specific subcategory of the parent.
        - There can be one parent and chiled label, or multiple parent-child pairs.
        - Both parent and child labels cannot be blank or null

        # OUTPUT FORMAT:
        Return only a valid JSON object with the following structure:
        {{
            "labels": [
                {{
                    "parent": "<parent category>",
                    "child": "<child category>"
                }},
            ]
        }}
        

        Do not return any explanation or text outside this JSON block.
        """
        return template