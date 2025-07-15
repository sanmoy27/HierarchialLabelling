from rouge_score import rouge_scorer

class AccuracyMetric:
    def __init__(self):
        pass

    def parse_label_string(self, label_str):
        labels = label_str.strip().split(';')
        label_set = set()
        for label in labels:
            parts = label.strip().split('>')
            if len(parts) == 2:
                parent = parts[0].strip().lower()
                child = parts[1].strip().lower()
                label_set.add((parent, child))
        return label_set
    
    def jaccard_similarity(self, set1, set2):
        if not set1 and not set2:
            return 1.0
        return len(set1 & set2) / len(set1 | set2)
    
    def compute_classification_accuracy(self, predicted, ground_truth):
        total = len(ground_truth)
        assert len(predicted) == total, "Mismatch in sample count"
        
        similarities = []
        
        for pred_item, gt_item in zip(predicted, ground_truth):
            # Normalize reviews to match
            review_pred = pred_item['review'].strip().lower()
            review_gt = gt_item['review'].strip().lower()
            
            if review_pred != review_gt:
                print(f"[⚠️ Warning] Review text mismatch:\n{review_pred}\n{review_gt}\n")

            pred_labels = self.parse_label_string(pred_item['labels'])
            true_labels = self.parse_label_string(gt_item['labels'])
            
            sim = self.jaccard_similarity(pred_labels, true_labels)
            similarities.append(sim)
        
        avg_jaccard = sum(similarities) / total
        return avg_jaccard, similarities
    


    def format_labels_for_rouge(self, label_str):
        """
        Converts 'Parent > Child; Parent > Child' into a string like:
        'parent child ; parent child ...'
        """
        pairs = label_str.strip().split(';')
        flattened = []
        for pair in pairs:
            if '>' in pair:
                parent, child = pair.split('>', 1)
                flattened.append(f"{parent.strip().lower()} {child.strip().lower()}")
        return ' ; '.join(flattened)

    # Compute ROUGE scores
    def compute_rouge_n(self, llm_preds, ground_truths):
        scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2'], use_stemmer=True)
        rouge1_scores = []
        rouge2_scores = []

        for pred, gt in zip(llm_preds, ground_truths):
            pred_text = self.format_labels_for_rouge(pred['labels'])
            gt_text = self.format_labels_for_rouge(gt['labels'])

            scores = scorer.score(gt_text, pred_text)
            rouge1_scores.append(scores['rouge1'].fmeasure)
            rouge2_scores.append(scores['rouge2'].fmeasure)

        avg_rouge1 = sum(rouge1_scores) / len(rouge1_scores)
        avg_rouge2 = sum(rouge2_scores) / len(rouge2_scores)
        return avg_rouge1, avg_rouge2



