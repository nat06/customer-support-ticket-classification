## work in progress ##

from src.data.load import load_customer_support_dataset
from src.data.preprocess import join_text_fields, drop_incomplete_rows
from src.data.split import stratified_split, build_balanced_eval_set
from src.prompt.prompt_builder import build_prompt
from src.models.batch_llm import run_llm_inference
from src.models.eval import print_basic_metrics, print_classification_report


def main():
    print("Loading data...")
    df = load_customer_support_dataset()
    df = join_text_fields(df)
    df = drop_incomplete_rows(df)

    print("Splitting...")
    train_df, test_df = stratified_split(df)
    balanced_df = build_balanced_eval_set(test_df)

    queue_list = sorted(df["queue"].dropna().unique().tolist())
    print("Queue classes:", queue_list)

    print("Running LLM inference...")
    balanced_df, pred_col, norm_col = run_llm_inference(
        balanced_df,
        queue_list,
        build_prompt,
        model="mistral-medium-2505",
        column_name_prefix="mistralmedium",
    )

    print("Evaluating results...")
    print_basic_metrics(balanced_df["queue"], balanced_df[norm_col])
    print_classification_report(
        balanced_df["queue"], balanced_df[norm_col], labels=queue_list
    )


if __name__ == "__main__":
    main()
