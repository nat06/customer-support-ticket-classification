def format_fewshot_examples(df, n=3):
    examples = []
    seen_queues = set()

    for _, row in df.iterrows():
        queue = row["queue"]
        if queue in seen_queues:
            continue
        seen_queues.add(queue)
        example = f"""<s>[INST] {row['input_text']} [/INST] {queue}</s>"""
        examples.append(example)
        if len(examples) == n:
            break
    return examples
