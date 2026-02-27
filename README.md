# Testing Strategy for Quick-Calc

## What I Tested

### Unit Tests (12 tests)
I wrote unit tests to check each part of the calculator works alone:
- Addition, subtraction, multiplication, division
- Division by zero error
- Negative numbers
- Decimal numbers
- Big numbers
- Clear button
- Chained operations (like 5+3+2)

### Integration Tests (4 tests)
I tested that the GUI and calculator work together:
- Clicking 5 + 3 = shows 8
- Clear button resets everything
- Multiplication works (6 * 7 = 42)
- Division by zero shows "Error"

### What I Did NOT Test
- **GUI looks**: I didn't test if buttons are the right color or size
- **Speed**: I didn't test how fast it runs
- **Different computers**: I only tested on my computer

**Why?** Because the assignment asked for functional testing, not making it pretty or fast.

---

## Lecture Concepts

### 1. Testing Pyramid
I followed the pyramid idea:
- **Bottom (many tests)**: 12 unit tests - fast and simple
- **Top (few tests)**: 4 integration tests - slower but test everything together

This is good because unit tests find bugs quickly, and integration tests make sure the whole app works.

### 2. Black-box vs White-box Testing

**Unit Tests = White-box**
I looked inside the code. I checked things like `calc.current` and `calc.previous` to make sure the calculator remembers numbers correctly.

**Integration Tests = Black-box**
I pretended to be a user. I only clicked buttons and checked the screen, without looking at the code inside.

### 3. Functional vs Non-Functional Testing

**Functional (what I did)**:
- Does 5+3=8? ✓
- Does division by zero show error? ✓
- Does clear button work? ✓

**Non-Functional (what I skipped)**:
- Is it fast? (not required)
- Is it pretty? (not required)
- Works on all computers? (not required)

### 4. Regression Testing
If I change the code later (like making it faster), I can run all tests again to make sure I didn't break anything. If tests fail, I know I made a mistake.

---

## Test Results

All 16 tests passed:

| Test | Type | Result |
|------|------|--------|
| Addition | Unit | ✅ Pass |
| Subtraction | Unit | ✅ Pass |
| Multiplication | Unit | ✅ Pass |
| Division | Unit | ✅ Pass |
| Division by zero | Unit | ✅ Pass |
| Negative numbers | Unit | ✅ Pass |
| Decimal numbers | Unit | ✅ Pass |
| Big numbers | Unit | ✅ Pass |
| Clear button | Unit | ✅ Pass |
| Chained operations | Unit | ✅ Pass |
| Floating point fix | Unit | ✅ Pass |
| Display formatting | Unit | ✅ Pass |
| 5+3=8 workflow | Integration | ✅ Pass |
| Clear after calc | Integration | ✅ Pass |
| 6*7=42 workflow | Integration | ✅ Pass |
| Division by zero GUI | Integration | ✅ Pass |

**Total: 16 tests, all passing**
