from main import ReturnClassifier
from test_cases import TEST_CASES, MIXED_LANG_CASES

def run_evals():
    print("\n" + "="*60)
    print("RUNNING EVALUATIONS ON RETURN CLASSIFIER")
    print("="*60 + "\n")
    
    classifier = ReturnClassifier()
    
    results = {
        "total": 0,
        "correct": 0,
        "by_difficulty": {"easy": {"correct": 0, "total": 0}, 
                          "adversarial": {"correct": 0, "total": 0}},
        "failures": []
    }
    
    all_cases = TEST_CASES + MIXED_LANG_CASES
    
    for i, case in enumerate(all_cases):
        results["total"] += 1
        difficulty = case["difficulty"]
        results["by_difficulty"][difficulty]["total"] += 1
        
        print(f"Test {i+1}: {case['text'][:50]}...")
        
        decision = classifier.classify(
            case["text"], 
            order_value=case.get("order_value"),
            days_since_delivery=case.get("days")
        )
        
        is_correct = (decision.decision == case["expected"])
        
        if is_correct:
            results["correct"] += 1
            results["by_difficulty"][difficulty]["correct"] += 1
            print(f"  ✓ Expected: {case['expected']}, Got: {decision.decision} (conf: {decision.confidence_score:.2f})")
        else:
            results["failures"].append({
                "input": case["text"],
                "expected": case["expected"],
                "got": decision.decision,
                "confidence": decision.confidence_score
            })
            print(f"  ✗ Expected: {case['expected']}, Got: {decision.decision} (conf: {decision.confidence_score:.2f})")
    
    # Print summary
    print("\n" + "="*60)
    print("EVALUATION SUMMARY")
    print("="*60)
    accuracy = results["correct"] / results["total"] * 100
    print(f"Total tests: {results['total']}")
    print(f"Correct: {results['correct']}")
    print(f"Accuracy: {accuracy:.1f}%")
    
    if results["failures"]:
        print(f"\nFAILURES ({len(results['failures'])}):")
        for f in results["failures"]:
            print(f"  - Expected {f['expected']}, Got {f['got']}: '{f['input'][:60]}'")
    
    return results

if __name__ == "__main__":
    run_evals()