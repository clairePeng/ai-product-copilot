from pathlib import Path


REQUIREMENT_DIR = Path("test-data")
REVIEW_DIR = Path("review-results")


def main():
    requirements = sorted(REQUIREMENT_DIR.glob("requirement*.md"))

    if not requirements:
        print("没有找到需求文件")
        return

    print("=== Requirement Review Batch Check ===")

    pending = []
    completed = []

    for requirement in requirements:
        review = REVIEW_DIR / f"{requirement.stem}-review.md"

        if review.exists():
            completed.append(requirement.name)
        else:
            pending.append(requirement.name)

    print(f"\n需求总数：{len(requirements)}")
    print(f"已完成：{len(completed)}")
    print(f"待评审：{len(pending)}")

    if completed:
        print("\n已完成：")
        for item in completed:
            print(f"  ✅ {item}")

    if pending:
        print("\n待评审：")
        for item in pending:
            print(f"  ⏳ {item}")

    print("\n=== 建议执行 ===")

    if pending:
        print("只需要让 Agent 处理以下文件：")
        for item in pending:
            print(f"  → {item}")
    else:
        print("所有需求均已有评审结果。")


if __name__ == "__main__":
    main()