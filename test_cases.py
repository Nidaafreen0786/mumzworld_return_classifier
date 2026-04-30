# 12 test cases: 8 easy, 4 adversarial (to test uncertainty)

TEST_CASES = [
    # Easy cases - should have high confidence
    {
        "text": "The product arrived damaged. Box was crushed and bottle leaked.",
        "expected": "refund",
        "order_value": 150,
        "days": 2,
        "difficulty": "easy"
    },
    {
        "text": "Wrong item sent. I ordered a stroller but received a car seat.",
        "expected": "refund",
        "order_value": 800,
        "days": 1,
        "difficulty": "easy"
    },
    {
        "text": "Size doesn't fit. Need a larger size for my 2-year-old.",
        "expected": "exchange",
        "order_value": 89,
        "days": 3,
        "difficulty": "easy"
    },
    {
        "text": "المنتج ممتاز لكني غيرت رأيي",  # "Product is great but I changed my mind"
        "expected": "store_credit",
        "order_value": 45,
        "days": 10,
        "difficulty": "easy"
    },
    {
        "text": "I want my money back NOW. This is the worst quality ever.",
        "expected": "refund",  # Aggressive but still refund-worthy
        "order_value": 200,
        "days": 5,
        "difficulty": "easy"
    },
    {
        "text": "Missing parts. Assembly manual says screws should be included but they're not.",
        "expected": "exchange",
        "order_value": 350,
        "days": 7,
        "difficulty": "easy"
    },
    {
        "text": "My baby didn't like it. Nothing wrong with product just not for us.",
        "expected": "store_credit",
        "order_value": 65,
        "days": 12,
        "difficulty": "easy"
    },
    {
        "text": "Product defective. Doesn't turn on even with new batteries.",
        "expected": "refund",
        "order_value": 120,
        "days": 4,
        "difficulty": "easy"
    },
    
    # Adversarial cases - should trigger low confidence or escalate
    {
        "text": "I will never shop here again. You're thieves.",
        "expected": "escalate",  # Abusive language -> escalate
        "order_value": 30,
        "days": 30,  # Past return window
        "difficulty": "adversarial"
    },
    {
        "text": "المنتج جيد لكني أريد استرداد المبلغ",  # "Product is good but I want refund"
        "expected": "store_credit",  # Changed mind, not damaged
        "order_value": 10,  # Very low value
        "days": 20,  # Past window
        "difficulty": "adversarial"
    },
    {
        "text": "I don't know. Just feels off. Can't explain.",
        "expected": "escalate",  # Too ambiguous
        "order_value": 500,
        "days": 2,
        "difficulty": "adversarial"
    },
    {
        "text": "The color is slightly different than the picture but it's fine I guess?",
        "expected": "store_credit",  # Minor issue, not clearly defective
        "order_value": 75,
        "days": 14,
        "difficulty": "adversarial"
    }
]

# Bonus: cases that mix languages
MIXED_LANG_CASES = [
    {
        "text": "المنتج arrived broken and I want my فلوس back",
        "expected": "refund",
        "order_value": 100,
        "days": 3,
        "difficulty": "easy"
    },
    {
        "text": "Size small but I ordered large. بدي استبدال",
        "expected": "exchange",
        "order_value": 99,
        "days": 2,
        "difficulty": "easy"
    }
]