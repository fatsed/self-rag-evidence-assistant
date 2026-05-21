from src.pipeline import run_pipeline


def main():
    print("=" * 60)
    print("Self-RAG Evidence Assistant")
    print("=" * 60)

    question = input("\nAsk a question: ")

    if not question.strip():
        print("Please enter a question.")
        return

    result = run_pipeline(question)

    print("\n" + "=" * 60)
    print("Question")
    print("=" * 60)
    print(result["question"])

    print("\n" + "=" * 60)
    print("Evidence")
    print("=" * 60)
    print(result["evidence"])

    print("\n" + "=" * 60)
    print("Answer")
    print("=" * 60)
    print(result["answer"])

    print("\n" + "=" * 60)
    print("Critique")
    print("=" * 60)
    print(result["critique"])

    print("\n" + "=" * 60)
    print("Done")
    print("=" * 60)


if __name__ == "__main__":
    main()
