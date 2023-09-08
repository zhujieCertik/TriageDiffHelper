What is it? \
This is a python script that can help you easily triage diff results when you are refining a rule.

How to use?

1. copy both result logs from defect page into `a.txt` and `b.txt`
2. run command:  `python3 test.py` \
   the output result is like:
    ```
    A is result of pre rule, B is result of current rule
    len of a == 43
    len of b == 44
    len in_a_not_in_b == 0
    len in_b_not_in_a == 1
    len both_have == 43
    ```
3. copy the result of `outA.txt` and `outB.txt` into your detector result google sheet, then you can triage.

