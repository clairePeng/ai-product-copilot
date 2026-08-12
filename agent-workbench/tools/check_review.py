from pathlib import Path
import sys


REQUIRED_SECTIONS = [
    "# 1. 需求摘要",
    "# 2. P0",
    "# 3. P1",
    "# 4. P2",
    "# 5. 核心风险 Top 3",
    "# 6. 最应该问业务方的5个问题",
    "# 7. 评审结论",
]


def check_review(requirement_file, review_file):
    requirement = Path(requirement_file)
    review = Path(review_file)

    result = []

    if not requirement.exists():
        result.append("❌ 需求文件不存在")
        return result

    result.append("✅ 需求文件存在")

    if not review.exists():
        result.append("❌ 评审报告不存在")
        return result

    result.append("✅ 评审报告存在")

    content = review.read_text(encoding="utf-8")

    for section in REQUIRED_SECTIONS:
        if section in content:
            result.append(f"✅ {section}")
        else:
            result.append(f"❌ 缺少：{section}")

    word_count = len(content)

    result.append(f"📄 报告字符数：{word_count}")

    return result


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法：")
        print("python3 tools/check_review.py <需求文件> <评审报告>")
        sys.exit(1)

    result = check_review(sys.argv[1], sys.argv[2])

    print("\n".join(result))