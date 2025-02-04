import sys
from build_index import build_vector_store_for_pdf
from rag_pipeline import answer_query

def main():
    print("Welcome to the chat interface!")
    if len(sys.argv) < 2:
        print("Usage: python chat.py /path/to/your.pdf")
        sys.exit(1)

    pdf_path = sys.argv[1]

    print("Building the vector store...")
    build_vector_store_for_pdf(pdf_path)
    print("Vector store built. You can now ask questions.")

    while True:
        user_input = input("\n[User] > ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting...")
            break

        # Get the answer from the pipeline
        answer = answer_query(user_input, model="llama2", k=3)
        print(f"[Assistant] {answer}")

if __name__ == "__main__":
    main()
